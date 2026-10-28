# Cohort Analysis: the sc-rnaseq-wf, Step by Step

These notebooks re-run the cohort analysis of the [sc-rnaseq-wf](https://github.com/ASAP-CRN/sc-rnaseq-wf) PMDBS workflow one step at a time, for one team's dataset: `team-jakobsson` (`jakobsson-pmdbs-sn-rnaseq`). Each notebook explains what the step does, runs the workflow's script through its [sc-tools](https://github.com/ASAP-CRN/sc-tools) command (`sc-<script>`) with the workflow's default parameters, and compares the outputs with the curated release.

The series starts from the per-sample `*.cleaned_unfiltered.h5ad` files in the curated bucket's `preprocess/` folder (CellBender-cleaned counts with QC metrics and doublet scores). Cell Ranger and CellBender are not re-run. The optional reference spike-in (`prep_da_spike_in`) and downsampling are skipped; all cells are kept.

---

## Notebooks

Run them in order; each one reads the previous one's outputs.

| Notebook | Step | sc-tools command | WDL task |
| :- | :- | :- | :- |
| `00_setup` | Workspace paths, sc-tools install, MapMyCells reference | - | - |
| `01_prep_metadata` | Per-sample QC metrics and doublet scores (inspection; re-running is optional) | `sc-prep-metadata` | `preprocess.counts_to_adata` |
| `02_merge_and_plot_qc` | Merge samples, QC violin plots | `sc-merge-and-plot-qc` | `merge_and_plot_qc_metrics` |
| `03_filter` | QC filtering | `sc-filter` | `filter` |
| `04_mmc` | MapMyCells cell type mapping | `sc-mmc` | `map_cell_types` |
| `05_process` | Normalize, cell cycle, HVGs, PCA | `sc-process` | `normalize` |
| `06_transcriptional_phenotype` | Confident MapMyCells labels | `sc-transcriptional-phenotype` | `add_mapped_cell_types` |
| `07_integrate_scvi` | scVI integration | `sc-integrate-scvi` | `cluster_data.integrate_sample_data` |
| `08_clustering_umap` | Neighbors, Leiden clusters, UMAP | `sc-clustering-umap` | `cluster_data.cluster_cells` |
| `09_annotate` | scANVI labels, Harmony, scib metrics | `sc-annotate` | `assign_remaining_cells` + `integrate_harmony` + `artifact_metrics` |
| `10_artifact_metrics` | Reading the scib report (re-running is optional) | `sc-artifact-metrics` | `artifact_metrics` |
| `11_plot_groups_and_feats` | UMAP plots of groups and features | `sc-plot-groups-and-feats` | `plot_groups_and_features` |

All paths and parameters are set in [`wf_config.py`](wf_config.py).

---

## Prerequisites

- **Environment:** create it from `environment.yml`, then register the kernel:

  ```bash
  conda env create -f environment.yml
  conda activate cohort_analysis
  python -m ipykernel install --user --name=cohort_analysis --display-name "Python (cohort_analysis)"
  ```

- **Compute:** notebooks 07–09 need a GPU (scVI/scANVI, and `rapids-singlecell` for clustering, UMAP and Harmony). Notebook 04 (MapMyCells) runs on CPU and needs a lot of memory.
- **Data:** the workspace resources mounted under `~/workspace`. Off Verily Workbench, set `ASAP_WS_ROOT` to a directory with the same layout.
- **Reference:** the MapMyCells precomputed stats file, downloaded in `00_setup` (several GB).

## Differences from the workflow

sc-tools runs the workflow's scripts unchanged (`sc_tools.__upstream_commit__` records the sc-rnaseq-wf commit). The series differs from a workflow run in a few places:

- `sc-annotate` (sc-tools only) combines scANVI labeling, Harmony and the scib metrics in one step, and re-attaches the MapMyCells labels first, so another reference can be swapped in without retraining scVI.
- Clustering and UMAP run before `sc-annotate` rather than after scANVI; they use only the scVI latent space, so the result is the same.
- The plotting step warns about missing groups and matches the workflow's default `leiden_res_1.0` to the `leiden_res_1.00` column (the workflow skips it).
- No reference spike-in and no downsampling.
