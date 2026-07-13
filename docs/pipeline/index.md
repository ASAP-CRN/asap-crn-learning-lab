# scRNA-seq Pipeline Guide

**Pipeline release:** `v4.0.0` — [view on GitHub](https://github.com/ASAP-CRN/sc-rnaseq-wf/releases/tag/sc_rnaseq_analysis-v4.0.0)

**Applicable CRN release:** `v5.0.0`

!!! note
    This page will be revised for future CRN releases as needed

## Overview

The ASAP CRN sc/snRNA-seq pipeline provides a harmonized, reproducible processing workflow for single-cell and single-nucleus RNA-seq datasets contributed by ASAP CRN teams. 

The pipeline supports both:

- Human PMDBS sc/snRNA-seq data
- Mouse single-cell/single-nucleus RNA-seq data

For full workflow implementation details, see the [ASAP-CRN pmdbs-sc-rnaseq-wf repository](https://github.com/ASAP-CRN/pmdbs-sc-rnaseq-wf).

!!! warning "Important disclaimer"
    Pipeline outputs are curated, standardized processing outputs — they are **not intended to be finished science**. Treat them as a harmonized starting point for research, not a substitute for study-specific analysis decisions. Review the pipeline's assumptions, QC thresholds, cell type annotations, covariates, and cohort structure before using outputs for biological interpretation, publication-ready analysis, or hypothesis testing.

    The pipeline is designed to make processing choices explicit and consistent across datasets — more nuanced biological decisions should be made by researchers based on their specific scientific question.

## Pipeline structure

This guide follows the pipeline itself: preprocessing, then cohort analysis, then the resulting outputs and how to use them. The workflow has two major stages:

1. **Preprocessing** — run once per sample
2. **Cohort analysis** — run on a set of samples

## Preprocessing

Preprocessing is run once per sample, preparing individual sample-level data before samples are combined into a cohort-level analysis. Typical steps include:

- Alignment and initial count generation
- Technical artifact removal
- Conversion into AnnData format
- QC metric calculation
- Doublet score calculation
- Sample, dataset, team, and batch metadata assignment

Preprocessing outputs are generally sample-level files, including both raw/intermediate objects and files copied into staging as final workflow outputs.

### CellRanger and count generation

The pipeline uses CellRanger reference data for read alignment and count generation — the specific transcriptome reference matches the organism and genome build used for the dataset. This is the first stage of the [preprocessing workflow](https://github.com/ASAP-CRN/harmonized-wf-dev/blob/main/workflows/preprocess/preprocess.wdl), run once per sample directly on the raw FASTQ files.

**CellRanger v7.0.1** is currently used with:

- Human GRCh38 (GENCODE v32/Ensembl98 annotations), or
- Mouse GRCm39 (GENCODE vM33/Ensembl110 annotations)

### CellBender

CellBender removes technical artifacts from the count matrix, including count correction for ambient RNA molecules and random barcode swapping. See the [CellBender documentation](https://cellbender.readthedocs.io/en/latest/introduction/index.html) for details. The workflow preserves CellBender outputs and reports so users can inspect sample-level behavior.

### QC metrics and doublet scores

Standard single-cell QC metrics calculated:

- Total counts per cell
- Number of genes detected per cell
- Percent mitochondrial counts
- Percent ribosomal counts

Doublet scores are calculated with [Scrublet](https://scanpy.readthedocs.io/en/stable/api/generated/scanpy.pp.scrublet.html) through Scanpy. The pipeline keeps the continuous `doublet_score` value and drops the binary `predicted_doublet` field, so filtering is based on the score threshold rather than a pre-assigned binary label.

### Metadata added during preprocessing

| Field | Meaning |
|---|---|
| `sample` | Sample identifier |
| `batch` | Batch value provided in the sample metadata |
| `team` | ASAP team identifier |
| `dataset` | Dataset identifier |

## Cohort analysis

Cohort analysis is run on a set of samples, either at the project/team level or across the full cohort. It can be rerun with different sample subsets, but adding or removing samples requires re-running the whole cohort analysis. Intermediate files from previous runs are not reused. In the underlying workflow, this entire process is referred to as the "cohort analysis," with the key integration logic implemented in the [clustering workflow](https://github.com/ASAP-CRN/harmonized-wf-dev/blob/main/workflows/cohort_analysis/cluster_data/cluster_data.wdl).

Cohort analysis includes:

- Merging sample AnnData objects
- Plotting initial QC metrics
- Filtering cells
- Running MapMyCells
- Assigning high-confidence cell type labels
- Normalization and feature selection
- scVI integration
- scANVI label transfer
- Clustering and UMAP visualization
- Final metadata and AnnData export
- QC and integration metrics

### Filtering

Filtering happens at the start of the cohort-analysis stage, after QC metrics and doublet scores have been calculated. By merging all samples and filtering out low-quality cells, the pipeline derives a QC-ed gene expression matrix for all cells in the dataset.

**Default cell-level filters** (a cell must pass all to remain in the filtered AnnData object):

| Metric | Default threshold |
|---|---|
| Mitochondrial gene percentage | `pct_counts_mt < 10` |
| Doublet score | `doublet_score < 0.2` |
| Total counts | `500 <= total_counts <= 100000` |
| Genes detected per cell | `300 <= n_genes_by_counts <= 10000` |

!!! note
    These thresholds are intentionally general — useful for standardized processing across many datasets, but not necessarily optimal for every biological question, brain region, cell type, or sample quality profile.

### Cell type annotation

The pipeline uses a two-stage cell type annotation strategy.

**1. MapMyCells reference mapping** — run before feature selection so annotation can use as many genes as possible.

| Workflow | Reference strategy |
|---|---|
| Human PMDBS | Allen Brain Map / SEA-AD taxonomy |
| Mouse | Allen Brain Map / 10x whole brain mouse taxonomy |

MapMyCells produces taxonomy labels and confidence-related metrics, including correlation coefficients and bootstrapping probabilities.

**2. High-confidence cell type assignment** — built from MapMyCells results.

- **Human PMDBS:** GABAergic neurons from the neuronal GABAergic class; glutamatergic neurons from the neuronal glutamatergic class; non-neuronal/non-neural cells use subclass-level labels.
- **Mouse:** GABAergic, glutamatergic, and serotonergic neurons identified from class labels; non-neuronal cells use subclass-level labels.

Lower-confidence mappings are marked `Unknown`. A mapping is lower-confidence if **either**:

- `correlation coefficient < 0.5`, or
- `bootstrapping probability < 0.5`

**3. scANVI label transfer** — after high-confidence labels are assigned, scANVI predicts labels for remaining cells (including those marked `Unknown`), giving a complete label set while preserving the distinction between direct high-confidence reference mappings and model-predicted labels. Review confidence metrics before relying on labels for a downstream question.

Users should review confidence metrics and consider whether the provided labels are appropriate for their downstream question.

### Processing and integration

After filtering and reference mapping:

1. Store raw counts in a `counts` layer
2. Normalize total counts
3. Apply log transformation
4. Score cell cycle
5. Select highly variable genes
6. Run PCA
7. Run scVI integration
8. Run scANVI label prediction
9. Build nearest-neighbor graph
10. Run Leiden clustering
11. Compute UMAP

**Highly variable genes:** default is **3000** genes, selected using the [`highly_variable_genes` method from Pearson's residuals](https://scanpy.readthedocs.io/en/stable/generated/scanpy.experimental.pp.highly_variable_genes.html#scanpy.experimental.pp.highly_variable_genes), applied to pre-processed counts. The batch key is used during selection.

**scVI integration:** default latent key `X_scVI` — reduces technical/batch-associated variation while preserving biological structure.

**scANVI labeling:** semi-supervised label transfer based on MapMyCells high-confidence labels. Default latent key `X_scANVI`; default prediction column `C_scANVI`.

**Harmony integration:** alongside scVI/scANVI, the final AnnData object also includes Harmony-equalized principal components as an additional batch-corrected embedding, so you have more than one integration method to compare.

**Clustering and UMAP:** neighbors computed on the selected latent representation; Leiden clustering run at multiple resolutions (default: `0.05, 0.1, 0.2, 0.4`). UMAPs are visual summaries of the integrated latent space, not direct proof of biological separation.

## What's next

See [Outputs & File Structure](outputs.md) for the actual files produced at each stage, where they're stored, and guidance on when to use the curated outputs as-is versus reprocessing them yourself.