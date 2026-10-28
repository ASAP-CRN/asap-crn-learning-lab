"""Shared paths and parameters for the sc-rnaseq-wf expository notebooks.

Paths mirror the Verily Workbench (VWB) workspace layout used in asap-crn-learning-lab
(`~/workspace/...`). Off VWB, set `ASAP_WS_ROOT` to a local directory with the same layout.

Parameters are the defaults of `workflows/main.wdl` (sc_rnaseq_analysis v5.0.0) unless noted, and file names
match the WDL task outputs, so each notebook's outputs can be compared with the curated release.
"""

import os
import shlex
import subprocess
from pathlib import Path

# --- VWB workspace ---------------------------------------------------------------------------
WS_ROOT = Path(os.environ.get("ASAP_WS_ROOT", Path.home() / "workspace"))
WS_FILES = WS_ROOT / "ws_files"
DATASETS_PATH = WS_ROOT / "01_PMDBS_scRNAseq"

# --- Dataset ---------------------------------------------------------------------------------
# dataset_id = {team-xxyy}-{source}-{modality_flavour}-{context}; curated bucket = asap-curated-{dataset_id}
WORKFLOW_NAME = "pmdbs_sc_rnaseq"
TEAM_ID = "team-jakobsson"
DATASET_NAME = "jakobsson-pmdbs-sn-rnaseq"
DATASET_ID = f"team-{DATASET_NAME}"
BUCKET_NAME = f"asap-curated-{DATASET_ID}"
# The per-project cohort analysis uses asap_team_id as its cohort_id (main.wdl)
COHORT_ID = TEAM_ID

DATASET_PATH = DATASETS_PATH / BUCKET_NAME / WORKFLOW_NAME
PREPROCESS_PATH = DATASET_PATH / "preprocess"
CURATED_COHORT_PATH = DATASET_PATH / "cohort_analysis"
METADATA_PATH = WS_ROOT / "release_resources" / DATASET_NAME / "metadata"

# --- Local working directories ---------------------------------------------------------------
RUN_DIR = WS_FILES / "sc_rnaseq_wf" / COHORT_ID
REFERENCES_PATH = WS_FILES / "references"

# --- Filtering (filter) ----------------------------------------------------------------------
PCT_COUNTS_MT_MAX = 10
DOUBLET_SCORE_MAX = 0.2
TOTAL_COUNTS_LIMITS = [500, 150000]
N_GENES_BY_COUNTS_LIMITS = [300, 15000]
N_MADS_LOWER = 3
N_MADS_UPPER = 5

# --- Allen Institute's MapMyCells (mmc) ------------------------------------------------------
# Must match the precomputed stats file; 'Siletti' = 10x whole human brain (WHB-10Xv3), 'SEAAD' = SEA-AD MTG
MMC_TAXONOMY = "Siletti"
MMC_PRECOMPUTED_STATS = {
    "Siletti": REFERENCES_PATH / "precomputed_stats.siletti.training.h5",
    "SEAAD": REFERENCES_PATH / "precomputed_stats.20231120.sea_ad.MTG.h5",
}
MMC_N_PROCESSORS = 16  # map_cell_types `threads` for on-the-fly mapping

# --- Normalization (process) -----------------------------------------------------------------
NORM_TARGET_SUM = 10000
N_TOP_GENES = 3000
N_COMPS = 30

# --- Sample integration (integrate_scvi, label_scanvi, add_harmony) --------------------------
SCVI_LATENT_KEY = "X_scVI"
SCANVI_LATENT_KEY = "X_scANVI"
SCANVI_PREDICTIONS_KEY = "C_scANVI"
BATCH_KEY = "batch_id"

# --- Clustering (clustering_umap) ------------------------------------------------------------
N_NEIGHBORS = 15
LEIDEN_RES = [0.2, 0.5, 1.0]

# --- Plotting (plot_groups_and_feats) --------------------------------------------------------
# main.wdl defaults plus C_scANVI; sc-tools resolves "leiden_res_1.0" to the "leiden_res_1.00" key clustering writes
GROUPS = ["sample", "batch_id", "cell_type", "C_scANVI", "leiden_res_0.20", "leiden_res_0.50", "leiden_res_1.0"]
FEATURES = ["n_genes_by_counts", "total_counts", "pct_counts_mt", "pct_counts_rb", "doublet_score", "S_score", "G2M_score"]


def out(suffix: str) -> Path:
    """Path of a cohort output in RUN_DIR, named as in the WDL (`${cohort_id}.<suffix>`)."""
    return RUN_DIR / f"{COHORT_ID}.{suffix}"


def curated(suffix: str) -> Path:
    """Path of the same output in the curated release, for comparison."""
    return CURATED_COHORT_PATH / f"{COHORT_ID}.{suffix}"


def run(*cmd) -> None:
    """Run an sc-tools command in RUN_DIR, streaming its output; raise if it fails.

    The scripts write plots to `plots/` relative to the working directory, as in the WDL tasks.
    """
    cmd = [str(c) for c in cmd]
    print("$", shlex.join(cmd), flush=True)
    RUN_DIR.mkdir(parents=True, exist_ok=True)
    with subprocess.Popen(
        cmd, cwd=RUN_DIR, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1
    ) as proc:
        for line in proc.stdout:
            print(line, end="", flush=True)
    if proc.returncode != 0:
        raise subprocess.CalledProcessError(proc.returncode, cmd)
