# %%

import pandas as pd
import numpy as np
import scanpy as sc
import seaborn as sns
import matplotlib.pyplot as plt
import sys, subprocess, importlib, warnings, math, os

from pathlib import Path

import subprocess
import sys

# %%
##
# pip3 install -U scvi-tools[cuda]  # gets jax and jaxlib, updates cuda
# pip3 install -U scib-metrics
#
#
# %%
###########
# ## STEP 0. Workspace Setup

# set general folder paths
HOME = Path.home()
WS_ROOT = HOME / "workspace"
DATA_DIR = WS_ROOT / "data"
WS_FILES = WS_ROOT / "ws_files"

# if not WS_ROOT.exists():
#     print(f"{WS_ROOT} doesn't exist. We need to remount our resources")
#     !wb resource mount

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
adata_mmc = sc.read_h5ad(sn_full_raw_filename)

# Preserve gene_name as a column
adata_mmc.var["gene_name"] = adata_mmc.var.index

# 2. Set var_names to gene_id (ENSG IDs)
adata_mmc.var_names = adata_mmc.var["gene_id"].astype(str)

# 3. Ensure uniqueness
adata_mmc.var_names_make_unique()
sn_mmc_filename = local_data_path / f"asap-{dataset_team}.SN.04_mmc.h5ad"
adata_mmc.write_h5ad(sn_mmc_filename)

# %%
#######################################################

# Set paths
precomputed_stats_filepath = (
    mapmycells_input_dir / "Human.precomputed_stats.20250507.h5"
)
query_markers_filepath = mapmycells_input_dir / "Human.query_markers.20250507.json"

# paths to files where mapping output will be written
json_dst_path = str(mapmycells_output_dir / "SN.04_mmc.human_sn_mapping.json")
csv_dst_path = str(mapmycells_output_dir / "SN.04_mmc.human_sn_neruons_mapping.csv")


output_prefix = "SN.04_mmc.human_sn"
arg_mmc_markers = str(query_markers_filepath)

n_processers = "8"

args = [
    "--adata-input",
    str(sn_mmc_filename),
    "--mmc-precomputed-stats",
    str(precomputed_stats_filepath),
    "--mmc-marker-genes",
    str(query_markers_filepath),
    "--n-processors",
    n_processers,
    "--output-prefix",
    output_prefix,
]


# run human_bg_mmc.py
# Command with arguments
command = [sys.executable, "./mmc.py"] + args
# %%

try:
    result = subprocess.run(
        command,
        capture_output=True,  # Capture stdout and stderr
        text=True,  # Decode output as text (Python 3.5+)
        check=True,  # Raise an exception if the script returns a non-zero exit status
        timeout=60,  # Set a timeout for the command to finish (optional)
    )
    print("Script output:", result.stdout)
    # print("Script errors (if any):", result.stderr) # stderr is captured if check=True raises CalledProcessError

except subprocess.CalledProcessError as e:
    print(f"Script failed with return code {e.returncode}")
    print("Error output:", e.stderr)
except subprocess.TimeoutExpired:
    print("Script timed out")

#######################################################
# %%


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


# %%

results = read_csv_results(csv_dst_path)
results.head()

# get the "Class_name" for each Neighborhood_name
output = results.groupby("Neighborhood_name")["Class_name"].unique()

# %%


def class_assign(x):
    if x in ["ExN", "InN", "DA"]:
        return "neuron"
    elif x in ["Oligo", "VC", "OPC", "Astro", "MG"]:
        return "non-neuronal"


neighborhood_names = [
    "Nonneuron",
    "Glut Sero Dopa",
    "Subpallium GABA",
    "Subpallium GABA-Glut",
]

class_names = [
    "OPC-Oligo",
    "Astro-Epen",
    "Vascular",
    "Immune",
    "F M Glut",
    "CN CGE GABA",
    "M Dopa",
    "F M GABA",
    "CN MGE GABA",
    "CN LGE GABA",
    "Cx GABA",
    "CN GABA-Glut",
]


CARD_classes = [
    "Astro",
    "DaN",
    "EC",
    "ExN",
    "EpC",
    "FB",
    "InN",
    "MG",
    "OPC",
    "Oligo",
    "PC",
    "TC",
]


subc_mapping = {
    "Oligo": "oligo",
    "OPC": "opc",
    "ExN": "glutamatergic",
    "InN": "gabaergic",
    "Astro": "astrocyte",
    "MG": "immune",
    "VC": "blood_vessel",
    "DA": "Dopaminergic",
    "EC": "Endothelial",
    "EpC": "Epithelial",
    "PC": "Pericyte",
    "TC": "T-cells",
}

