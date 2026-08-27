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
sn_integrated_filename = local_data_path / f"asap-{dataset_team}.SN.03_scvi.h5ad"
sn_scvi_full_filename = local_data_path / f"asap-{dataset_team}.SN.03_scvi_full.h5ad"

n_comps = 30

# %%


def integrate_with_scvi(
    adata: sc.AnnData,
    batch_key: str,
    latent_key: str | None = None,
) -> tuple[sc.AnnData, scvi.model.SCVI]:
    """
    Fit scVI model to AnnData object
    """

    # Fixed parameters
    n_latent = 30
    n_layers = 2
    train_size = 0.85
    scvi_epochs = 1000
    batch_size = 1024
    accelerator = "gpu"
    dispersion = "gene-batch"  # "gene"
    gene_likelihood = "zinb"
    latent_distribution = "normal"
    early_stopping = True
    early_stopping_patience = 20

    if latent_key is None:
        latent_key = f"X_scVI"

    # Set parameters based on numerical instabilities
    threshold_cells = 3.05e6  # No. of cells in Sep 2025 PMDBS sc cohort (Lee, Hardy, Hafler, Jakobsson, Scherzer)
    if adata.n_obs > threshold_cells:
        plan_kwargs = {"lr": 1e-4}
        gradient_clip_val = 5.0
        print(f"AnnData object contains {adata.n_obs} which is > {threshold_cells}")
        print(f"--- Using learning rate: {plan_kwargs}")
        print(f"--- Using gradient clipping: {gradient_clip_val}")
    else:
        # Defaults
        plan_kwargs = {"lr": 1e-3}
        gradient_clip_val = None
        print(f"AnnData object contains {adata.n_obs} which is < {threshold_cells}")
        print(f"--- Using default learning rate: {plan_kwargs}")
        print(f"--- Using default gradient clipping: {gradient_clip_val}")

    # Integrate the data with scVI
    # noise = ["doublet_score", "pct_counts_mt", "pct_counts_rb"]
    categorical_covariate_keys = None
    scvi.model.SCVI.setup_anndata(
        adata,
        layer="counts",
        batch_key=batch_key,
        # continuous_covariate_keys=noise,
        # categorical_covariate_keys=categorical_covariate_keys,
    )

    model = scvi.model.SCVI(
        adata,
        n_layers=n_layers,
        n_latent=n_latent,
        dispersion=dispersion,
        gene_likelihood=gene_likelihood,
    )

    model.train(
        train_size=train_size,
        max_epochs=scvi_epochs,
        early_stopping=early_stopping,
        early_stopping_patience=early_stopping_patience,
        accelerator=accelerator,
        gradient_clip_val=gradient_clip_val,
        plan_kwargs=plan_kwargs,
    )

    adata.obsm[latent_key] = model.get_latent_representation()  # type: ignore
    adata.obs["atlas_identifier"] = adata.obs.index.to_list()

    return (adata, model)


###########
# ## STEP 3. make SN integrate with scVI (.SN.03_scvi.h5ad)
batch_key = "sample"
n_layers = 2
n_latent = n_comps  # defined above
###
print(torch.cuda.is_available())

scvi.settings.seed = 0
torch.set_float32_matmul_precision("high")

# Set the number of data loader workers
scvi.settings.dl_num_workers = max(1, os.cpu_count() - 1)
print(f"Using {scvi.settings.dl_num_workers} workers")

# 0. Load data
adata = sc.read_h5ad(sn_processed_filename)

# 2. Process data
adata, vae = integrate_with_scvi(adata, batch_key)

# %%


# Calculate nearest neighbors and the UMAP from the X_scvi observable matrix
sc.pp.neighbors(adata, use_rep="X_scVI")
sc.tl.umap(adata, min_dist=0.3)
# Calculate the leiden distance from the nearest neighbors, use a couple resolutions
sc.tl.leiden(adata, resolution=2, key_added="leiden_2")
sc.tl.leiden(adata, key_added="leiden")
sc.tl.leiden(adata, resolution=0.5, key_added="leiden_05")


# 3. Save the integrated adata and scVI model
sn_integrated_filename = local_data_path / f"asap-{dataset_team}.SN.03_scvi.h5ad"

adata.write_h5ad(sn_integrated_filename)

scvi_model_filename = local_data_path / f"asap-{dataset_team}.SN.03_scvi_model"

vae.save(scvi_model_filename, overwrite=True)
# %%
# 3. Post-processing
# # Extract the elbo plot of the model and save the values
# elbo = vae.history["elbo_train"]
# elbo["elbo_validation"] = vae.history["elbo_validation"]
# # elbo.to_csv(sys.argv[3], index=False)

unfiltered_adata = adata.raw.to_adata()
unfiltered_adata.obs = adata.obs

unfiltered_adata.var_names_make_unique()

# %%
# make sure we have X_scVI

# Convert the cell barcode to the observable matrix X_scvi which neighbors and UMAP can be calculated from

# Calculate nearest neighbors and the UMAP from the X_scvi observable matrix
sc.pp.neighbors(unfiltered_adata, use_rep="X_scVI")
sc.tl.umap(unfiltered_adata, min_dist=0.3)
# Calculate the leiden distance from the nearest neighbors, use a couple resolutions
sc.tl.leiden(unfiltered_adata, resolution=2, key_added="leiden_2")
sc.tl.leiden(unfiltered_adata, key_added="leiden")
sc.tl.leiden(unfiltered_adata, resolution=0.5, key_added="leiden_05")


sn_scvi_full_filename = local_data_path / f"asap-{dataset_team}.SN.03_scvi_full.h5ad"
unfiltered_adata.write_h5ad(sn_scvi_full_filename)
