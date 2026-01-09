# %%
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

# decoupler
import decoupler as dc
import scvi

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


adata = sc.read_h5ad(sn_integrated_filename)


# Double check that no transcripts not found in cells are in the atlas
sc.pp.filter_genes(adata, min_cells=10)

# Make a copy of the AnnData atlas that only contains variable genes
filtered_adata = adata[
    :, (adata.var["highly_variable"]) & ~(adata.var["mt"]) & ~(adata.var["rb"])
].copy()


# %%


# %%
#####################
### STEP 2: decoupler (follow CARD scMAVERICS pipeline (annotate.py)
#####################
# Save full sn neuronal Anndata object

# Open the RNA merged and filtered
adata = filtered_adata.copy()
# %%


# doublet_clusters = []
# for cluster in adata.obs["leiden_2"].drop_duplicates():
#     # print(cluster, adata[adata.obs['leiden'] == cluster].obs['doublet_score'].mean(), adata[adata.obs['leiden'] == cluster].obs['doublet_score'].median())
#     if adata[adata.obs["leiden_2"] == cluster].obs["doublet_score"].median() > 0.05:
#         doublet_clusters.append(cluster)

# adata = adata[~adata.obs["leiden_2"].isin(doublet_clusters)].copy()

# %%
# # Create the DataFrame of canonical gene markers (This can be expanded)
marker_gene_filename = "./example_marker_genes.csv"
marker_gene_df = pd.read_csv(marker_gene_filename)


# doublet_clusters = []
# for cluster in adata.obs["leiden"].drop_duplicates():
#     # print(cluster, adata[adata.obs['leiden'] == cluster].obs['doublet_score'].mean(), adata[adata.obs['leiden'] == cluster].obs['doublet_score'].median())
#     if adata[adata.obs["leiden"] == cluster].obs["doublet_score"].median() > 0.05:
#         doublet_clusters.append(cluster)

# adata = adata[~adata.obs["leiden"].isin(doublet_clusters)].copy()
# %%

# Run over-represenation analysis based on cell markers
# provided in the marker_gene_df DataFrame.

marker_net = pd.DataFrame()
marker_net["source"] = marker_gene_df["cell type"]
marker_net["target"] = marker_gene_df["official gene symbol"]
# for src in marker_net["source"].unique():
#     n = len(marker_net[marker_net["source"] == src])
#     weight = (1/n)
#     marker_net.loc[marker_net["source"] == src, "weight"] = weight

net_ = marker_net.drop_duplicates(subset=["source", "target"])

# toy_ad, net = dc.ds.toy()
# # (
# #     mat: np.ndarray,
# #     cnct: np.ndarray,
# #     starts: np.ndarray,
# #     offsets: np.ndarray,
# #     n_up: int | float | None = None,
# #     n_bm: int | float = 0,
# #     n_bg: int | float | None = 20_000,
# #     ha_corr: int | float = 0.5,
# #     verbose: bool = False,
# # ) -> tuple[np.ndarray, np.ndarray]:


# %%

doublet_clusters = []
for cluster in adata.obs["_leiden_res_0.40"].drop_duplicates():
    # print(cluster, adata[adata.obs['leiden'] == cluster].obs['doublet_score'].mean(), adata[adata.obs['leiden'] == cluster].obs['doublet_score'].median())
    if (
        adata[adata.obs["_leiden_res_0.40"] == cluster].obs["doublet_score"].median()
        > 0.05
    ):
        doublet_clusters.append(cluster)

adata = adata[~adata.obs["_leiden_res_0.40"].isin(doublet_clusters)].copy()


doublet_clusters = []
for cluster in adata.obs["_leiden_res_0.20"].drop_duplicates():
    # print(cluster, adata[adata.obs['leiden'] == cluster].obs['doublet_score'].mean(), adata[adata.obs['leiden'] == cluster].obs['doublet_score'].median())
    if (
        adata[adata.obs["_leiden_res_0.20"] == cluster].obs["doublet_score"].median()
        > 0.05
    ):
        doublet_clusters.append(cluster)

adata = adata[~adata.obs["_leiden_res_0.20"].isin(doublet_clusters)].copy()


# %%
dc.mt.ora(adata, net_, tmin=1)
dc.mt.ora(adata, net_, tmin=1, verbose=True, layer="log-norm")

#  'score_ora', 'padj_ora'
# %%

adata.obsm["score_ora"]
# %%


# %%
# Create a mini AnnData object with the over-represenation
# analysis estimate (p-value of given cell marker)
acts = dc.pp.get_obsm(adata, "score_ora")

# Convert the ORA AnnData object to numpy array to rank
# which cell type for each leiden cluster
acts_v = acts.X.ravel()
max_e = np.nanmax(acts_v[np.isfinite(acts_v)])
acts.X[~np.isfinite(acts.X)] = max_e
# df = dc.tl.rankby_groups(acts, groupby="leiden_2", reference="rest")
df = dc.tl.rankby_group(
    acts, groupby="leiden_2", reference="rest", method="t-test_overestim_var"
)

# Apply the best ranked cell type to a cluster-celltype dictionary
annotation_dict = df.groupby("group").head(1).set_index("group")["name"].to_dict()

# Apply the dictionary to the AnnData object
adata.obs["cell_type"] = [annotation_dict[clust] for clust in adata.obs["leiden_2"]]

# Save the cell barcode, cluster, cell-type, and batch values to a .csv

decoupler_output_filename = (
    local_data_path / f"asap-{dataset_team}.SN.06_decoupler_output.csv"
)

adata.obs[["atlas_identifier", "leiden_2", "cell_type", "sample"]].to_csv(
    decoupler_output_filename, index=False
)


# Save the annotated AnnData object
sn_decoupler_output_filename = (
    local_data_path / f"asap-{dataset_team}.SN.06_decoupler_output.h5ad"
)
adata.write_h5ad(filename=sn_decoupler_output_filename, compression="gzip")
