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

# ## STEP 1. make SN raw counts. (.SN.01_full_raw.h5ad)

###########################################
# STEP 0: imports
import pandas as pd
import numpy as np
import scanpy as sc
import seaborn as sns
import matplotlib.pyplot as plt
import sys, subprocess, importlib, warnings, math, os

from pathlib import Path

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
# #  1.2.  Copy Data Locally
###########

# We now bring in the curated dataset files:

# - **`asap-cohort.final_metadata.csv`** → cell‑level metadata table
# - **`asap-cohort.final.h5ad`** → full AnnData object containing HVG expression data and annotations  

# We copy these files into our local `pilot_workshop_files` directory (if not already present) and load them into memory.

# The metadata CSV is read into a Pandas dataframe, while the `.h5ad` file is loaded as an AnnData object in backed mode.

# %%
# # Downloading obs field (cell metadata)
# # Define the expected local path for the metadata file.
# cell_metadata_local_path = local_data_path / f"asap-{dataset_team}.final_metadata.csv"\

# # Check if the metadata file already exists locally.
# if not cell_metadata_local_path.exists():
#     # Construct the original path where the metadata file is stored.
#     cell_metadata_og_path = cohort_analysis_path / f"asap-{dataset_team}.final_metadata.csv"

#     # Use a shell command (`cp`) to copy the file from the original location
#     # into the local workshop_files directory for analysis.
#     !cp {cell_metadata_og_path} {cell_metadata_local_path}

# %%
# Downloading the anndata object
# Define the expected local path
adata_local_path = local_data_path / f"asap-{dataset_team}.final.h5ad"

# # Check if the adata file already exists locally.
# if not adata_local_path.exists():
#     # Construct the original path where the metadata file is stored.
#     adata_cell_metadata_og_path = cohort_analysis_path / f"asap-{dataset_team}.final.h5ad"

#     # Use a shell command (`cp`) to copy the file from the original location
#     # into the local workshop_files directory for analysis.
#     !cp {adata_cell_metadata_og_path} {adata_local_path}

# load the adata object
adata = sc.read_h5ad(adata_local_path, backed="r")
adata


# %%
###########
# #  1.2.  Copy Data Locally
###########
#Define metadata folder path
ds_metadata_path = WS_FILES / "metadata/cohort-pmdbs-sc-rnaseq/metadata"

#preview contents
!ls {ds_metadata_path} 

# %%
# Sample-level metadata
SAMPLE = pd.read_csv(ds_metadata_path / "SAMPLE.csv", index_col=0)
# Subject-level metadata
SUBJECT = pd.read_csv(ds_metadata_path / "SUBJECT.csv", index_col=0)
#  Brain-sample metadata
PMDBS = pd.read_csv(ds_metadata_path / "PMDBS.csv", index_col=0)
# Experimental condition metadata
CONDITION = pd.read_csv(ds_metadata_path / "CONDITION.csv", index_col=0)

# Select Relevant Columns
sample_cols = [
    "ASAP_sample_id",
    "ASAP_subject_id",
    "ASAP_team_id",
    "ASAP_dataset_id",
    "replicate",
    "condition_id",
    "age_at_collection",
]
subject_cols = [
    "ASAP_subject_id",
    "source_subject_id",
    "sex",
    "primary_diagnosis",
]
pmdbs_cols = [
    "ASAP_sample_id",
    "brain_region",
    "region_level_1",
    "region_level_2",
    "region_level_3",
]
condition_cols = [
    "condition_id",
    "intervention_name",
    "intervention_id",
    "protocol_id",
]
# %%
# patch TEAM_SULZER condition_id.
gp2_phenotype_mapper = {
    "no_pd_nor_other_neurological_disorder": "Control",
    "alzheimers_disease": "Control",
    "other_neurological_disorder": "Control",
    "idiopathic_pd": "PD",
    "Control": "Control",
    "PD": "PD",
    "Prodromal": "Prodromal",
}

CONDITION["condition_id"] = CONDITION["condition_id"].map(gp2_phenotype_mapper)

CONDITION["intervention_id"] = CONDITION["condition_id"].map(
    {"Control": "Control", "PD": "PD", "Prodromal": "Case"}
)

# drop duplicates
CONDITION = CONDITION.drop_duplicates()

# %%
# i don't think merge is right here...
df = pd.merge(
    SAMPLE[sample_cols].copy(),
    CONDITION[condition_cols].copy(),
    on=["condition_id"],
    how="left",  # keep all SAMPLE rows, add CONDITION info
    validate="many_to_many",  # each SAMPLE row maps to one CONDITION row
)

df = pd.merge(
    df,
    SUBJECT[subject_cols],
    on=["ASAP_subject_id"],
    how="left",  # keep all SAMPLE rows, add SUBJECT info
    validate="many_to_many",  # each SUBJECT row maps to multiple SAMPLE rows
)

# Merge in brain-region information
df = pd.merge(
    df, PMDBS[pmdbs_cols], on=["ASAP_sample_id"], how="left", validate="many_to_many"
)

# create unique sample identifier
df["sample"] = df["ASAP_sample_id"] + "_" + df["replicate"]
# %%
# get just the substantia nigra samples
df_nigra = df[df["brain_region"] == "Substantia nigra"]
df_nigra

