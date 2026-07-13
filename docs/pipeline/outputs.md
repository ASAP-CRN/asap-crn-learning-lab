# Key Outputs & File Structures

The pipeline produces curated data at two levels:

-  **dataset-level** data curated per ASAP team, and 
- fully harmonized **cohort-level** data that integrates all contributing teams.

 Within each level, artifacts are categorized as **preprocessed**, **processed**, **integrated**, or **final**, depending on how far they've moved through the pipeline. Raw FASTQ data is also available separately for teams that need to start from the original sequencing files.

The final harmonized data is also benchmarked with [scib-metrics](https://scib-metrics.readthedocs.io/en/stable/index.html), which characterizes biological conservation and batch correction quality; a summary table and figure are produced for each cohort and team-level run (see QC and Validation Summaries below).

## Dataset-level curated data

Produced per ASAP team and dataset, prior to cohort-wide integration. Stored at:

```
gs://asap-curated-<team_name>-pmdbs-<sc_dataset_name>
```

| Stage | File | Type | Description | Location |
|---|---|---|---|---|
| Preprocessed | Gene expression matrix (raw) | H5 | Raw gene expression matrix from CellRanger | `preprocess/<ASAP_sample_id>_<replicate>.raw_feature_bc_matrix.h5` |
| Preprocessed | Gene expression matrix (filtered) | H5 | Filtered gene expression matrix from CellRanger | `preprocess/<ASAP_sample_id>_<replicate>.filtered_feature_bc_matrix.h5` |
| Preprocessed | Molecule information | H5 | Detailed molecular data from CellRanger | `preprocess/<ASAP_sample_id>_<replicate>.molecule_info.h5` |
| Preprocessed | CellRanger metrics | CSV | Metrics summary from the preprocessing step | `preprocess/<ASAP_sample_id>_<replicate>.metrics_summary.csv` |
| Preprocessed | CellBender output | H5 | Ambient RNA-removed cell counts (plus auxiliary CellBender artifacts) | `preprocess/<ASAP_sample_id>_<replicate>.cellbender_filtered.h5` |
| Preprocessed | Raw counts AnnData | H5AD | AnnData object capturing raw counts | `preprocess/<ASAP_sample_id>_<replicate>.adata_object.h5ad` |
| Processed | Initial cell metadata | CSV | Basic cell metadata for samples | `cohort_analysis/<team_name>.initial_metadata.csv` |
| Processed | Merged sample AnnData object | H5AD | QC-ed AnnData object | `cohort_analysis/<team_name>.merged_adata_object.h5ad` |
| Processed | Sample list | TSV | All samples contributing to the team-level curated data | `cohort_analysis/<team_name>.sample_list.tsv` |
| Integrated | scVI model | TAR.GZ | Trained scVI model | `cohort_analysis/<team_name>_scvi_model.tar.gz` |
| Final | Final full metadata | CSV | Basic cell metadata for samples  | `cohort_analysis/asap-cohort.final_metadata.csv` |
| Final | Final full artifact | H5AD | scVI-integrated AnnData object with all embeddings (PCA, UMAP, scVI, Harmony) | `cohort_analysis/<team_name>.final_adata.h5ad` |

## Cohort-level curated data

The fully integrated, harmonized dataset across all contributing teams. Stored at:

```
gs://asap-curated-cohort-pmdbs-sc-rnaseq
```

| Stage | File | Type | Description | Location |
|---|---|---|---|---|
| Processed | Sample list | TSV | All samples contributing to the cohort-level curated data | `cohort_analysis/asap-cohort.sample_list.tsv` |
| Processed | Initial cell metadata | CSV | Basic cell metadata for merged samples | `cohort_analysis/asap-cohort.initial_metadata.csv` |
| Processed | Merged sample AnnData object | H5AD | QC-ed AnnData object | `cohort_analysis/asap-cohort.merged_adata_object.h5ad` |
| Processed | Cell types | CSV | Inferred cell types | `cohort_analysis/asap-cohort.cell_types.csv` |
| Processed | scVI model | TAR.GZ | Trained scVI model | `cohort_analysis/asap-cohort_scvi_model.tar.gz` |
| Final | Final full metadata | CSV | Basic cell metadata for merged samples  | `cohort_analysis/asap-cohort.final_metadata.csv` |
| Final | Final full artifact | H5AD | scVI-integrated AnnData object with all embeddings (PCA, UMAP, scVI, Harmony) | `cohort_analysis/asap-cohort.final_adata.h5ad` |

## QC and validation summaries

A family of plots illustrates QC statistics and gives an overall picture of the dataset — embedding plots show batch labels, doublet scores, cell types, total counts, feature counts, percent mitochondrial, percent ribosomal, and samples across the UMAP, alongside a UMI-count-vs-gene-count scatter and per-metric violin plots.

| File | Type | Description | Location |
|---|---|---|---|
| Groups UMAP | PNG | UMAP embedding labeled by sample, batch, and cell type | `cohort_analysis/<asap-cohort\|team_name>.groups.umap.png` |
| Features UMAP | PNG | UMAP embedding labeled by n_genes_by_counts, total_counts, pct_counts_mt, pct_counts_rb, doublet_score, S_score, and G2M_score | `cohort_analysis/<asap-cohort\|team_name>.features.umap.png` |
| QC: N genes by count | PNG | QC violin plot for n_genes_by_counts | `cohort_analysis/<asap-cohort\|team_name>.n_genes_by_counts.violin.png` |
| QC: total counts | PNG | QC violin plot for total_counts | `cohort_analysis/<asap-cohort\|team_name>.total_counts.violin.png` |
| QC: percent mitochondrial | PNG | QC violin plot for pct_counts_mt | `cohort_analysis/<asap-cohort\|team_name>.pct_counts_mt.violin.png` |
| QC: percent ribosomal | PNG | QC violin plot for pct_counts_rb | `cohort_analysis/<asap-cohort\|team_name>.pct_counts_rb.violin.png` |
| QC: doublet scores | PNG | QC violin plot for doublet_score | `cohort_analysis/<asap-cohort\|team_name>.doublet_score.violin.png` |
| Scib values table | CSV | scib-metrics validation of outputs | `cohort_analysis/<cohort\|team>.scib_report.csv` |
| Scib validation figure | SVG | scib-metrics report assessing batch correction vs. biological conservation (not yet surfaced in-platform) | `cohort_analysis/<cohort\|team>.scib_results.svg` |

## Raw data

Raw FASTQ files transferred by each ASAP CRN team are available, but stored in **Requester Pays** buckets on Google Cloud Platform — a Google Cloud billing account must be registered to access them. See [How to Access and Analyze Raw Files in Verily Workbench](https://workbench.verily.com/workspaces/asap-crn-reference-workspace/resources/9099df22-8412-4c7c-adb7-810f261d0820/docs/how-to-access-and-analyze-raw-files-in-verily-workbench.html) for details.


## Using the outputs

### Use the curated outputs as-is when you want to:

- Start from a standardized, harmonized version of the data
- Explore the cohort structure
- Review metadata and sample composition
- Inspect QC metrics
- Run through a CRN tutorial or onboarding analysis
- Compare broad cell type distributions
- Use a consistent starting object for downstream analysis

The recommended starting points are usually the **final full artifact** and its accompanying metadata (see tables above):

- Use the final AnnData object (`{cohort_id}.final_adata.h5ad`) when you need the processed expression matrix, embeddings, annotations, and metadata together.
- Use the final metadata CSV (`{cohort_id}.final_metadata.csv`) when you only need sample, cell, annotation, QC, or clustering metadata. *(See the flag above — this file isn't yet listed in the tables.)*

### Reprocess or customize when your analysis requires decisions that differ from the standardized CRN processing assumptions, for example:

- Testing a specific biological hypothesis
- Focusing on one brain region
- Comparing disease versus control within a restricted donor set
- Studying a rare cell population
- Requiring more stringent QC
- Using a different cell type annotation strategy
- Changing the batch correction variable
- Including or excluding specific covariates
- Reintegrating a subset of samples or cell types

## Summary

The ASAP CRN sc/snRNA-seq pipeline provides standardized processing for single- and multi-team human and mouse sc/snRNA-seq data — sample-level preprocessing, QC, filtering, reference-based annotation, scVI/scANVI/Harmony integration, clustering, visualization, and final AnnData export.

Curated outputs are best used as a harmonized starting point. Customize, subset, reprocess, or reannotate as needed for your specific biological question.