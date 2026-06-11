# Tutorials

Hands-on tutorials for learning how to access, explore, and analyze ASAP CRN Cloud data in Verily Workbench.

These tutorials are designed to help users build practical skills with CRN Cloud resources, from workspace orientation to exploratory analysis and downstream workflows.

---

## Tutorial Paths

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

### Spatial RNA-seq

Tutorials focused on spatial transcriptomics datasets, including Visium and GeoMx.

| Notebook | Description |
|---|---|
| [`01_load_spatial_data_visium_geomx.ipynb`](Spatial_RNAseq/01_load_spatial_data_visium_geomx.ipynb) | Load Visium and GeoMx datasets into AnnData and explore spatial metadata and coordinates |

**Recommended for:** users working with spatial transcriptomics datasets.

--- 

## Workshops

### Pilot Workshop Series

A structured tutorial series for building core skills with ASAP CRN Cloud data.

| Notebook | Description |
|---|---|
| [`01_getting_started.ipynb`](00_pilot_workshop_series/01_getting_started.ipynb) | Connect to CRN Cloud resources and load your first dataset |
| [`02_data_exploration.ipynb`](00_pilot_workshop_series/02_data_exploration.ipynb) | Explore metadata, visualize distributions, and inspect data quality |
| [`03_downstream_analysis.ipynb`](00_pilot_workshop_series/03_downstream_analysis.ipynb) | Run downstream analysis examples, including differential expression and summary statistics |

**Recommended for:** workshop participants, guided onboarding, and users who want a step-by-step learning path.

---

## Prerequisites

Before running these tutorials, make sure you have:

1. Approved access to the relevant ASAP CRN data collections through the [CRN Cloud Explorer](https://cloud.parkinsonsroadmap.org/collections)
2. Access to [Verily Workbench](https://workbench.verily.com/)
3. A duplicated copy of the ASAP CRN Learning Lab workspace with the `asap-crn-learning-lab` repository connected
4. A running JupyterLab or RStudio app in Verily Workbench

For setup instructions, see the [Getting Started Guide](https://asap-crn.github.io/asap-crn-learning-lab/).

---

## Folder Structure

```plaintext
tutorials/
├── Sample_Notebooks/
│   ├── Py3_Explore_ASAP_CRN_Data.ipynb
│   └── R_Explore_ASAP_CRN_Data.ipynb
├── Spatial_RNAseq
│   └──01_load_spatial_data_visium_geomx.ipynb
└── 00_pilot_workshop_series/
    ├── 01_getting_started.ipynb
    ├── 02_data_exploration.ipynb
    ├── 03_downstream_analysis.ipynb
    └── environment.yml

```
--- 
## Next Steps
After completing these tutorials, explore the applied case studies in: 

[../case_studies/](https://github.com/ASAP-CRN/asap-crn-learning-lab/tree/main/case_studies/)

Case studies build on the same workspace and data access concepts, but focus on specific biological questions and analysis workflows.
