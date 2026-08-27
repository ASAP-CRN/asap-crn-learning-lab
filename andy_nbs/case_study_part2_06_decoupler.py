# %%
###########################################
# pip3 install -U scvi-tools[cuda]  # gets jax and jaxlib, updates cuda
# pip3 install -U scib-metrics
# . pip install pydeseq2
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

from pydeseq2.dds import DeseqDataSet, DefaultInference
from pydeseq2.ds import DeseqStats

# %%
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
###########
# %%
sn_full_raw_filename = local_data_path / f"asap-{dataset_team}.SN.01_full_raw.h5ad"

# %%
sn_full_norm_filename = local_data_path / f"asap-{dataset_team}.SN.02_raw_norm.h5ad"

# %%
#################################
sn_processed_filename = local_data_path / f"asap-{dataset_team}.SN.02_processed.h5ad"

#################################
sn_integrated_filename = local_data_path / f"asap-{dataset_team}.SN.03_scvi.h5ad"
sn_scvi_full_filename = local_data_path / f"asap-{dataset_team}.SN.03_scvi_full.h5ad"
#################################
sn_mmc_filename = local_data_path / f"asap-{dataset_team}.SN.04_mmc.h5ad"
sn_mmc_pheno_filename = (
    local_data_path / f"asap-{dataset_team}.SN.04_mmc_processed.h5ad"
)
#################################                                                                                                                                       ∑ …………  ∑    …∑ ∑…∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∑∑                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   ∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑……………………………………………∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂∂
sn_scanvi_filename = local_data_path / f"asap-{dataset_team}.SN.05_scanvi.h5ad"
output_cell_types_file = (
    local_data_path / f"asap-{dataset_team}.SN.05_scanvi_cell_types.parquet"
)
#################################
sn_mmc_pheno_filename_v2 = (
    local_data_path / f"asap-{dataset_team}.SN.04_mmc_processed_v2.h5ad"
)
sn_scanvi_filename_v2 = local_data_path / f"asap-{dataset_team}.SN.05_scanvi_v2.h5ad"

output_cell_types_file_v2 = (
    local_data_path / f"asap-{dataset_team}.SN.05_scanvi_cell_types_v2.parquet"
)
#################################
sn_mmc_pheno_filename_v3 = (
    local_data_path / f"asap-{dataset_team}.SN.04_mmc_processed_v3.h5ad"
)
sn_scanvi_filename_v3 = local_data_path / f"asap-{dataset_team}.SN.05_scanvi_v3.h5ad"
output_cell_types_file_v3 = (
    local_data_path / f"asap-{dataset_team}.SN.05_scanvi_cell_types_v3.parquet"
)
#################################
# %%
adata = sc.read_h5ad(sn_mmc_pheno_filename)

# %%
#####################
### STEP 2: decoupler (follow CARD scMAVERICS pipeline (annotate.py)
#####################

# use decoupler to do psuedobulk and differential expression

# samples = pd.read_csv(metadata_table)[sample_key].tolist()
# disease_param = 'Primary Diagnosis' # Name of the disease parameter
# control = 'control' # Define disease states
# diseases = ['PD', 'DLB'] # Disease states to compare, keep as list of strings, unnecessary
# cell_types = pd.read_csv(gene_markers_file)['cell type'] # Define the cell types to look for, from gene marker file
# design_covariates = ['Age','Sex'] # Design factors/covariates for DGEs and DARs

all_adata = sc.read_h5ad(sn_mmc_pheno_filename)
all_adata.var_names_make_unique()
sample_key = "sample"
disease_param = "condition_id"
cell_type_key = "class_name"

cell_types = all_adata.obs[cell_type_key].unique().tolist()
# %%

