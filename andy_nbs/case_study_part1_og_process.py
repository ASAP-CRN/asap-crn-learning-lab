# %%

# compose SN subset dataset for further analysis
####################################
########### PART 0: make subset
####################################
# case_study_part0.py. (this file)

####################################
########### PART 1: OG process (sc_wf)
####################################
# case_study_part1_og_process.py


####################################
########### PART 2: OG basal-ganglia 
####################################
# case_study_part2_og_basal_ganglia.py

####################################
########### PART 3: CARD process decoupler 
####################################
# case_study_part3_decoupler.py


####################################
########### PART 4: comparisions 
####################################
# case_study_part4_comparisons.py



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
# ## STEP 0. Workspace Setup
# ## STEP 1. load SN raw counts. (.SN.01_full_raw.h5ad)
#    (skip)    ## STEP 1A. make SN MMC raw counts. (.SN.01_mmc.h5ad)
# ## STEP 2. make SN processed (HVG + normalized). (.SN.02_processed.h5ad)

# ## STEP 3. make SN integrate with scVI (.SN.03_scvi.h5ad)

# ## STEP 4. make SN integrate with scVI (.SN.04_scanvi.h5ad)



###########
# ### 1.1 Set dataset paths
# In this example, we are working with the **PMDBS single‑cell RNA‑seq cohort** dataset:
# - **Workflow** → `pmdbs_sc_rnaseq`  
# - **Team** → `cohort`  
# - **Source** → `pmdbs`  
# - **Type** → `sc-rnaseq`  
# These components are combined to construct the bucket and dataset names.  
# We then set the path to the **cohort analysis outputs** and preview the available files.
###########

# %%
###########
# ## STEP 0. Workspace Setup

#set general folder paths
HOME = Path.home()
WS_ROOT = HOME / "workspace"
DATA_DIR = WS_ROOT / "data"
WS_FILES = WS_ROOT / "ws_files"

if not WS_ROOT.exists():
    print(f"{WS_ROOT} doesn't exist. We need to remount our resources")
    !wb resource mount    

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
# ## STEP 1. load SN raw counts. (.SN.01_full_raw.h5ad)
#    (skip)    ## STEP 1A. make SN MMC raw counts. (.SN.01_mmc.h5ad)
# %%
sn_full_raw_filename = (
    local_data_path / f"asap-{dataset_team}.SN.01_full_raw.h5ad"
)

# %%
adata = sc.read_h5ad(sn_full_raw_filename)

# %%
# Make a raw counts layer
adata.layers['counts'] = adata.X.copy()
adata.raw = adata
# %%
# Calculate QC metrics
## do we need to re-do this?

# Normalize data
sc.pp.normalize_total(adata)
# Logarithmize the data
sc.pp.log1p(adata)
# Save the normalized-log data
adata.layers['log-norm']=adata.X.copy() 


# %%
# export
sn_full_norm_filename = (
    local_data_path / f"asap-{dataset_team}.SN.02_raw_norm.h5ad"
)
adata.write_h5ad(sn_full_norm_filename)

# %%
###########
# ## STEP 2. make SN processed (HVG + normalized). (.SN.02_processed.h5ad)
# # Open the RNA merged and filtered
# adata = sc.read_h5ad(sn_neuronal_full_samples_filename)
n_top_genes = 3000
min_cells = 5
n_comps = 30

# %%

# Select for the most variable genes
sc.pp.highly_variable_genes(
    adata, 
    layer='log-norm',
    n_top_genes=n_top_genes)

# Double check that no transcripts not found in cells are in the atlas
sc.pp.filter_genes(adata, min_cells=min_cells)

#TODO:
# double-chck against marker genes?



# 

# Make a copy of the AnnData atlas that only contains variable genes
filtered_adata = adata[:, (adata.var['highly_variable']) & ~(adata.var['mt']) & ~(adata.var['rb'])].copy()



# %%
# calculate pca
sc.pp.pca(filtered_adata, n_comps=n_comps)


# %%
# export
sn_processed_filename = (
    local_data_path / f"asap-{dataset_team}.SN.02_processed.h5ad"
)



adata.write_h5ad(sn_processed_filename)

#%%
###########
adata = sc.read_h5ad(sn_processed_filename)
# ## STEP 3. make SN integrate with scVI (.SN.03_scvi.h5ad)
batch_key = "sample"
n_layers = 2
n_latent = n_comps # defined above
###
print(torch.cuda.is_available())

scvi.settings.seed = 0
torch.set_float32_matmul_precision('high')

# Setup SCVI on the data layer
scvi.model.SCVI.setup_anndata(
    adata, layer="counts", batch_key=batch_key)

# Add the parameters of the model
vae = scvi.model.SCVI(
    adata, 
    dispersion="gene-batch", 
    n_layers=2, 
    n_latent=30, 
    gene_likelihood="nb"
)

