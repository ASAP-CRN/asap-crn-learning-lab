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
######
##### v _


# output file neame
sn_mmc_pheno_filename = (
    local_data_path / f"asap-{dataset_team}.SN.04_mmc_processed.h5ad"
)
sn_scanvi_filename = local_data_path / f"asap-{dataset_team}.SN.05_scanvi.h5ad"

output_cell_types_file = (
    local_data_path / f"asap-{dataset_team}.SN.05_scanvi_cell_types.parquet"
)

######
##### v2
sn_mmc_pheno_filename_v2 = (
    local_data_path / f"asap-{dataset_team}.SN.04_mmc_processed_v2.h5ad"
)
sn_scanvi_filename_v2 = local_data_path / f"asap-{dataset_team}.SN.05_scanvi_v2.h5ad"

output_cell_types_file_v2 = (
    local_data_path / f"asap-{dataset_team}.SN.05_scanvi_cell_types_v2.parquet"
)

######
##### v3
sn_mmc_pheno_filename_v3 = (
    local_data_path / f"asap-{dataset_team}.SN.04_mmc_processed_v3.h5ad"
)
sn_scanvi_filename_v3 = local_data_path / f"asap-{dataset_team}.SN.05_scanvi_v3.h5ad"

output_cell_types_file_v3 = (
    local_data_path / f"asap-{dataset_team}.SN.05_scanvi_cell_types_v3.parquet"
)
######

sn_decoupler_output_filename = (
    local_data_path / f"asap-{dataset_team}.SN.06_decoupler_output.h5ad"
)
# Save the cell barcode, cluster, cell-type, and batch values to a .csv

decoupler_output_filename = (
    local_data_path / f"asap-{dataset_team}.SN.06_decoupler_output.csv"
)


# %%
adata = sc.read_h5ad(sn_integrated_filename)


# %%
################################
#### sankey tools ##############
################################

import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


def create_sankey(df, cols):
    # 2. Create unique labels and a color map based on the first column
    # This ensures that the flow color is tied to the original classification
    unique_labels = []
    df_labeled = df[cols].copy()
    for col in cols:
        df_labeled[col] = df_labeled[col] + f"_{col}"
        for label in df_labeled[col].unique():
            if label not in unique_labels:
                unique_labels.append(label)

    label_map = {label: i for i, label in enumerate(unique_labels)}

    # Generate a color palette for the unique labels
    palette = px.colors.qualitative.Safe
    color_map = {
        label: palette[i % len(palette)] for i, label in enumerate(df[cols[0]].unique())
    }

    # 3. Build the links
    sources, targets, values, link_colors = [], [], [], []

    for i in range(len(cols) - 1):
        counts = (
            df_labeled.groupby([cols[i], cols[i + 1], cols[0]])
            .size()
            .reset_index(name="count")
        )

        for _, row in counts.iterrows():
            sources.append(label_map[row[cols[i]]])
            targets.append(label_map[row[cols[i + 1]]])
            values.append(row["count"])
            # Assign color based on the origin (Column A)
            # We use 'rgba' to add transparency (0.4) so overlapping flows are visible
            hex_col = color_map[row[cols[0]]]
            rgb_col = hex_col.lstrip("#")
            r, g, b = tuple(int(rgb_col[i : i + 2], 16) for i in (0, 2, 4))
            link_colors.append(f"rgba({r}, {g}, {b}, 0.4)")

    # 4. Create the Figure
    fig = go.Figure(
        data=[
            go.Sankey(
                node=dict(
                    pad=15,
                    thickness=20,
                    label=unique_labels,
                    color="gray",  # Nodes remain neutral
                ),
                link=dict(
                    source=sources,
                    target=targets,
                    value=values,
                    color=link_colors,  # Links are color-coded by origin
                ),
            )
        ]
    )

    fig.update_layout(title_text="Cell Type Flow Tracking", font_size=12)
    return fig


df = adata.obs.copy()
cols = ["cell_type", "cell_type_scanvi", "cell_type_scanvi_v2", "cell_type_scanvi_v3"]
fig.show()
