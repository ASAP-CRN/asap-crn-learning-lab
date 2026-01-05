# %%
import pandas as pd
import numpy as np
import scanpy as sc
import seaborn as sns
import matplotlib.pyplot as plt
import sys, subprocess, importlib, warnings, math, os

from pathlib import Path

import torch
import scvi

# %%
##
# pip3 install -U scvi-tools[cuda]  # gets jax and jaxlib, updates cuda
# pip3 install -U scib-metrics
#
#
####################################
########### PART 1: OG process (sc_wf)
####################################
# case_study_part1_og_process.py


####################################
###########  STEPS
####################################


# %%
###########
# ## STEP 0. Workspace Setup

# set general folder paths
HOME = Path.home()
WS_ROOT = HOME / "workspace"
DATA_DIR = WS_ROOT / "data"
WS_FILES = WS_ROOT / "ws_files"

# if not WS_ROOT.exists():
#     print(f"{WS_ROOT} doesn't exist. We need to remount our resources")
#     !wb resource mount

print("Home directory:     ", HOME)
print("Workspace root:     ", WS_ROOT)
print("Data directory:     ", DATA_DIR)
print("ws_files directory: ", WS_FILES)

print("\nContents of workspace root:")
for p in WS_ROOT.glob("*"):
    print(" -", p.name, "/" if p.is_dir() else "")
# %%
## Build and set path to desired dataset
DATASETS_PATH = WS_ROOT / "01_PMDBS" / "PMDBS_sc_rnaseq"

workflow = "pmdbs_sc_rnaseq"
dataset_team = "cohort"
dataset_source = "pmdbs"
dataset_type = "sc-rnaseq"

bucket_name = f"asap-curated-{dataset_team}-{dataset_source}-{dataset_type}"
dataset_name = f"asap-{dataset_team}-{dataset_source}-{dataset_type}"

dataset_path = DATASETS_PATH / bucket_name / workflow
print("Dataset Path:", dataset_path)

# Build the folder path to the cohort analysis directory
cohort_analysis_path = dataset_path / "cohort_analysis"

# Preview the directory contents
# Define a local path for workshop files
local_data_path = WS_FILES / "case_study_01"

# map my cells directories
mapmycells_input_dir = local_data_path / "mapmycells/input"
mapmycells_output_dir = local_data_path / "mapmycells/output"

# other directories
resources_path = local_data_path / "resources"
plots_path = local_data_path / "output_plots"
output_path = local_data_path / "output_matrices"

print(f"Local data directory ready at: {local_data_path}")
# %%
###########
sn_full_raw_filename = local_data_path / f"asap-{dataset_team}.SN.01_full_raw.h5ad"

# %%
sn_full_norm_filename = local_data_path / f"asap-{dataset_team}.SN.02_raw_norm.h5ad"

# %%
###########
sn_processed_filename = local_data_path / f"asap-{dataset_team}.SN.02_processed.h5ad"

n_comps = 30

# %%
###########
adata = sc.read_h5ad(sn_processed_filename)
# ## STEP 3. make SN integrate with scVI (.SN.03_scvi.h5ad)
batch_key = "sample"
n_layers = 2
n_latent = n_comps  # defined above
###
print(torch.cuda.is_available())

scvi.settings.seed = 0
torch.set_float32_matmul_precision("high")

# Setup SCVI on the data layer
scvi.model.SCVI.setup_anndata(adata, layer="counts", batch_key=batch_key)

# Add the parameters of the model
vae = scvi.model.SCVI(
    adata, dispersion="gene-batch", n_layers=2, n_latent=30, gene_likelihood="nb"
)

# Train the model
vae.train(
    max_epochs=1000, accelerator="gpu", early_stopping=True, early_stopping_patience=20
)

# Extract the elbo plot of the model and save the values
elbo = vae.history["elbo_train"]
elbo["elbo_validation"] = vae.history["elbo_validation"]
# elbo.to_csv(sys.argv[3], index=False)

# Convert the cell barcode to the observable matrix X_scvi which neighbors and UMAP can be calculated from
adata.obs["atlas_identifier"] = adata.obs.index.to_list()
adata.obsm["X_scvi"] = vae.get_latent_representation()

# Calculate nearest neighbors and the UMAP from the X_scvi observable matrix
sc.pp.neighbors(adata, use_rep="X_scvi")
sc.tl.umap(adata, min_dist=0.3)
# Calculate the leiden distance from the nearest neighbors, use a couple resolutions
sc.tl.leiden(adata, resolution=2, key_added="leiden_2")
sc.tl.leiden(adata, key_added="leiden")
sc.tl.leiden(adata, resolution=0.5, key_added="leiden_05")


# Save the anndata object
sn_integrated_filename = local_data_path / f"asap-{dataset_team}.SN.03_scvi.h5ad"

adata.write_h5ad(sn_integrated_filename)

scvi_model_filename = local_data_path / f"asap-{dataset_team}.SN.03_scvi_model.pkl"

vae.save(scvi_model_filename, overwrite=True)
# %%