for cell_type in cell_types:
    if cell_type == cell_types[0]:
        continue
    # Subset to cell type
    adata = all_adata[all_adata.obs[cell_type_key] == cell_type].raw.to_adata()

    # dc.pp.pseudobulk(adata, sample_col, groups_col, layer=None, raw=False, empty=False, mode='sum', skip_checks=False, bsize=250000, verbose=True)
    pdata = dc.pp.pseudobulk(
        adata,
        sample_col=sample_key,
        groups_col=disease_param,
        # layer='counts',
        # raw=True, # could probably just use raw=True, layer=None (default)
        mode="sum",
        # min_cells=5,
        # min_counts=5
    )
    # TODO: file bug report with decoupler.  the "raw=True" option does not work
    # ##
    # Store raw counts in layers
    pdata.layers["counts"] = pdata.X.copy()

    # Normalize, scale and compute pca
    sc.pp.normalize_total(pdata, target_sum=1e4)
    sc.pp.log1p(pdata)
    sc.pp.scale(pdata, max_value=10)

    # Return raw counts to X
    dc.pp.swap_layer(pdata, "counts", X_key=None, inplace=True)
    # decoupler.pp.swap_layer(adata, key, X_key='X', inplace=False)

    # Abbreviate diagnosis to avoid space syntax error
    pdata.obs["comparison"] = pdata.obs[disease_param]

    # # dc.get_metadata_associations(
    # #     pdata,
    # #     obs_keys = ['comparison', 'psbulk_n_cells', 'psbulk_counts'],  # Metadata columns to associate to PCs
    # #     obsm_key='X_pca',  # Where the PCs are stored
    # #     uns_key='pca_anova',  # Where the results are stored
    # #     inplace=True,
    # # )

    # dc.tl.rankby_obsm(adata, "X_pca")

    # # or, to perform based on a subset of obs columns.
    # dc.tl.rankby_obsm(
    #     pdata,
    #     "X_pca",
    #     obs_keys=['comparison', 'psbulk_n_cells', 'psbulk_counts'],
    #     uns_key='pca_anova',  # Where the results are stored
    # )

    # CSV pseudobulk
    adata_df = pd.DataFrame(pdata.X)
    sample_cell = pdata.obs[[sample_key, cell_type_key, disease_param]]
    adata_df.columns = pdata.var_names.to_list()
    adata_df.index = sample_cell.index
    adata_df = pd.merge(
        left=sample_cell, right=adata_df, left_index=True, right_index=True
    )

    celltype_pseudobulk_filename = (
        local_data_path / f"asap-{dataset_team}.SN.06_{cell_type}_pseudobulk.csv"
    )
    adata_df.to_csv(celltype_pseudobulk_filename, index=False)

    # # Select gene specific profiles
    # pdata_genes = dc.filter_by_expr(
    #     pdata,
    #     group='comparison',
    #     min_count=10,
    #     min_total_count=15
    #     )

    # # Subset valuable genes
    # pdata = pdata[:, pdata_genes].copy()

    # # Determine the number of cpus to use
    # inference = DefaultInference(n_cpus=64)

    # Design the differential expression analysis with covariates
    inference = DefaultInference(n_cpus=8)

    dds = DeseqDataSet(
        adata=pdata,
        design_factors=["comparison"],
        refit_cooks=True,
        inference=inference,
    )

    # Compute log-fold changes
    dds.deseq2()

    disease_name = "PD"
    control_name = "Control"

    # Extract contrast between control and disease states
    stat_res = DeseqStats(
        dds,
        contrast=["comparison", disease_name, control_name],
        inference=inference,
    )

    # Compute Wald test
    stat_res.summary()

    # Extract results
    DGE_results_df = stat_res.results_df
    DGE_results_df["-log10_padj"] = -np.log10(DGE_results_df["padj"])
    DGE_output_filename = (
        local_data_path / f"asap-{dataset_team}.SN.06_{cell_type}_DGE.csv"
    )
    DGE_results_df.to_csv(DGE_output_filename)

    # # Plot
    # dc.plot_volcano_df(
    #     DGE_results_df,
    #     x="log2FoldChange",
    #     y="padj",
    #     top=20,
    #     lFCs_thr=1,
    #     sign_thr=1e-2,
    #     figsize=(4, 4),
    # )

    # plt.title(f"{control_name} vs. {disease_name} in {cell_type}")
    # plt.tight_layout()
    # volcano_plot_filename = (
    #     local_data_path / f"asap-{dataset_team}.SN.06_{cell_type}_volcano_plot.png"
    # )
    # plt.savefig(volcano_plot_filename, dpi=300)

