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


###########################################


# %%
##
# pip3 install -U scvi-tools[cuda]  # gets jax and jaxlib, updates cuda
# pip3 install -U scib-metrics
#
#
####################################
########### PART 2: OG basal-ganglia 
####################################
# case_study_part2_og_basal_ganglia.py


####################################
###########  STEPS 
# STEP 0: imports
# 
import pandas as pd
import numpy as np
import scanpy as sc
import seaborn as sns
import matplotlib.pyplot as plt
import sys, subprocess, importlib, warnings, math, os

from pathlib import Path

# map my cells
import json
import cell_type_mapper
from abc_atlas_access.abc_atlas_cache.abc_project_cache import AbcProjectCache
from cell_type_mapper.cli.from_specified_markers import FromSpecifiedMarkersRunner

import os


###########################################
# ## STEP 1. Workspace Setup
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


# Create the directory if it doesn't already exist
if not local_data_path.exists():
    local_data_path.mkdir(parents=True)

print(f"Local data directory ready at: {local_data_path}")

# %%
# Downloading the anndata object
# Define the expected local path
adata_local_path = local_data_path / f"asap-{dataset_team}.final.h5ad"

# %%
###########
# #  1.2.  Copy Data Locally
###########


#Define metadata folder path
ds_metadata_path = WS_FILES / "metadata/cohort-pmdbs-sc-rnaseq/metadata"


# %%
#####################
### Export SN - Subset
#####################
sn_samples_filename = local_data_path / f"asap-{dataset_team}.sn_samples.h5ad"


#%%
#####################
### Load Full Gene Expression for the Subset
#####################

# define file paths 
# full_adata_filename = (
#     cohort_analysis_path / f"asap-{dataset_team}.merged_cleaned_unfiltered.h5ad"
# )
l_full_adata_filename = (
    local_data_path / f"asap-{dataset_team}.merged_cleaned_unfiltered.h5ad"
)

# Save full sn neuronal Anndata object


####################################
# ## STEP 1. Workspace Setup

#if starting from here 
sn_full_samples_filename = (
    local_data_path / f"asap-{dataset_team}.full_sn_samples.h5ad"
)



# %%
#####################
### STEP 2: MapMyCells with Human Basal Ganglia Taxonomy 
#####################

### 3.2 MapMyCells with Human Basal Ganglia Taxonomy 
# For more informations please see:
#     https://alleninstitute.github.io/abc_atlas_access/descriptions/HMBA-BG_dataset.html
# %%

# Set paths
precomputed_stats_filepath = ( mapmycells_input_dir / "Human.precomputed_stats.20250507.h5" )
query_markers_filepath =  ( mapmycells_input_dir / "Human.query_markers.20250507.json" )

#### 3.3 Download the taxonomy files required by MapMyCells
# %%
# grab taxonomy files 
if not precomputed_stats_filepath.exists():
    ! wget "https://released-taxonomies-802451596237-us-west-2.s3.us-west-2.amazonaws.com/HMBA/BasalGanglia/BICAN_05072025_pre-print_release/MapMyCells/Human.precomputed_stats.20250507.h5" -O {precomputed_stats_filepath}
if not query_markers_filepath.exists():
    ! wget "https://released-taxonomies-802451596237-us-west-2.s3.us-west-2.amazonaws.com/HMBA/BasalGanglia/BICAN_05072025_pre-print_release/MapMyCells/Human.query_markers.20250507.json" -O {query_markers_filepath}


# %%

##########
# ### 3.4 Prepare data for MapMyCells 
# This taxonomic data uses the ensemble gene annotation IDs, so have to make those accessible to the Mapmycells program 

# have to use ENSG ids for this mapmycells taxonomy
# prep data

# Preserve gene_name as a column
#sn_full_ad = sc.read_h5ad(sn_full_samples_filename)
adata_mmc = sc.read_h5ad(sn_full_samples_filename)

adata_mmc.var["gene_name"] = adata_mmc.var.index

# 2. Set var_names to gene_id (ENSG IDs)
adata_mmc.var_names = adata_mmc.var["gene_id"].astype(str)

# 3. Ensure uniqueness
adata_mmc.var_names_make_unique()

# Quick check
print(adata_mmc.var.head())
print(adata_mmc.var_names[:5])

adata_mmc_filename = ( mapmycells_input_dir / "sn_mapmycells_input.h5ad" )
adata_mmc.write_h5ad(adata_mmc_filename)




