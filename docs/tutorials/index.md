# Tutorials & Case Studies

Hands-on ways to build skills with CRN Cloud data and see those skills applied to real research questions.

If you have not yet set up data access and a Verily Workbench workspace, start with [Requesting Data Access](../getting-started/requesting-data-access.md) and the [Verily Workbench Guide](../workbench/index.md) first.

## Tutorials

Tutorials are hands-on modules for building core skills with CRN Cloud data. Each tutorial series includes an `environment.yml` to help recreate the required software environment.

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
| [`sn_celltyping__part02_preprocessing.ipynb`](https://github.com/ASAP-CRN/asap-crn-learning-lab/blob/main/case_studies/SN_CellType_Annotation/sn_celltyping__part02_preprocessing.ipynb) | Preprocessing         |
| [`sn_celltyping__part03_mapmycells.ipynb`](https://github.com/ASAP-CRN/asap-crn-learning-lab/blob/main/case_studies/SN_CellType_Annotation/sn_celltyping__part03_mapmycells.ipynb)       | MapMyCells annotation |

**Best for:** seeing how data access, Verily Workbench, and the [scRNA-seq pipeline](../pipeline/index.md) cell-type annotation strategy come together in an applied research workflow.

## Prerequisites

Before running any tutorial or case study, make sure you have:

* [Requested data access](../getting-started/requesting-data-access.md)
* Set up your [Verily Workbench workspace](../workbench/index.md)
* Connected the [Learning Lab GitHub repo](../workbench/github.md) to your workspace

Each tutorial or case study folder includes its own `environment.yml`. Install the appropriate environment before running the notebooks.
