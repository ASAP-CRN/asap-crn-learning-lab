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


# have to use ENSG ids for this mapmycells taxonomy
# prep data
# %%
sn_mmc_filename = local_data_path / f"asap-{dataset_team}.SN.04_mmc.h5ad"



# %%
adata = sc.read_h5ad(sn_full_raw_filename)

###########

n_comps = 30

# %%


sn_processed_filename = local_data_path / f"asap-{dataset_team}.SN.02_processed.h5ad"


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
sn_neuronal_full_samples_filename = (
    local_data_path / f"asap-{dataset_team}.SN.03_scvi.h5ad"
)

adata.write_h5ad(sn_neuronal_full_samples_filename)



scvi_model_filename = local_data_path / f"asap-{dataset_team}.SN.03_scvi_model.pkl"
vae = scvi.model.SCVI.load(scvi_model_filename)




#!/usr/bin/env python3

import os
import argparse
import anndata as ad
import scvi


def label_with_scanvi(
    adata: ad.AnnData,
    model: scvi.model.SCVI,
    num_workers: int,
    workflow_name: str
) -> tuple[ad.AnnData, scvi.model.SCANVI]:
    """
    Fit scANVI model to AnnData object
    """
    
    # Fixed parameters
    scanvi_epochs = 300
    batch_size = 1024
    accelerator = "gpu"
    dispersion = "gene-cell"  # "gene"
    gene_likelihood = "zinb"
    latent_distribution = "normal"
    early_stopping = True
    early_stopping_patience = 20

    # Set parameters based on numerical instabilities and source
    if workflow_name == "pmdbs_sc_rnaseq":
        threshold_cells = 3.05e6 # No. of cells in Sep 2025 PMDBS sc cohort (Lee, Hardy, Hafler, Jakobsson, Scherzer)
    elif workflow_name == "mouse_sc_rnaseq":
        threshold_cells = 1e6 # Approx. no. of cells in Dec 2025 Mouse sc cohort (Cragg, Biederer)
    else:
        raise ValueError(f"[ERROR] Source cannot be detected from workflow name: [{workflow_name}]")
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
    adata.obsm[args.latent_key] = scanvi_model.get_latent_representation(adata)
    adata.obs[args.predictions_key] = scanvi_model.predict(adata)

    return (adata, scanvi_model)


def main(args: argparse.Namespace):
    # Set the number of data loader workers
    #num_workers = max(1, os.cpu_count() - 1)
    num_workers = 0 # Pytorch bug unable to mmap solution https://github.com/pytorch/pytorch/issues/92134
    scvi.settings.dl_num_workers = num_workers
    print(f"Using {scvi.settings.dl_num_workers} workers")

    # 0. Load data
    adata = ad.read_h5ad(args.adata_input)  # type: ignore
    model_path = args.scvi_outputs_dir
    model = scvi.model.SCVI.load(
        dir_path=model_path,
        adata=adata,
    )
    # 4. Get scANVI model
    adata, scanvi_model = label_with_scanvi(adata, model, num_workers, args.workflow_name)
    # 5. Save the integrated adata and scANVI model
    scanvi_model.save(args.output_scanvi_dir, overwrite=True)
    # 6. Save the latent space
    adata.write_h5ad(filename=args.adata_output, compression="gzip")
    # 7. Save the cell types to feather
    # adata.obs[[args.predictions_key]].to_feather(args.output_cell_types_file, compression="gzip")
    # 7. Save the cell types to parquet
    adata.obs[[args.predictions_key]].to_parquet(args.output_cell_types_file, compression="gzip")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Leverage cell-type from MMC to assign the rest of the cells with scANVI")
    parser.add_argument(
        "--workflow-name",
        type=str,
        required=True,
        help="Workflow name to set training parameters based on source ('human' or 'mouse') due to numerical instabilities",
    )
    parser.add_argument(
        "--latent-key",
        type=str,
        required=True,
        help="Latent key to save the scANVI latent to",
    )
    parser.add_argument(
        "--predictions-key",
        type=str,
        required=True,
        help="scANVI cell type predictions column name in AnnData object",
    )
    parser.add_argument(
        "--adata-input",
        type=str,
        required=True,
        help="AnnData object for a dataset",
    )
    parser.add_argument(
        "--scvi-outputs-dir",
        type=str,
        required=True,
        help="Saved scVI outputs folder",
    )
    parser.add_argument(
        "--adata-output",
        type=str,
        required=True,
        help="Output file to save AnnData object to",
    )
    parser.add_argument(
        "--output-scanvi-dir",
        type=str,
        required=True,
        help="Output folder to save scANVI model",
    )
    parser.add_argument(
        "--output-cell-types-file",
        type=str,
        required=True,
        help="Output file to write cell types to",
    )

    args = parser.parse_args()
    main(args)