##############
## need to run this separately to allow the multi-processing to finish

###############
# %%
# adata_mmc_filename = ( mapmycells_input_dir / "sn_mapmycells_input.h5ad" )
# adata_mmc = sc.read_h5ad(adata_mmc_filename)


# # %%
# marker_ids = set()

# for node, marker_list in query_markers.items():
#     if marker_list is None:
#         continue
#     # Each marker_list is already a list of ENSG IDs
#     marker_ids.update(marker_list)

# print(f"Collected {len(marker_ids)} unique marker IDs across all nodes")

# overlap = marker_ids.intersection(set(adata_mmc.var_names))
# print(f"Overlap with taxonomy markers: {len(overlap)} genes")

# %%
import os
os.environ["NUMEXPR_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"


# paths to files where mapping output will be written
json_dst_path = str( mapmycells_output_dir / "human_sn_mapping.json") 
csv_dst_path = str( mapmycells_output_dir / "human_sn_neruons_mapping.csv")


config = {
    "query_path": str(adata_mmc_filename),
    "extended_result_path": json_dst_path,
    "csv_result_path": csv_dst_path,
    "verbose_csv": True,
    "query_markers": {
       "serialized_lookup":str(query_markers_filepath)
    },
    "precomputed_stats": {
        "path": str(precomputed_stats_filepath)
    },
    "type_assignment": {
        "n_processors": 4,
        "normalization": "raw",
        "bootstrap_factor": 0.5,
        "bootstrap_iteration": 100
    }
}


# %%
# run map my cells
runner = FromSpecifiedMarkersRunner(
    args=[],
    input_data=config
)
runner.run()
# %%

mmc_mapping_filename = ( mapmycells_output_dir / "human_sn_neruons_mapping.csv" )
mmc_res = pd.read_csv(mmc_mapping_filename, comment='#')
mmc_res.columns


### 3.5 Assess Mapmycells results
# %%
mmc_res.Neighborhood_name.value_counts()

# %%
mmc_res.Class_name.value_counts()

# %%

# Set index to cell_id for easy alignment
mapmycells_df = mmc_res.set_index("cell_id")

# validate connection 
print(len(set(mapmycells_df.index).intersection(set(adata_mmc.obs_names))))

# %%
## Integrate adata and mapmycell results
# Add taxonomy labels
adata_mmc.obs["mmc_neighborhood"] = mapmycells_df.loc[adata_mmc.obs_names, "Neighborhood_name"]
adata_mmc.obs["mmc_class"] = mapmycells_df.loc[adata_mmc.obs_names, "Class_name"]

# add confidence scores
if "Neighborhood_bootstrapping_probability" in mapmycells_df.columns:
    adata_mmc.obs["mmc_neighborhood_btstrap_prob"] = mapmycells_df.loc[adata_mmc.obs_names, "Neighborhood_bootstrapping_probability"]

if "Class_name" in mapmycells_df.columns:
    adata_mmc.obs["mmc_class_btstrp_prob"] = mapmycells_df.loc[adata_mmc.obs_names, "Class_bootstrapping_probability"]

# %%

# define low-confidence threshold --> unknown
conf_thresh = 0.7
labels = adata_mmc.obs["mmc_class"].copy()

# mark low-confidence cells as Unknown
low_conf_mask = adata_mmc.obs["mmc_class_btstrp_prob"] < conf_thresh
labels[low_conf_mask] = "Unknown"

# save refined labels
adata_mmc.obs["mmc_class_refined_1"] = labels
# %%
# quick check
print(adata_mmc.obs["mmc_class_refined_1"].value_counts())


sc.pl.umap(adata_mmc, color=["mmc_neighborhood", "mmc_neighborhood_btstrap_prob"])


sc.pl.umap(adata_mmc, color=["mmc_class", "mmc_class_btstrp_prob", "mmc_class_refined_1"])


# %%
# move gene names back to index for readability
# 2. Set var_names to gene_names
adata_mmc.var_names = adata_mmc.var["gene_name"].astype(str)

# 3. Ensure uniqueness
adata_mmc.var_names_make_unique()

# Quick check
print(adata_mmc.var.head())
print(adata_mmc.var_names[:5])

mmc_adata_output_filepath = ( mapmycells_output_dir / "sn_mapmycells_integrated_output.h5ad")
adata_mmc.write_h5ad(mmc_adata_output_filepath)


####################################################
# STEP 3 - integration...
####################################################

# TODO: 