#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################

# %%
#################################################

doublet_clusters = []
for cluster in adata.obs["leiden_2"].drop_duplicates():
    # print(cluster, adata[adata.obs['leiden'] == cluster].obs['doublet_score'].mean(), adata[adata.obs['leiden'] == cluster].obs['doublet_score'].median())
    if adata[adata.obs["leiden_2"] == cluster].obs["doublet_score"].median() > 0.05:
        doublet_clusters.append(cluster)

adata1 = adata[~adata.obs["leiden_2"].isin(doublet_clusters)].copy()

# %%


doublet_clusters = []
for cluster in adata.obs["leiden"].drop_duplicates():
    # print(cluster, adata[adata.obs['leiden'] == cluster].obs['doublet_score'].mean(), adata[adata.obs['leiden'] == cluster].obs['doublet_score'].median())
    if adata[adata.obs["leiden"] == cluster].obs["doublet_score"].median() > 0.05:
        print(
            cluster, adata[adata.obs["leiden"] == cluster].obs["doublet_score"].median()
        )
        doublet_clusters.append(cluster)

adata2 = adata[~adata.obs["leiden"].isin(doublet_clusters)].copy()

print(f"adata1: {adata1.shape}, adata2: {adata2.shape}, adata: {adata.shape}")
# %%

# Run over-represenation analysis based on cell markers
# provided in the marker_gene_df DataFrame.
# # Create the DataFrame of canonical gene markers (This can be expanded)
marker_gene_filename = "./example_marker_genes.csv"
marker_gene_df = pd.read_csv(marker_gene_filename)


marker_net = pd.DataFrame()
marker_net["source"] = marker_gene_df["cell type"]
marker_net["target"] = marker_gene_df["official gene symbol"]
# for src in marker_net["source"].unique():
#     n = len(marker_net[marker_net["source"] == src])
#     weight = (1/n)
#     marker_net.loc[marker_net["source"] == src, "weight"] = weight

net_ = marker_net.drop_duplicates(subset=["source", "target"])


bdata = adata.raw.to_adata()
# check that marker genes are in the adata object
for g in net_["target"]:
    assert g in bdata.var_names, f"{g} not found in var_names!"


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


## I don't understand these doublet_clusters things.

# doublet_clusters = []
# for cluster in adata.obs["leiden_2"].drop_duplicates():
#     # print(cluster, adata[adata.obs['leiden'] == cluster].obs['doublet_score'].mean(), adata[adata.obs['leiden'] == cluster].obs['doublet_score'].median())
#     if adata[adata.obs["leiden_2"] == cluster].obs["doublet_score"].median() > 0.05:
#         doublet_clusters.append(cluster)

# adata = adata[~adata.obs["leiden_2"].isin(doublet_clusters)].copy()


# doublet_clusters = []
# for cluster in adata.obs["leiden"].drop_duplicates():
#     # print(cluster, adata[adata.obs['leiden'] == cluster].obs['doublet_score'].mean(), adata[adata.obs['leiden'] == cluster].obs['doublet_score'].median())
#     if adata[adata.obs["leiden"] == cluster].obs["doublet_score"].median() > 0.05:
#         doublet_clusters.append(cluster)

# adata = adata[~adata.obs["leiden"].isin(doublet_clusters)].copy()


# %%
# dc.mt.ora(adata, net_, tmin=1)

# Normalize data
sc.pp.normalize_total(bdata)
# Logarithmize the data
sc.pp.log1p(bdata)
# Save the normalized-log data
bdata.layers["log-norm"] = bdata.X.copy()

dc.mt.ora(bdata, net_, tmin=1, verbose=True)

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
