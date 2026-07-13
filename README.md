![ASAP logo](./docs/images/ASAP-CRN_logo.png)
# ASAP CRN Learning Lab

Reproducible tutorials and analysis examples for working with ASAP CRN data to spark new discoveries in Parkinson's disease.

[![Getting Started Guide](https://img.shields.io/badge/Getting_Started_Guide-Live-blue)](https://asap-crn.github.io/asap-crn-learning-lab/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)

## Overview

The ASAP CRN Learning Lab is designed to facilitate exploration and analysis of [ASAP CRN Cloud](https://cloud.parkinsonsroadmap.org/collections) data through reproducible exploratory and meta-analysis examples. Users may engage via workshops or start directly with the modules most relevant to their research.

## Prerequisite: Data Access

Before running any tutorials or case studies, users must request and receive approval for the relevant **ASAP-CRN data collections** via the [CRN Cloud Explorer](https://cloud.parkinsonsroadmap.org/collections). Once approved, datasets can be accessed within supported analysis environments, including Verily Workbench.

For detailed instructions, please see the [ASAP CRN Cloud User Manual](https://storage.googleapis.com/asap-public-assets/wayfinding/ASAP-CRN-Cloud-User-Manual.pdf).

## Getting started

> **First time here?** Head to our [Getting Started guide](https://asap-crn.github.io/asap-crn-learning-lab/) for the full onboarding experience — including how to request data access, set up Verily Workbench, and run your first notebook.

For help with Workbench setup, GitHub workflows, or common errors, see the [troubleshooting page](https://asap-crn.github.io/asap-crn-learning-lab/troubleshooting/).


## Tutorials

Hands-on modules for building core skills with CRN Cloud data. Each series includes its own `environment.yml`.

| Notebook | Description |
|----------|-------------|
| [`01_getting_started.ipynb`](tutorials/Workshops/00_pilot_workshop_series/01_getting_started.ipynb) | Connect to CRN Cloud and load your first dataset |
| [`02_data_exploration.ipynb`](tutorials/Workshops/00_pilot_workshop_series/02_data_exploration.ipynb) | Explore metadata, visualize distributions, and inspect quality |
| [`03_downstream_analysis.ipynb`](tutorials/Workshops/00_pilot_workshop_series/03_downstream_analysis.ipynb) | Run differential expression and basic statistical analyses |
| [`Py3_Explore_ASAP_CRN_Data.ipynb`](tutorials/Sample_Notebooks/Py3_Explore_ASAP_CRN_Data.ipynb) | Introduction to working with CRN Data on Verily Workbench |
| [`R_Explore_ASAP_CRN_Data.ipynb`](tutorials/Sample_Notebooks/PR_Explore_ASAP_CRN_Data.ipynb) | Introduction to working with CRN Data on Verily Workbench |
[`01_load_spatial_data_visium_geomx.ipynb](tutorials/Spatial_RNAseq/01_load_spatial_data_visium_geomx.ipynb) | Load Visium and GeoMx datasets into AnnData and explore spatial metadata and coordinates |

## Case studies

Analysis examples with a specific biological objective. Each case study includes its own `environment.yml` and `README.md` with background and instructions.

| Case study | Description |
|------------|-------------|
| [`SN_CellType_Annotation/`](case_studies/SN_CellType_Annotation/) | Cell-type annotation and analysis in the substantia nigra |


## Repository Structure

```plaintext
asap-crn-learning-lab/
│
├── docs/                     # GitHub Pages source
│   ├── index.md
│   ├── getting-started.md
│   └── images/
├── tutorials/               # Learning resources and guided tutorials
│   └── Sample_Notebooks   
│       ├──  Py3_Explore_ASAP_CRN_Data.ipynb
│       └──  R_Explore_ASAP_CRN_Data.ipynb
│   └── Spatial_RNAseq          
│       └── 01_load_spatial_data_visium_geomx.ipynb
│   └── Workshops          
│       └── 00_pilot_workshop_series
│           ├── 01_getting_started.ipynb
│           ├── 02_data_exploration.ipynb
│           ├── 03_downstream_analysis.ipynb
│           └── environment.yml

├── case_studies/              # Analyses with a biological objective
│   └── SN_CellType_Annotation
│       ├──sn_celltyping__part01_setup.ipynb
│       ├──sn_celltyping__part02_preprocessing.ipynb
│       ├──sc_celltyping__part03_mapmycells.ipynb
│       ├── environment.yml
│       └── README.md
├── mkdocs.yml
├── .github
│   ├── workflows
│   └── build_docs.yml
├── requirements-docs.txt
├── LICENSE                 
└── README.md             
```
---

## Contributing

We welcome contributions from the ASAP-CRN community and the broader research ecosystem.

- **Found a typo?** Submit a pull request.
- **Have a new dataset or tutorial idea?** [Open an issue](https://github.com/asap-crn/asap-crn-learning-lab/issues). 

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

