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


import plotly.graph_objects as go
import plotly.express as px


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

#################################
sn_decoupler_output_filename = (
    local_data_path / f"asap-{dataset_team}.SN.06_decoupler_output.h5ad"
)
# Save the cell barcode, cluster, cell-type, and batch values to a .csv

decoupler_output_filename = (
    local_data_path / f"asap-{dataset_team}.SN.06_decoupler_output.csv"
)

#################################
sn_integrated_filename = local_data_path / f"asap-{dataset_team}.SN.03_scvi.h5ad"
sn_scvi_full_filename = local_data_path / f"asap-{dataset_team}.SN.03_scvi_full.h5ad"
#################################
mmc_csv_dst_path = str(mapmycells_output_dir / "SN.04_mmc.human_sn_neruons_mapping.csv")


sn_mmc_filename = local_data_path / f"asap-{dataset_team}.SN.04_mmc.h5ad"
sn_mmc_pheno_filename = (
    local_data_path / f"asap-{dataset_team}.SN.04_mmc_processed.h5ad"
)
#################################

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


# Assumptions:
#     - Basal Ganglia cell-types are reasonable.  (just use the uncollapsed classes)
#     - "target" genes from GWAS will be differentially expressed
#     - no variance due to data from two datasets.  (this is probably wrong, but hopefully scVI mitigates)

# Outline:
#     - summary of confirmation of reasonable DA neuron phenotyping
#           - consistency with CARD marker genes
#           - DA marker genes "score"
#     - "target" genes
#        - Target Gene expression summary (heatmaps)
#        - Case/control breakdown (2x heatmaps)
#     - differential expression analysis
#        - psuedobulk by MMC cell-types
#        - case/control differential expression
#        - heatmap of all 4k targets
#        - dot plot for "top" differentially expressed targets



# %%
mmc_csv_dst_path = str(mapmycells_output_dir / "SN.04_mmc.human_sn_neruons_mapping.csv")


# Results header is the first 4 lines
def read_csv_results(csv_results_path: str | Path) -> pd.DataFrame:
    """
    Read the results file and return a pandas DataFrame
    """
    ## HEADER
    # metadata = asap-cohort.merged_adata_object.mmc.seaad_results.20250129.json
    # taxonomy hierarchy = ["CCN20230505_CLAS", "CCN20230505_SUBC", "CCN20230505_SUPT"]
    # readable taxonomy hierarchy = ["class", "subclass", "supertype"]
    # algorithm: 'hierarchical'; codebase: http://github.com/AllenInstitute/cell_type_mapper; version: v1.4.2
    # cell_id,class_label,class_name,class_bootstrapping_probability,class_correlation_coefficient,class_aggregate_probability,subclass_label,subclass_name,subclass_bootstrapping_probability,subclass_correlation_coefficient,subclas

    results = pd.read_csv(csv_results_path, header=4)
    results.set_index("cell_id", inplace=True)
    results.index.name = None
    return results

phenotype_df = read_csv_results(mmc_csv_dst_path)

# %%
adata = sc.read_h5ad(sn_decoupler_output_filename)
df = pd.read_csv(decoupler_output_filename)


# %%
###################
#     - "target" genes
#        - Target Gene expression summary (heatmaps)
#        - Case/control breakdown (2x heatmaps)



#####################
### STEP 2: decoupler (follow CARD scMAVERICS pipeline (annotate.py)
#####################

# %%
cell_type = "OPC-Oligo"

DGE_filename = (
    local_data_path / f"asap-{dataset_team}.SN.06_{cell_type}_DGE.csv"
)

psuedobulk_filename = (
    local_data_path / f"asap-{dataset_team}.SN.06_{cell_type}_pseudobulk.csv"
)
# %%
dge_df = pd.read_csv(DGE_filename, index_col=0)
dge_df["gene_name"] = dge_df.index
dge_df["cell_type"] = cell_type

# %%
psuedobulk_df = pd.read_csv(psuedobulk_filename, index_col=0)
psuedobulk_df["gene_name"] = psuedobulk_df.index
psuedobulk_df["cell_type"] = cell_type

# %%
## make subset to targets
targets = pd.read_csv("./genes_by_locus.csv")
target_genes = targets["GENE"].tolist()
target_df = psuedobulk_df[dfs["gene_name"].isin(target_genes)]
# sort by -log10_padj
target_df = target_df.sort_values(by="-log10_padj", ascending=False)

## make subset to HVGs
# LOAD asap-cohort.hvg_genes.csv
hvgs_filename = (
    local_data_path / f"asap-{dataset_team}.hvg_genes.csv"
)
hvg_df = pd.read_csv(hvgs_filename)
# %%
# just make the hvg which are NOT in target
hvg_df = dfs[~dfs["gene_name"].isin(target_genes)]
hvg_df = hvg_df.sort_values(by="-log10_padj", ascending=False)

# %%
ordered_gene_list = target_df.index.tolist() + hvg_df.index.tolist()


# construct table with genes as columns and samples as rows


# %%
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
dfs = pd.DataFrame()
DGE_results_dfs = pd.DataFrame()