# Train the model
vae.train(
    max_epochs=1000,
    accelerator='gpu',  
    early_stopping=True,
    early_stopping_patience=20
)

# Extract the elbo plot of the model and save the values
elbo = model.history['elbo_train']
elbo['elbo_validation'] = model.history['elbo_validation']
# elbo.to_csv(sys.argv[3], index=False)

# Convert the cell barcode to the observable matrix X_scvi which neighbors and UMAP can be calculated from
adata.obs['atlas_identifier'] = adata.obs.index.to_list()
adata.obsm['X_scvi'] = model.get_latent_representation()

# Calculate nearest neighbors and the UMAP from the X_scvi observable matrix
sc.pp.neighbors(adata, use_rep='X_scvi')
sc.tl.umap(adata, min_dist=0.3)
# Calculate the leiden distance from the nearest neighbors, use a couple resolutions
sc.tl.leiden(adata, resolution=2, key_added='leiden_2')
sc.tl.leiden(adata, key_added='leiden')
sc.tl.leiden(adata, resolution=.5, key_added='leiden_05')


# Save the anndata object
sn_neuronal_full_samples_filename = (
    local_data_path / f"asap-{dataset_team}.SN.03_scvi.h5ad"
)

adata.write_h5ad(sn_neuronal_full_samples_filename)

scvi_model_filename = (
    local_data_path / f"asap-{dataset_team}.SN.03_scvi_model.pkl"
)

vae.save(scvi_model_filename, overwrite=True)



# %%
###########
# ## STEP 4... 
# ## STEP 4-MMC. compute mmc on raw data (.SN.04_mmc.h5ad)
# ## STEP 4-MMC.  

# https://released-taxonomies-802451596237-us-west-2.s3.us-west-2.amazonaws.com/HMBA/BasalGanglia/BICAN_05072025_pre-print_release/MapMyCells/Human.precomputed_stats.20250507.h5
# https://released-taxonomies-802451596237-us-west-2.s3.us-west-2.amazonaws.com/HMBA/BasalGanglia/BICAN_05072025_pre-print_release/MapMyCells/Human.query_markers.20250507.json

# have to use ENSG ids for this mapmycells taxonomy
# prep data

# %%
sn_full_raw_filename = (
    local_data_path / f"asap-{dataset_team}.SN.01_full_raw.h5ad"
)

# %%
adata = sc.read_h5ad(sn_full_raw_filename)

# Preserve gene_name as a column
adata_mmc = adata.copy()
adata_mmc.var["gene_name"] = adata_mmc.var.index

# 2. Set var_names to gene_id (ENSG IDs)
adata_mmc.var_names = adata_mmc.var["gene_id"].astype(str)



# 3. Ensure uniqueness
adata_mmc.var_names_make_unique()

# Quick check
print(adata_mmc.var.head())
print(adata_mmc.var_names[:5])



sn_mmc_filename = (
    local_data_path / f"asap-{dataset_team}.SN.04_mmc.h5ad"
)

adata_mmc.write_h5ad(sn_mmc_filename)

###########
# ## STEP 4-phenotype. MMC phenotype (.SN.04_mmc_processed.h5ad)





sn_mmc_pheno_filename = (
    local_data_path / f"asap-{dataset_team}.SN.04_mmc_processed.h5ad"
)

adata.write_h5ad(sn_mmc_pheno_filename)








#!/usr/bin/env python3

# import muon.pp.filter_obs as filter_obs ???
# import muon as mu
import scanpy as sc
import argparse
import pandas as pd
import sys
from anndata import AnnData
from pathlib import Path
import os
import pyarrow

sys.path.append("/opt/scripts/utility")
from helpers import update_validation_metrics


# os.environ["AIBS_BKP_USE_TORCH"] = "false"
# os.environ["NUMEXPR_NUM_THREADS"] = "1"
# os.environ["MKL_NUM_THREADS"] = "1"
# os.environ["OMP_NUM_THREADS"] = "1"

# CHUNK_SIZE = 40000
# N_RUNNERS_UP = 5
# RNG_SEED = 11235813
# N_PROCESSORS = 8
# MAX_GB = 48.0


#%%
###########
# ## STEP 4. make SN transfer cell-type with scanvVI (.SN.04_scanvi.h5ad)

sn_scanvi_filename = (
    local_data_path / f"asap-{dataset_team}.SN.04_scanvi.h5ad"
)

adata.write_h5ad(sn_scanvi_filename)





############################################
# we want to remove doublets from the contingency table by doing somethign smart... but first we have to get HVG and 


#######################
# # FEATURE SELECTION
#######################
# # Read in AnnData atlas object
adata = ad.read_h5ad(snakemake.input.merged_rna_anndata)



#######################
### MODEL
#######################




#######################
### MODEL
#######################


# %%
# ## STEP 4. make SN integrate with scanVI (.SN.04_scanvi.h5ad)





# %%