tmp = results.groupby("Neighborhood_name")["Class_name"].unique()

our_names = [
    "Dopaminergic",
    "Glutamatergic",
    "GABAergic",
    "OPC-Oligo",
    "Astrocyte",
    "Immune",
    "Vascular",
]

# map Class_name directly to our_names

class_mapper = {
    "OPC-Oligo": "OPC-Oligo",
    "Astro-Epen": "Astrocyte",
    "Vascular": "Vascular",
    "Immune": "Immune",
    "F M Glut": "Glutamatergic",
    "M Dopa": "Dopaminergic",
    "CN CGE GABA": "GABAergic",
    "F M GABA": "GABAergic",
    "CN MGE GABA": "GABAergic",
    "CN LGE GABA": "GABAergic",
    "Cx GABA": "GABAergic",
    "CN GABA-Glut": "GABAergic",
}

# Oligo,OPC,ExN,InN,Astro,MG,VC
# DaN,EC,EpC,FB,PC,TC


# %%
def summarize_mmc_results(mmc_results: pd.DataFrame, workflow_name: str):
    # First get "classes"
    # Define row indices for each class
    # HUMAN
    if workflow_name == "pmdbs_sc_rnaseq":
        gabaergic = mmc_results["class_name"] == "Neuronal: GABAergic"
        glutamatergic = mmc_results["class_name"] == "Neuronal: Glutamatergic"
        non_neuronal = mmc_results["class_name"] == "Non-neuronal and Non-neural"

        mmc_results.loc[gabaergic, "phenotype"] = "GABAergic"
        mmc_results.loc[glutamatergic, "phenotype"] = "Glutamatergic"
        mmc_results.loc[non_neuronal, "phenotype"] = mmc_results.loc[
            non_neuronal, "subclass_name"
        ]

        mmc_results.loc[glutamatergic, "rho"] = mmc_results.loc[
            glutamatergic, "class_correlation_coefficient"
        ]
        mmc_results.loc[gabaergic, "rho"] = mmc_results.loc[
            gabaergic, "class_correlation_coefficient"
        ]
        mmc_results.loc[non_neuronal, "rho"] = mmc_results.loc[
            non_neuronal, "subclass_correlation_coefficient"
        ]

        mmc_results.loc[glutamatergic, "prob"] = mmc_results.loc[
            glutamatergic, "class_bootstrapping_probability"
        ]
        mmc_results.loc[gabaergic, "prob"] = mmc_results.loc[
            gabaergic, "class_bootstrapping_probability"
        ]
        mmc_results.loc[non_neuronal, "prob"] = mmc_results.loc[
            non_neuronal, "subclass_bootstrapping_probability"
        ]

        mmc_results["cell_type"] = mmc_results["phenotype"]

        # Change the phenotype to unknown if the correlation or bootstrap probability < 0.5
        mmc_results.loc[mmc_results["rho"] < 0.5, "cell_type"] = "Unknown"
        mmc_results.loc[mmc_results["prob"] < 0.5, "cell_type"] = "Unknown"

        return mmc_results[
            [
                "cell_type",
                "phenotype",
                "rho",
                "prob",
                "class_name",
                "subclass_name",
                "supertype_name",
            ]
        ]
    elif workflow_name == "mouse_sc_rnaseq":
        # MOUSE
        gabaergic = mmc_results["class_name"].str.contains("GABA")
        glutamatergic = mmc_results["class_name"].str.contains("Glut")
        serotonergic = mmc_results["class_name"].str.contains("Sero")
        # This includes OPC-Oligo, Astro-Epen, Vascular, Immune, and OEC (olfactory ensheathing cells - glial)
        non_neuronal = ~(gabaergic | glutamatergic | serotonergic)

        mmc_results.loc[gabaergic, "phenotype"] = "GABAergic"
        mmc_results.loc[glutamatergic, "phenotype"] = "Glutamatergic"
        mmc_results.loc[serotonergic, "phenotype"] = "Serotonergic"
        mmc_results.loc[non_neuronal, "phenotype"] = mmc_results.loc[
            non_neuronal, "subclass_name"
        ]

        mmc_results.loc[glutamatergic, "rho"] = mmc_results.loc[
            glutamatergic, "class_correlation_coefficient"
        ]
        mmc_results.loc[gabaergic, "rho"] = mmc_results.loc[
            gabaergic, "class_correlation_coefficient"
        ]
        mmc_results.loc[serotonergic, "rho"] = mmc_results.loc[
            serotonergic, "class_correlation_coefficient"
        ]
        mmc_results.loc[non_neuronal, "rho"] = mmc_results.loc[
            non_neuronal, "subclass_correlation_coefficient"
        ]

        mmc_results.loc[glutamatergic, "prob"] = mmc_results.loc[
            glutamatergic, "class_bootstrapping_probability"
        ]
        mmc_results.loc[gabaergic, "prob"] = mmc_results.loc[
            gabaergic, "class_bootstrapping_probability"
        ]
        mmc_results.loc[serotonergic, "prob"] = mmc_results.loc[
            serotonergic, "class_bootstrapping_probability"
        ]
        mmc_results.loc[non_neuronal, "prob"] = mmc_results.loc[
            non_neuronal, "subclass_bootstrapping_probability"
        ]

        mmc_results["cell_type"] = mmc_results["phenotype"]

        # Change the phenotype to unknown if the correlation or bootstrap probability < 0.5
        mmc_results.loc[mmc_results["rho"] < 0.5, "cell_type"] = "Unknown"
        mmc_results.loc[mmc_results["prob"] < 0.5, "cell_type"] = "Unknown"

        # Include cluster info but did not filter like above
        return mmc_results[
            [
                "cell_type",
                "phenotype",
                "rho",
                "prob",
                "class_name",
                "subclass_name",
                "supertype_name",
                "cluster_name",
                "cluster_correlation_coefficient",
                "cluster_bootstrapping_probability",
            ]
        ]

    elif workflow_name == "basal_ganglia":
        class_mapper = {
            "OPC-Oligo": "OPC-Oligo",
            "Astro-Epen": "Astrocyte",
            "Vascular": "Vascular",
            "Immune": "Immune",
            "F M Glut": "Glutamatergic",
            "M Dopa": "Dopaminergic",
            "CN CGE GABA": "GABAergic",
            "F M GABA": "GABAergic",
            "CN MGE GABA": "GABAergic",
            "CN LGE GABA": "GABAergic",
            "Cx GABA": "GABAergic",
            "CN GABA-Glut": "GABAergic",
        }
        #   ['Nonneuron', 'Glut Sero Dopa', 'Subpallium GABA', 'Subpallium GABA-Glut']

        # map Class_name to to phenotype
        mmc_results["phenotype"] = mmc_results["Class_name"].map(class_mapper)

        # fixup GABAergic rho and prob to be the Neighborhood_correlation_coefficient
        # and Neighborhood_bootstrapping_probability

        gabaergic = mmc_results["Class_name"] == "GABAergic"
        mmc_results["rho"] = mmc_results["Class_correlation_coefficient"]

        mmc_results.loc[gabaergic, "rho"] = mmc_results.loc[
            gabaergic, "Neighborhood_correlation_coefficient"
        ]

        mmc_results["prob"] = mmc_results["Class_bootstrapping_probability"]
        mmc_results.loc[gabaergic, "prob"] = mmc_results.loc[
            gabaergic, "Neighborhood_bootstrapping_probability"
        ]

        mmc_results["cell_type"] = mmc_results["phenotype"]

        # Change the phenotype to unknown if the correlation or bootstrap probability < 0.5
        mmc_results.loc[mmc_results["rho"] < 0.5, "cell_type"] = "Unknown"
        mmc_results.loc[mmc_results["prob"] < 0.5, "cell_type"] = "Unknown"

        # rename class_name, sublcass_name, to be lowercase.abs
        #
        # rename Neighborhood_name, and supertype_name
        name_mapper = {
            "Neighborhood_name": "supertype_name",
            "Class_name": "class_name",
            "Subclass_name": "subclass_name",
        }
        mmc_results.rename(columns=name_mapper, inplace=True)

        return mmc_results[
            [
                "cell_type",
                "phenotype",
                "rho",
                "prob",
                "class_name",
                "subclass_name",
                "supertype_name",
            ]
        ]

    else:
        raise ValueError(
            f"[ERROR] Source cannot be detected from workflow name: [{workflow_name}]"
        )


# %%
adata = sc.read_h5ad(sn_integrated_filename)


results = read_csv_results(csv_dst_path)
results = summarize_mmc_results(results, "basal_ganglia")
# Save the results to parquet file.. or feather?


# output file neame
sn_mmc_pheno_parquet_filename = (
    local_data_path / f"asap-{dataset_team}.SN.04_mmpc_phenotype.parquet"
)

results.to_parquet(sn_mmc_pheno_parquet_filename, compression="gzip")


adata.obs = adata.obs.merge(results, left_index=True, right_index=True)


# Save the adata
adata.write_h5ad(filename=sn_mmc_pheno_filename, compression="gzip")


# %%
