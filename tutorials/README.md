# Tutorials

Hands-on tutorials for learning how to access, explore, and analyze ASAP CRN Cloud data in Verily Workbench.

These tutorials are designed to help users build practical skills with CRN Cloud resources, from workspace orientation to exploratory analysis, downstream workflows, and integration with other Parkinson's disease programs.

---

## Tutorial Paths

| If you want to... | Start with |
|---|---|
| Get oriented in the CRN Cloud and Verily Workbench | [Sample Notebooks](#sample-notebooks) |
| Follow a guided, step-by-step learning path | [Pilot Workshop Series](#pilot-workshop-series) |
| Build one clean metadata table for a cohort | [Metadata Assembly](#metadata-assembly) |
| Resolve a rare cell population in single-cell data | [Rare Cell Type Analysis](#rare-cell-type-analysis) |
| Work with spatial transcriptomics data | [Spatial RNA-seq](#spatial-rna-seq) |
| Link CRN samples to GP2 genetics data | [GP2 × CRN Interoperability](#gp2--crn-interoperability) |

---

## Getting Started
New to the CRN Cloud? Start here.

### Sample Notebooks

Quick-start notebooks for users who want a lightweight introduction to CRN Cloud data organization in Verily Workbench.

| Notebook | Description |
|---|---|
| [`Py3_Explore_ASAP_CRN_Data.ipynb`](Sample_Notebooks/Py3_Explore_ASAP_CRN_Data.ipynb) | Python sample notebook for locating mounted resources, previewing metadata, inspecting curated outputs, and exploring AnnData files |
| [`R_Explore_ASAP_CRN_Data.ipynb`](Sample_Notebooks/R_Explore_ASAP_CRN_Data.ipynb) | R sample notebook for locating mounted resources, previewing metadata, inspecting curated outputs, and exploring CRN data in R |

**Recommended for:** first-time users, quick orientation, and users who want to understand the workspace layout before running deeper analyses.

---

## Workshops

### Pilot Workshop Series

A structured tutorial series for building core skills with ASAP CRN Cloud data.

| Notebook | Description |
|---|---|
| [`01_getting_started.ipynb`](Workshops/00_pilot_workshop_series/01_getting_started.ipynb) | Connect to CRN Cloud resources and load your first dataset |
| [`02_data_exploration.ipynb`](Workshops/00_pilot_workshop_series/02_data_exploration.ipynb) | Explore metadata, visualize distributions, and inspect data quality |
| [`03_downstream_analysis.ipynb`](Workshops/00_pilot_workshop_series/03_downstream_analysis.ipynb) | Run downstream analysis examples, including differential expression and summary statistics |

**Recommended for:** workshop participants, guided onboarding, and users who want a step-by-step learning path.

---

## Analysis Tutorials

### Metadata Assembly

Merge a cohort's SAMPLE, SUBJECT, and CLINPATH tables into one cleaned, sample-level metadata table. Duplicate records are combined, and any disagreements are logged for review. Built for the PMDBS sc/snRNA-seq collection; other dataset types may need edits.

| Notebook | Description |
|---|---|
| [`Assembling_CRN_Metadata.ipynb`](Metadata_Assembly/Assembling_CRN_Metadata.ipynb) | Merge and clean cohort metadata, check for duplicates and conflicts, and save a sample-level table with conflict reports |

**Recommended for:** users who need sample, subject, and clinical metadata in one place before an analysis. See the [README](Metadata_Assembly/README.md) for details.

---

### Rare Cell Type Analysis

Subset one brain region from the PMDBS sc/snRNA-seq cohort, recover full-gene counts, annotate with MapMyCells, and integrate with scVI/scANVI to resolve a rare cell population. Worked example: dopaminergic neurons in the substantia nigra.

| Notebook | Description |
|---|---|
| [`01_cpu_subset_and_annotate.ipynb`](Rare_Celltype_Analysis/01_cpu_subset_and_annotate.ipynb) | Subset a brain region, recover full-gene counts, and annotate cells with MapMyCells (CPU app) |
| [`02_gpu_integrate_and_export.ipynb`](Rare_Celltype_Analysis/02_gpu_integrate_and_export.ipynb) | Integrate with scVI/scANVI to resolve the rare population and export results (GPU app) |

**Recommended for:** users working with single-cell data who want to study a specific or rare cell population. See the [README](Rare_Celltype_Analysis/README.md) for details.

---

### Spatial RNA-seq

Tutorials focused on spatial transcriptomics datasets, including Visium and GeoMx.

| Notebook | Description |
|---|---|
| [`01_load_spatial_data_visium_geomx.ipynb`](Spatial_RNAseq/01_load_spatial_data_visium_geomx.ipynb) | Load Visium and GeoMx datasets into AnnData and explore spatial metadata and coordinates |

**Recommended for:** users working with spatial transcriptomics datasets.

---

## Data Integration

### GP2 × CRN Interoperability

Link CRN PMDBS sc/snRNA-seq samples to [GP2](https://gp2.org) participants, and add GP2 study, phenotype, and genetic data availability (NBA, WGS) to each sample. Built in the [GP2 × ASAP CRN Verily Workbench workspace](https://workbench.verily.com/workspaces/gp2).

| Notebook | Description |
|---|---|
| [`GP2_CRN_Interoperability.ipynb`](GP2_CRN_Interoperability/GP2_ASAPCRN_Interoperability.ipynb) | Clean GP2 IDs, join the GP2 master key onto CRN samples, and check match coverage and genetic data availability |

**Before you start:** run [Metadata Assembly](#metadata-assembly) for the PMDBS cohort first. This tutorial also requires approved GP2 Tier 2 access.

**Recommended for:** users who want to combine CRN single-cell data with GP2 genetics. See the [README](GP2_CRN_Interoperability/README.md) for details.

---

## Prerequisites

Before running these tutorials, make sure you have:

1. Approved access to the relevant ASAP CRN data collections through the [CRN Cloud Explorer](https://cloud.parkinsonsroadmap.org/collections)
2. Access to [Verily Workbench](https://workbench.verily.com/)
3. A duplicated copy of the ASAP CRN Learning Lab workspace with the `asap-crn-learning-lab` repository connected
4. A running JupyterLab or RStudio app in Verily Workbench

The **GP2 × CRN Interoperability** tutorial also requires approved GP2 Tier 2 access and the [GP2 × ASAP CRN workspace](https://workbench.verily.com/workspaces/gp2). Contact [pm@gp2.org](mailto:pm@gp2.org) for GP2 workspace access.

For setup instructions, see the [Getting Started Guide](https://asap-crn.github.io/asap-crn-learning-lab/).

---

## Folder Structure

```plaintext
tutorials/
├── GP2_CRN_Interoperability/
│   ├── GP2_CRN_Interoperability.ipynb
│   └── README.md
├── Metadata_Assembly/
│   ├── Assembling_CRN_Metadata.ipynb
│   └── README.md
├── Rare_Celltype_Analysis/
│   ├── 01_cpu_subset_and_annotate.ipynb
│   ├── 02_gpu_integrate_and_export.ipynb
│   ├── environment.yml
│   └── README.md
├── Sample_Notebooks/
│   ├── Py3_Explore_ASAP_CRN_Data.ipynb
│   └── R_Explore_ASAP_CRN_Data.ipynb
├── Spatial_RNAseq/
│   └── 01_load_spatial_data_visium_geomx.ipynb
├── Workshops/
│   └── 00_pilot_workshop_series/
│       ├── 01_getting_started.ipynb
│       ├── 02_data_exploration.ipynb
│       ├── 03_downstream_analysis.ipynb
│       └── environment.yml
└── README.md
```

---

## Next Steps

After completing these tutorials, explore the applied case studies in [`case_studies/`](../case_studies/).

Case studies build on the same workspace and data access concepts, but focus on specific biological questions and analysis workflows.
