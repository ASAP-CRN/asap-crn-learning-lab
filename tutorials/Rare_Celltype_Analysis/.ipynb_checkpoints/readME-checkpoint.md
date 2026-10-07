# Rare Cell Type Analysis: Region Subsetting, Integration, and Label Transfer

This tutorial shows how to pull one brain region out of the ASAP CRN PMDBS sc/snRNA-seq cohort, recover full-gene raw counts, integrate across datasets with scVI, and annotate a rare cell population using a reference taxonomy, scANVI, and marker-based validation.

The worked example uses **dopaminergic neurons in the Substantia Nigra (SN)**. Every region, label, and marker choice lives in a single configuration cell, so the same notebooks can be pointed at other rare populations, such as striatal interneurons in the caudate or putamen.

> **Looking for the biological application?** See the case study [`case_studies/SN_CellType_Annotation/`](https://github.com/ASAP-CRN/asap-crn-learning-lab/tree/main/case_studies/SN_CellType_Annotation), which uses MapMyCells to annotate SN cell types end to end. This tutorial focuses on the reusable method.


## Learning goals

By completing this tutorial, users will learn how to:

- Select samples for one brain region from CRN metadata
- Combine curated, QC-filtered cells (`.final.h5ad`) with full-gene raw counts (`.merged_cleaned_unfiltered.h5ad`)
- Audit cohort composition (datasets, samples, conditions) before batch correction
- Choose features that keep a rare population resolvable
- Integrate datasets with scVI and refine labels with scANVI
- Validate annotations of a rare population using orthogonal marker genes


## Notebooks

Two notebooks, one per Verily Workbench app type. Everything that runs on CPU and happens before model training is in Notebook 01; everything that needs a GPU, plus the short evaluation and export, is in Notebook 02. You switch apps once.

| Notebook | App | Description |
|----------|-----|-------------|
| [`01_cpu_subset_and_annotate.ipynb`](01_cpu_subset_and_annotate.ipynb) | CPU (high memory) | Select region samples, recover full-gene raw counts, audit cohort composition, normalize and select features, annotate with MapMyCells, validate target-population labels with marker genes |
| [`02_gpu_integrate_and_export.ipynb`](02_gpu_integrate_and_export.ipynb) | GPU (T4) | Integrate with scVI, refine labels with scANVI (seeded by Notebook 01 labels), compare representations and label agreement, export the final dataset |

## Adapting this tutorial to another rare population

Edit the configuration cell near the top of Notebook 01 (and the matching variables at the top of Notebook 02):

```python
ANALYSIS_NAME        = "sn_dopaminergic"    # folder, file, and bucket names
TARGET_REGION_SUBSTR = "substantia nigra"   # matched against all region-name columns
TARGET_ONTOLOGY_IDS  = {"UBERON:0002038", "UBERON:0001965"}
TARGET_LABEL         = "Dopaminergic"       # simplified MapMyCells cell_type
MARKER_GENES         = ["TH", "SLC6A3", "SLC18A2", "DDC", "NR4A2", "KCNJ6", "SNCA", "ALDH1A1", "GCH1"]
BATCH_KEY            = "ASAP_dataset_id"
REFERENCE            = {...}                # taxonomy URLs, class mapper, confidence thresholds
```

Example configurations:

| Target population | `TARGET_REGION` | Example `MARKER_GENES` | Reference |
|-------------------|-----------------|------------------------|-----------|
| Dopaminergic neurons (worked example) | Substantia nigra | `TH`, `SLC6A3`, `SLC18A2`, `DDC` | [HMBA Basal Ganglia taxonomy](https://alleninstitute.github.io/abc_atlas_access/descriptions/HMBA-BG_dataset.html) |

Things to check when switching populations:

- **Region names differ between metadata levels.** Inspect `region_level_1_name`, `region_level_2_name`, and `region_level_3_name` before choosing `REGION_COL`.
- **Reference taxonomy must match the region.** The basal ganglia taxonomy fits SN and striatum. Cortical regions need a cortical reference.
- **Check where the target cells come from** The composition audit in Notebook 01 shows target cells per dataset and per sample. If one dataset contributes nearly all of them (as in the worked example), read the limitations below.


## Environment

```bash
conda env create -f environment.yml
conda activate rare_celltype
python -m ipykernel install --user --name=rare_celltype --display-name "Python (rare_celltype)"
```

The environment pins a PyTorch build for **CUDA 12.8**, which is compatible with the NVIDIA driver on Verily Workbench GPU apps (CUDA 12.9). A newer CUDA build fails with `The NVIDIA driver on your system is too old`.

GCS files are accessed with `google-cloud-storage` rather than `gcsfs`, which has dependency conflicts in Workbench.


## Suggested compute environments (Verily Workbench)

**CPU app — Notebook 01**

| Resource     | Value         |
| ------------ | ------------- |
| Machine type | n1-highmem-16 |
| CPUs         | 16            |
| Memory       | 104 GB        |
| GPU          | None          |
| Disk         | 500 GB        |
| Autostop     | 1 hour        |

Notebook 01 loads full `.merged_cleaned_unfiltered.h5ad` files into memory one at a time, so a high-memory machine is recommended.

**GPU app — Notebook 02**

| Resource     | Value         |
| ------------ | ------------- |
| Machine type | n1-highmem-8  |
| CPUs         | 8             |
| Memory       | 52 GB         |
| GPU          | NVIDIA Tesla T4 |
| Disk         | 200 GB        |
| Autostop     | 1 hour        |

By Notebook 02 the data is reduced to one region, so the GPU app needs less memory. A T4 (16 GB) is enough for typical scVI / scANVI models; move to a V100 only if training runs out of GPU memory.

Use the same `environment.yml` in both apps. The CUDA 12.8 PyTorch build also runs on CPU-only machines.

## Where the tutorial stops
 
The tutorial ends at an **analysis-ready object**: curated cells, full-gene counts, harmonized metadata, an integrated embedding, validated labels, and the QC and composition tables needed to judge them. It deliberately does **not** run disease comparisons (differential expression, proportion tests). Those depend on the research question, and the right design depends on the caveats below.

All files are written to `ws_files/{ANALYSIS_NAME}/`.
 
| File | Notebook | Contents |
|------|----------|----------|
| `{ANALYSIS_NAME}__samples.csv` | 01 | Selected samples with harmonized SAMPLE / SUBJECT / CLINPATH metadata |
| `{ANALYSIS_NAME}__01_annotated.h5ad` | 01 | Hand-off object for Notebook 02 |
| `{ANALYSIS_NAME}__01_target_concordance.csv` | 01 | Target cells and marker scores per dataset and condition |
| `{ANALYSIS_NAME}__02_final.h5ad` | 02 | **Final analysis-ready object** (contents below) |
| `{ANALYSIS_NAME}__02_label_agreement.csv` | 02 | MapMyCells vs. scANVI label crosstab |
| `{ANALYSIS_NAME}__02_per_sample_summary.csv` | 02 | Cells, target cells, and target fraction per sample |
| `{ANALYSIS_NAME}__02_integration_benchmark.csv` | 02 | scib-metrics and target-neighborhood results per embedding |
| `{ANALYSIS_NAME}__scvi_model/`, `__scanvi_model/` | 02 | Trained models, reloadable without retraining |


**Final object contents**
 
| Slot | Key | Description |
|------|-----|-------------|
| `layers` | `counts` | Raw integer counts, all genes. Use for scVI, pseudobulk, and DE |
| `X` | | Log-normalized counts (target sum 1e4) |
| `var` | `highly_variable`, `gene_id` | HVGs with `MARKER_GENES` forced in; Ensembl IDs |
| `obs` | `ASAP_dataset_id`, `sample_id`, `ASAP_subject_id`, `condition_id`, `sex`, clinical fields | Harmonized metadata |
| `obs` | `mmc_*`, `cell_type` | MapMyCells labels and confidence (`mmc_rho`, `mmc_prob`); low-confidence cells are `Unknown` |
| `obs` | `marker_score`, `is_target`, `marker_discordant`, `seed_label` | Marker validation and the seed labels given to scANVI |
| `obs` | `cell_type_refined` | scANVI labels |
| `obsm` | `X_scVI` | **Primary integrated embedding** (label-free) |
| `obsm` | `X_scANVI`, `X_pca_harmony`, `X_umap_pca` | scANVI latent, Harmony baseline, unintegrated UMAP |
| `uns` | `scvi_provenance` | Seed, package versions, GPU, and model settings |
 
`X_scVI` is the recommended embedding for downstream work because it is not trained on our labels. `X_scANVI` is kept for comparison, but it was trained on labels derived from MapMyCells, so it will look slightly better on any metric that uses those same labels.

## Known limitations of the worked example
 
Read these before using the SN object for disease comparisons.
 
- **DA neurons come almost entirely from one dataset.** DS_PMDBS_0006 contributes 97% of DA cells (15,930), DS_PMDBS_0001 3% (515), and DS_PMDBS_0004 25 cells. DA-level results are effectively DS_PMDBS_0006 results and cannot be read as cross-cohort replication. DS_PMDBS_0004 has too few DA cells for DA-level analysis.
- **DA fraction varies widely between samples.** Within DS_PMDBS_0006, the per-sample DA fraction ranges from 0.1% to 62%. This points to differences in enrichment or dissection between libraries, so **DA proportion is not a valid readout of DA loss** until the source of that variation is identified. Do not compare raw DA cell counts between PD and control.
- **Cross-dataset alignment of DA cells is partial.** Treat DA comparisons across datasets with caution; analyze within dataset, or include dataset as a covariate.
- **Seed labels and evaluation labels overlap.** scANVI was trained on MapMyCells-derived labels, which inflates its scores on MapMyCells-based metrics.

## Recommended downstream analyses
 
Analyses that hold up given the limitations above:
 
- **Pseudobulk differential expression within DA neurons**: sum `layers["counts"]` per sample, compare PD vs. control at the sample level (e.g. DESeq2 or edgeR), within DS_PMDBS_0006 or with dataset as a covariate.
- **DA subtype composition**: subcluster DA cells (ideally a DA-only scVI, re-selecting HVGs on DA cells) and compare subtype proportions *among DA cells* per sample. This does not depend on how many DA nuclei a library captured.
- **Glial or other cell-state analyses** across all three datasets, where cell counts are more balanced.
Avoid: cell-level statistical tests that treat cells as independent replicates, and PD vs. control comparisons of total DA proportion.

## Reproducibility
 
- All random steps are seeded with `RANDOM_SEED = 42`, including `scvi.settings.seed` before each model is created.
- Trained scVI and scANVI models are saved, so the embedding can be reloaded rather than retrained.
- GPU training is not bit-identical across GPU types or cuDNN versions. Expect small numerical differences on hardware other than a T4.
- Package versions, CUDA version, and GPU name are stored in `uns["scvi_provenance"]`.


## Data and provenance

- CRN pipeline repository: https://github.com/ASAP-CRN/sc-rnaseq-wf
- CRN pipeline guide: https://asap-crn.github.io/asap-crn-learning-lab/pipeline/
- Validated against **CRN release v5.0.0** on **2026-10-05**. The notebooks select the latest available release automatically, so results may differ slightly for newer releases.

Users must have approved access to the relevant ASAP CRN data collections. See the [Getting Started guide](https://asap-crn.github.io/asap-crn-learning-lab/).