# %%
# Recode brain region to be "PFC", "MFG", "HIP", "SN", "ACG", "IPL, "AMG", "PUT"
brain_fix = {
    "Prefrontal Cortex": "PFC",
    "Middle_Frontal_Gyrus": "MFG",
    "Hippocampus": "HIP",
    "Substantia_Nigra ": "SN",
    "ACG": "ACG",
    "IPL": "IPL",
    "Middle temporal gyrus": "MTG",
    "Substantia nigra": "SN",
    "Prefrontal cortex": "PFC",
    "Amygdala": "AMG",
    "Putamen": "PUT",
}
df["brain_region"] = df["brain_region"].map(brain_fix)
# %%
# Map to find more course designations
brain_simple = {
    "PFC": "frontal_ctx",
    "MFG": "frontal_ctx",
    "ACG": "cingulate_ctx",
    "IPL": "parietal_ctx",
    "MTG": "temporal_ctx",
    "HIP": "subcortical",
    "AMG": "subcortical",
    "PUT": "subcortical",
    "SN": "subcortical",
}

df["brain_region_simple"] = df["brain_region"].map(brain_simple)


# Define sample to match
br_mapper_full = dict(zip(df["sample"], df["brain_region"]))
br_mapper_simple = dict(zip(df["sample"], df["brain_region"].map(brain_simple)))

# Parkinsons and control samples
condition_id_mapper = dict(zip(df["sample"], df["condition_id"]))
case_id_mapper = dict(zip(df["sample"], df["intervention_name"]))

# Detailed brain region mapper
region_1_mapper = dict(zip(df["sample"], df["region_level_1"]))
region_2_mapper = dict(zip(df["sample"], df["region_level_2"]))

# Diagnoses
diagnoses_mapper = dict(zip(df["sample"], df["primary_diagnosis"]))

dataset_metadata_filen = local_data_path / "asap-cohort-dataset-metadata.csv"
df.to_csv(dataset_metadata_filen)

# %%
# # Map samples to metadata
# adata.obs["brain_region"] = adata.obs["sample"].map(br_mapper_full)
# adata.obs["brain_region_simple"] = adata.obs["sample"].map(br_mapper_simple)
# adata.obs["case_id"] = adata.obs["sample"].map(case_id_mapper)
# adata.obs["condition_id"] = adata.obs["sample"].map(condition_id_mapper)
# adata.obs["region_level_1"] = adata.obs["sample"].map(region_1_mapper)
# adata.obs["region_level_2"] = adata.obs["sample"].map(region_2_mapper)
cell_metadata = adata.obs.copy()

# Map samples to metadata
cell_metadata["brain_region"] = cell_metadata["sample"].map(br_mapper_full)
cell_metadata["brain_region_simple"] = cell_metadata["sample"].map(br_mapper_simple)
cell_metadata["case_id"] = cell_metadata["sample"].map(case_id_mapper)
cell_metadata["condition_id"] = cell_metadata["sample"].map(condition_id_mapper)
cell_metadata["region_level_1"] = cell_metadata["sample"].map(region_1_mapper)
cell_metadata["region_level_2"] = cell_metadata["sample"].map(region_2_mapper)

# %%
#################
## Subset for Substantia Nigra + Neuronal Cells
#################

# identify substantia nigra cells
sn_cells = cell_metadata["brain_region"] == "SN"
# Final boolean mask for subsetting
include = sn_cells

print(sum(include))
# Create SN subset
sn_ad = adata[include].to_memory()
adata.file.close()  # close the original adata file


#
# og_obs = sn_ad.obs.copy()
new_obs = cell_metadata[include]
# new_obs.shape
# cell_metadata.shape, new_obs.shape, og_obs.shape

sn_ad.obs = new_obs

# %%
#####################
### Export SN - Subset
#####################
snn_samples_filename = local_data_path / f"asap-{dataset_team}.sn_samples.h5ad"
sn_ad.write_h5ad(snn_samples_filename)

# note this object includes the normalized log data, PCs etc....

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

# if not l_full_adata_filename.exists():
#     !cp {full_adata_filename} {l_full_adata_filename}

# Load full expression matrix
full_adata = sc.read_h5ad(l_full_adata_filename, backed="r")

#%%
# Extract and select neuronal_subset cells from complete gene expression matrix
var_ = full_adata.var.copy()
X = full_adata[sn_ad.obs_names].X.copy()

uns_ = full_adata.uns.copy()
full_adata.file.close()


# %%
###############
# combine the full gene expression matrix with our substantia nigra neuron subset, and save the resulting AnnDataobject.
# note that below is defined by the normalized log data, PCs etc.....
###############
sn_neuronal_full_ad = sc.AnnData(
    X=X,
    obs=sn_ad.obs,
    var=var_,
    uns=uns_,
    obsm=sn_ad.obsm,
)
sn_neuronal_full_ad

# %%
# keep th eold stuff around  
for key in ['X_pca',
            'X_pca_harmony',
            'X_scANVI',
            'X_scVI',
            'X_umap']:
    new_key = f"_{key}"
    # rename
    sn_neuronal_full_ad.obsm[new_key] = sn_neuronal_full_ad.obsm.pop(key)
    


old_fields = [ 'cell_type',
 'phenotype',
 'rho',
 'prob',
 'class_name',
 'subclass_name',
 'supertype_name',
 '_scvi_batch',
 '_scvi_labels',
 'C_scANVI',
 'leiden_res_0.05',
 'leiden_res_0.10',
 'leiden_res_0.20',
 'leiden_res_0.40'
 ]

for key in old_fields:
    new_key = f"_{key}"
    # rename
    sn_neuronal_full_ad.obs[new_key] = sn_neuronal_full_ad.obs.pop(key)

# %%
#
# Save full sn neuronal Anndata object
sn_neuronal_full_samples_filename = (
    local_data_path / f"asap-{dataset_team}.SN.01_full_raw.h5ad"
)
sn_neuronal_full_ad.write_h5ad(sn_neuronal_full_samples_filename)


