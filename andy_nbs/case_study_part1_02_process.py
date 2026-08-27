# %%
import pandas as pd
import numpy as np
import scanpy as sc
import seaborn as sns
import matplotlib.pyplot as plt
import sys, subprocess, importlib, warnings, math, os

from pathlib import Path

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
adata.raw = adata.copy()
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
sn_full_norm_filename = (
    local_data_path / f"asap-{dataset_team}.SN.02_raw_norm.h5ad"
)
adata = sc.read_h5ad(sn_full_norm_filename)
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
hvg = adata.var['highly_variable']
hvgs = adata.var[hvg].index.tolist()
# %%
# load the GP2 GWAS target genes for comparison of HVG
targets = pd.read_csv("./genes_by_locus.csv")
target_genes = targets["GENE"].tolist()

# %%
# get the intersection between hvgs and target genes
overlap = set(hvgs).intersection(set(target_genes))

adata.var["overlap"] = adata.var.index.isin(overlap)
adata.var["gwas_target"] = adata.var.index.isin(target_genes)

keep_genes = set(hvgs) | set(target_genes)
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

filtered_adata.write_h5ad(sn_processed_filename)


#%%
#################################
adata = sc.read_h5ad(sn_processed_filename)

# %%
sn_full_norm_filename
adata = sc.read_h5ad(sn_full_norm_filename)
