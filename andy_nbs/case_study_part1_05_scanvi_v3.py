# %%
####################################

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

###########
# ## STEP 0. Workspace Setup

# set general folder paths
HOME = Path.home()
WS_ROOT = HOME / "workspace"
DATA_DIR = WS_ROOT / "data"
WS_FILES = WS_ROOT / "ws_files"

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

# Make sure the directories exists
os.makedirs(mapmycells_input_dir, exist_ok=True)
os.makedirs(mapmycells_output_dir, exist_ok=True)
os.makedirs(resources_path, exist_ok=True)
os.makedirs(output_path, exist_ok=True)
os.makedirs(plots_path, exist_ok=True)

# Create the directory if it doesn't already exist
if not local_data_path.exists():
    local_data_path.mkdir(parents=True)

print(f"Local data directory ready at: {local_data_path}")
# %%
###########
# %%
sn_full_raw_filename = local_data_path / f"asap-{dataset_team}.SN.01_full_raw.h5ad"

# %%
sn_full_norm_filename = local_data_path / f"asap-{dataset_team}.SN.02_raw_norm.h5ad"

# %%
#################################
sn_processed_filename = local_data_path / f"asap-{dataset_team}.SN.02_processed.h5ad"

# Save the anndata object
sn_integrated_filename = local_data_path / f"asap-{dataset_team}.SN.03_scvi.h5ad"

# output file neame
sn_mmc_pheno_filename = (
    local_data_path / f"asap-{dataset_team}.SN.04_mmc_processed.h5ad"
)

sn_mmc_pheno_filename_v3 = (
    local_data_path / f"asap-{dataset_team}.SN.04_mmc_processed_v3.h5ad"
)

# have to use ENSG ids for this mapmycells taxonomy
# prep data
# %%


###########
adata = sc.read_h5ad(sn_mmc_pheno_filename_v3)
# ## STEP 3. make SN integrate with scVI (.SN.03_scvi.h5ad)
batch_key = "sample"
n_layers = 2
n_comps = adata.obsm["X_pca"].shape[1]
n_latent = n_comps  # defined above
predictions_key = "C_scANVI"
###
print(torch.cuda.is_available())

scvi.settings.seed = 0
torch.set_float32_matmul_precision("high")


scvi_model_filename = local_data_path / f"asap-{dataset_team}.SN.03_scvi_model"
vae = scvi.model.SCVI.load(scvi_model_filename)


# %%
# %%
def label_with_scanvi(
    adata: sc.AnnData,
    model: scvi.model.SCVI,
    num_workers: int,
    latent_key: str | None = None,
    predictions_key: str | None = None,
    workflow_name: str = "generic_000",
) -> tuple[sc.AnnData, scvi.model.SCANVI]:
    """
    Fit scANVI model to AnnData object
    """

    # Fixed parameters
    scanvi_epochs = 1000
    batch_size = 1024
    accelerator = "gpu"
    dispersion = "gene-batch"  # "gene"
    gene_likelihood = "zinb"
    latent_distribution = "normal"
    early_stopping = True
    early_stopping_patience = 20

    if latent_key is None:
        latent_key = f"X_scANVI"
    if predictions_key is None:
        predictions_key = f"C_scANVI"

    # if adata.n_obs > threshold_cells:
    #     plan_kwargs = {"lr": 1e-4}
    #     gradient_clip_val = 5.0
    #     print(f"AnnData object contains {adata.n_obs} which is > {threshold_cells}")
    #     print(f"--- Using learning rate: {plan_kwargs}")
    #     print(f"--- Using gradient clipping: {gradient_clip_val}")
    # else:
    # Defaults
    plan_kwargs = {"lr": 1e-3}
    gradient_clip_val = None
    # print(f"AnnData object contains {adata.n_obs} which is < {threshold_cells}")
    # print(f"--- Using default learning rate: {plan_kwargs}")
    # print(f"--- Using default gradient clipping: {gradient_clip_val}")

    print("Generating scANVI model from scVI")
    scanvi_model = scvi.model.SCANVI.from_scvi_model(
        model,
        adata=adata,
        labels_key="cell_type",
        unlabeled_category="Unknown",
    )

    print("Training scANVI model")
    scanvi_model.train(
        accelerator=accelerator,
        max_epochs=scanvi_epochs,
        early_stopping=early_stopping,
        early_stopping_patience=early_stopping_patience,
        datasplitter_kwargs={"num_workers": num_workers},
        gradient_clip_val=gradient_clip_val,
        plan_kwargs=plan_kwargs,
    )

    print("Generating scANVI latents and predictions")
    adata.obsm[latent_key] = scanvi_model.get_latent_representation(adata)
    adata.obs[predictions_key] = scanvi_model.predict(adata)

    return (adata, scanvi_model)


# %%
num_workers = 0  # Pytorch bug unable to mmap solution https://github.com/pytorch/pytorch/issues/92134
scvi.settings.dl_num_workers = num_workers
print(f"Using {scvi.settings.dl_num_workers} workers")

# 4. Get scANVI model
workflow_name = "case_study_01"
adata, scanvi_model = label_with_scanvi(
    adata,
    vae,
    num_workers,
    workflow_name=workflow_name,
    predictions_key=predictions_key,
)

# 5. Save the integrated adata and scANVI model
# %%
scanvi_model_filename = local_data_path / f"asap-{dataset_team}.SN.05_scanvi_model_v3"

scanvi_model.save(scanvi_model_filename, overwrite=True)
# 6. Save the latent space
# output file neame
sn_scanvi_filename = local_data_path / f"asap-{dataset_team}.SN.05_scanvi_v3.h5ad"

adata.write_h5ad(filename=sn_scanvi_filename, compression="gzip")
# 7. Save the cell types to feather
# adata.obs[[args.predictions_key]].to_feather(args.output_cell_types_file, compression="gzip")
# 7. Save the cell types to parquet

output_cell_types_file = (
    local_data_path / f"asap-{dataset_team}.SN.05_scanvi_cell_types_v3.parquet"
)

adata.obs[[predictions_key]].to_parquet(output_cell_types_file, compression="gzip")

# %%
scanvi_model.history["elbo_train"].plot(figsize=(5, 3))
scanvi_model.history["elbo_validation"].plot(figsize=(5, 3))
# %%