# %%
for cell_type in cell_types:
    # Subset to cell type


    celltype_pseudobulk_filename = (
        local_data_path / f"asap-{dataset_team}.SN.06_{cell_type}_pseudobulk.csv"
    )


    df = pd.read_csv(celltype_pseudobulk_filename)
    
    # concatenate all cell_type df to dfs
    dfs = pd.concat([dfs, df], axis=1)



    disease_name = "PD"
    control_name = "Control"

    DGE_output_filename = (
        local_data_path / f"asap-{dataset_team}.SN.06_{cell_type}_DGE.csv"
    )

    DGE_results_df = pd.read_csv(DGE_output_filename)
    DGE_results_dfs = pd.concat([DGE_results_dfs, DGE_results_df], axis=0)


    volcano_plot_filename = (
        local_data_path / f"asap-{dataset_team}.SN.06_{cell_type}_volcano_plot.png"
    )


# reindex
dfs = dfs.set_index("Unnamed: 0")
DGE_results_dfs = DGE_results_dfs.set_index("Unnamed: 0")



#################################################
#################################################
#################################################
#################################################


# %%
###################
#     - differential expression analysis
#        - psuedobulk by MMC cell-types
#        - case/control differential expression
#        - heatmap of all 4k targets
#        - dot plot for "top" differentially expressed targets


# %%
# load the GP2 GWAS target genes for comparison of HVG
targets = pd.read_csv("./genes_by_locus.csv")
target_genes = targets["GENE"].tolist()


# %%
################################
#### sankey tools ##############
################################


# %%


def to_rgba(color, alpha=0.4):
    """Converts hex or rgb strings to rgba with transparency."""
    if color.startswith("#"):
        col = color.lstrip("#")
        rgb = tuple(int(col[i : i + 2], 16) for i in (0, 2, 4))
    elif color.startswith("rgb"):
        # Extract numbers from 'rgb(r, g, b)'
        rgb = tuple(map(int, color[4:-1].split(",")))
    else:
        return color  # Fallback for named colors
    return f"rgba({rgb[0]}, {rgb[1]}, {rgb[2]}, {alpha})"


def generate_multi_stage_sankey(df, cols, title="Category Assignment Flow"):
    sources, targets, values, link_colors = [], [], [], []

    # 1. Create unique node identifiers
    nodes = []
    for i, col in enumerate(cols):
        unique_vals = sorted(df[col].unique())
        for val in unique_vals:
            nodes.append({"id": f"{col}_{val}", "label": str(val)})

    id_map = {n["id"]: i for i, n in enumerate(nodes)}
    node_labels = [n["label"] for n in nodes]

    # 2. Setup Color Palette based on the first column
    # Using 'Bold' palette which often uses hex, but to_rgba handles variations
    palette = px.colors.qualitative.Bold
    first_col_name = cols[0]
    first_col_cats = sorted(df[first_col_name].unique())
    color_map = {cat: palette[i % len(palette)] for i, cat in enumerate(first_col_cats)}

    # 3. Build the links
    for i in range(len(cols) - 1):
        source_col = cols[i]
        target_col = cols[i + 1]

        # Deduplicate group columns to prevent ValueError
        group_cols = list(dict.fromkeys([source_col, target_col, first_col_name]))
        counts = df.groupby(group_cols).size().reset_index(name="count")

        for _, row in counts.iterrows():
            sources.append(id_map[f"{source_col}_{row[source_col]}"])
            targets.append(id_map[f"{target_col}_{row[target_col]}"])
            values.append(row["count"])

            # Use the helper to ensure color is rgba
            base_color = color_map[row[first_col_name]]
            link_colors.append(to_rgba(base_color, alpha=0.4))

    # 4. Create the Figure
    fig = go.Figure(
        data=[
            go.Sankey(
                node=dict(
                    pad=20,
                    thickness=20,
                    line=dict(color="black", width=0.5),
                    label=node_labels,
                    color="lightgray",
                ),
                link=dict(
                    source=sources, target=targets, value=values, color=link_colors
                ),
            )
        ]
    )

    fig.update_layout(title_text=title, font_size=12, height=600)
    return fig


# Usage:
# fig = generate_multi_stage_sankey(df, ["cell_typeA", "cell_typeB", "cell_typeC"])
# fig.show()

# --- Execution ---
# fig = generate_multi_stage_sankey(df, ["cell_typeA", "cell_typeB", "cell_typeC"])
# fig.show()

# %%
# read parquet files
df = pd.read_parquet(output_cell_types_file)
df2 = pd.read_parquet(output_cell_types_file_v2)
df3 = pd.read_parquet(output_cell_types_file_v3)

# %%
celltype_df = df.copy()
celltype_df["cell_typeC"] = df3["C_scANVI"]
celltype_df["cell_typeB"] = df2["C_scANVI"]
celltype_df["cell_typeA"] = df["C_scANVI"]


# %%
# df = adata.obs.copy()
# cols = ["cell_type", "cell_type_scanvi", "cell_type_scanvi_v2", "cell_type_scanvi_v3"]

cols = ["cell_typeA", "cell_typeB", "cell_typeC"]

fig = generate_multi_stage_sankey(celltype_df, cols)
# %%
fig.show()

# %%
ad3 = sc.read_h5ad(sn_scanvi_filename_v3)
ad2 = sc.read_h5ad(sn_scanvi_filename_v2)
ad1 = sc.read_h5ad(sn_scanvi_filename)
# %%

cols = ["cell_type", "C_scANVI", "condition_id"]
df = ad1.obs[cols].copy()
fig = generate_multi_stage_sankey(df, cols)
fig.show()

# %%
