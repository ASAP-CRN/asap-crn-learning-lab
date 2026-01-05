from cell_type_mapper.cli.from_specified_markers import FromSpecifiedMarkersRunner
from pathlib import Path
import os
import scanpy as sc


os.environ["AIBS_BKP_USE_TORCH"] = "false"

os.environ["NUMEXPR_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"

# precomputed stats:
# SEA-AD (cortical)
# "https://allen-brain-cell-atlas.s3-us-west-2.amazonaws.com/mapmycells/SEAAD/20240831/precomputed_stats.20231120.sea_ad.MTG.h5"
# Whole brain (silette et al)
# https://allen-brain-cell-atlas.s3-us-west-2.amazonaws.com/mapmycells/HMBA-BG-taxonomy-CCN20250428/20250630/precomputed_stats.HMBA.BG.2025-08-04.h5

# set general folder paths
HOME = Path.home()
WS_ROOT = HOME / "workspace"
DATA_DIR = WS_ROOT / "data"
WS_FILES = WS_ROOT / "ws_files"


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


# paths to files where mapping output will be written
json_dst_path = str(mapmycells_output_dir / "human_sn_mapping.json")
csv_dst_path = str(mapmycells_output_dir / "human_sn_neruons_mapping.csv")


# %%
sn_full_raw_filename = local_data_path / f"asap-{dataset_team}.SN.01_full_raw.h5ad"


sn_mmc_filename = local_data_path / f"asap-{dataset_team}.SN.04_mmc.h5ad"


sn_mmc_pheno_filename = (
    local_data_path / f"asap-{dataset_team}.SN.04_mmc_processed.h5ad"
)


CHUNK_SIZE = 40000
N_RUNNERS_UP = 5
RNG_SEED = 11235813
N_PROCESSORS = 8
MAX_GB = 48.0


adata_mmc_filename = sn_mmc_filename


# %%
adata = sc.read_h5ad(sn_full_raw_filename)

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


args = [
    "--adata-input",
    str(adata_mmc_filename),
    "--mmc-precomputed-stats",
    str(precomputed_stats_filepath),
    "--mmc-marker-genes",
    str(query_markers_filepath),
    "--n-processors",
    n_processers,
    "--output-prefix",
    output_prefix,
]


import subprocess
import sys

# Arguments to pass to the script
args = ["arg1", "arg2", "arg3"]

# Command with arguments
command = [sys.executable, "./mmc.py"] + args

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


def main():

    config = {
        "query_path": str(adata_mmc_filename),
        "extended_result_path": json_dst_path,
        "csv_result_path": csv_dst_path,
        "verbose_csv": True,
        "query_markers": {"serialized_lookup": str(query_markers_filepath)},
        "precomputed_stats": {"path": str(precomputed_stats_filepath)},
        "type_assignment": {
            "n_processors": 4,
            "normalization": "raw",
            "bootstrap_factor": 0.5,
            "bootstrap_iteration": 100,
        },
    }

    runner = FromSpecifiedMarkersRunner(args=[], input_data=config)

    runner.run()


if __name__ == "__main__":
    main()
