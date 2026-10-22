# Tutorials & Case Studies

Hands-on ways to build skills with CRN Cloud data and see those skills applied to real research questions.

If you have not yet set up data access and a Verily Workbench workspace, start with [Requesting Data Access](../getting-started/requesting-data-access.md) and the [Verily Workbench Guide](../workbench/index.md) first.

## Tutorials

Tutorials are hands-on modules for building core skills with CRN Cloud data. Tutorials with extra dependencies include an `environment.yml` to help recreate the required software environment, and tutorial folders include a `README.md` with instructions.

### Pilot Workshop Series

Sequential, numbered notebooks that provide a guided path from first connection to a basic analysis.

Located in:

```text
tutorials/Workshops/00_pilot_workshop_series/
```

| Notebook                                                                                                                                                                | What it teaches                                                |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| [`01_getting_started.ipynb`](https://github.com/ASAP-CRN/asap-crn-learning-lab/blob/main/tutorials/Workshops/00_pilot_workshop_series/01_getting_started.ipynb)         | Connect to CRN Cloud and load your first dataset               |
| [`02_data_exploration.ipynb`](https://github.com/ASAP-CRN/asap-crn-learning-lab/blob/main/tutorials/Workshops/00_pilot_workshop_series/02_data_exploration.ipynb)       | Explore metadata, visualize distributions, and inspect quality |
| [`03_downstream_analysis.ipynb`](https://github.com/ASAP-CRN/asap-crn-learning-lab/blob/main/tutorials/Workshops/00_pilot_workshop_series/03_downstream_analysis.ipynb) | Run differential expression and basic statistical analyses     |

**Best for:** first-time users who want a guided, sequential introduction.

### Sample Notebooks

Standalone references, not a sequence. These are useful once you already know what you are looking for or want a quick example in Python or R.

Located in:

```text
tutorials/Sample_Notebooks/
```

| Notebook                                                                                                                                                    | What it teaches                                                        |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| [`Py3_Explore_ASAP_CRN_Data.ipynb`](https://github.com/ASAP-CRN/asap-crn-learning-lab/blob/main/tutorials/Sample_Notebooks/Py3_Explore_ASAP_CRN_Data.ipynb) | Introduction to working with CRN data on Verily Workbench using Python |
| [`R_Explore_ASAP_CRN_Data.ipynb`](https://github.com/ASAP-CRN/asap-crn-learning-lab/blob/main/tutorials/Sample_Notebooks/R_Explore_ASAP_CRN_Data.ipynb)     | Introduction to working with CRN data on Verily Workbench using R      |

**Best for:** users who want a quick reference rather than a guided sequence.

### Metadata Assembly

Merge a cohort's SAMPLE, SUBJECT, and CLINPATH tables into one cleaned, sample-level metadata table. Duplicate records are combined, and any disagreements are logged for review.

Located in:

```text
tutorials/Metadata_Assembly/
```

| Notebook | What it teaches |
| --- | --- |
| [`Assembling_CRN_Metadata.ipynb`](https://github.com/ASAP-CRN/asap-crn-learning-lab/blob/main/tutorials/Metadata_Assembly/Assembling_CRN_Metadata.ipynb) | Merge and clean cohort metadata, find and combine duplicate records, and review conflicts |

> **Note:** Built for the PMDBS sc/snRNA-seq collection. Other dataset types may have different tables or column names, so the notebook may need edits. See the [README](https://github.com/ASAP-CRN/asap-crn-learning-lab/blob/main/tutorials/Metadata_Assembly/README.md) for details.

**Best for:** users who need sample, subject, and clinical metadata in one place before an analysis.

### Rare Cell Type Analysis

Subset one brain region from the PMDBS sc/snRNA-seq cohort, recover full-gene counts, annotate with MapMyCells, and integrate with scVI/scANVI to resolve a rare cell population. Worked example: dopaminergic neurons in the substantia nigra.

Located in:

```text
tutorials/Rare_Celltype_Analysis/
```

| Notebook | What it teaches |
| --- | --- |
| [`01_cpu_subset_and_annotate.ipynb`](https://github.com/ASAP-CRN/asap-crn-learning-lab/blob/main/tutorials/Rare_Celltype_Analysis/01_cpu_subset_and_annotate.ipynb) | Subset a brain region, recover full-gene counts, and annotate cells with MapMyCells (CPU app) |
| [`02_gpu_integrate_and_export.ipynb`](https://github.com/ASAP-CRN/asap-crn-learning-lab/blob/main/tutorials/Rare_Celltype_Analysis/02_gpu_integrate_and_export.ipynb) | Integrate with scVI/scANVI to resolve the rare population and export results (GPU app) |

**Best for:** users who want to study a specific or rare cell population. This is a reusable version of the [Substantia Nigra Cell-Type Annotation](#substantia-nigra-cell-type-annotation) case study that can target other regions.

### Spatial RNA-seq

Tutorials focused on spatial transcriptomics datasets, including Visium and GeoMx.

Located in:

```text
tutorials/Spatial_RNAseq/
```

| Notebook | What it teaches |
| --- | --- |
| [`01_load_spatial_data_visium_geomx.ipynb`](https://github.com/ASAP-CRN/asap-crn-learning-lab/blob/main/tutorials/Spatial_RNAseq/01_load_spatial_data_visium_geomx.ipynb) | Load Visium and GeoMx datasets into AnnData and explore spatial metadata and coordinates |

**Best for:** users working with spatial transcriptomics datasets.

### GP2 × CRN Interoperability

Link CRN PMDBS sc/snRNA-seq samples to [GP2](https://gp2.org) participants, and add GP2 study, phenotype, and genetic data availability (NBA, WGS) to each sample. Built in the [GP2 × ASAP CRN Verily Workbench workspace](https://workbench.verily.com/workspaces/gp2).

Located in:

```text
tutorials/GP2_CRN_Interoperability/
```

| Notebook | What it teaches |
| --- | --- |
| [`GP2_CRN_Interoperability.ipynb`](https://github.com/ASAP-CRN/asap-crn-learning-lab/blob/main/tutorials/GP2_CRN_Interoperability/GP2_CRN_Interoperability.ipynb) | Clean GP2 IDs, join the GP2 master key onto CRN samples, and check match coverage and genetic data availability |

> **Note:** Run [Metadata Assembly](#metadata-assembly) for the PMDBS cohort first. This tutorial also requires approved GP2 Tier 2 access. See the [README](https://github.com/ASAP-CRN/asap-crn-learning-lab/blob/main/tutorials/GP2_CRN_Interoperability/README.md) for details.

**Best for:** users who want to combine CRN single-cell data with GP2 genetics.

## Case Studies

Case studies apply pipeline outputs and Workbench tools to a specific biological question, end to end.

Unlike the tutorials above, case studies live in their own top-level `case_studies/` folder in the repository. Each case study includes its own `environment.yml` and `README.md` with background and setup instructions.

### Substantia Nigra Cell-Type Annotation

Located in:

```text
case_studies/SN_CellType_Annotation/
```

| Notebook                                                                                                                                                                                 | Step                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| [`sn_celltyping__part01_setup.ipynb`](https://github.com/ASAP-CRN/asap-crn-learning-lab/blob/main/case_studies/SN_CellType_Annotation/sn_celltyping__part01_setup.ipynb)                 | Setup                 |
| [`sn_celltyping__part02_processing.ipynb`](https://github.com/ASAP-CRN/asap-crn-learning-lab/blob/main/case_studies/SN_CellType_Annotation/sn_celltyping__part02_processing.ipynb) | Processing |
| [`sn_celltyping__part03_mapmycells.ipynb`](https://github.com/ASAP-CRN/asap-crn-learning-lab/blob/main/case_studies/SN_CellType_Annotation/sn_celltyping__part03_mapmycells.ipynb)       | MapMyCells annotation |

**Best for:** seeing how data access, Verily Workbench, and the [scRNA-seq pipeline](../pipeline/index.md) cell-type annotation strategy come together in an applied research workflow.

## Prerequisites

Before running any tutorial or case study, make sure you have:

* [Requested data access](../getting-started/requesting-data-access.md)
* Set up your [Verily Workbench workspace](../workbench/index.md)
* Connected the [Learning Lab GitHub repo](../workbench/github.md) to your workspace

The **GP2 × CRN Interoperability** tutorial also requires approved GP2 Tier 2 access and the [GP2 × ASAP CRN workspace](https://workbench.verily.com/workspaces/gp2). Contact [pm@gp2.org](mailto:pm@gp2.org) for GP2 workspace access.

If a tutorial or case study folder includes an `environment.yml`, install that environment before running the notebooks. Folders without one only need the packages preinstalled in Verily Workbench.
