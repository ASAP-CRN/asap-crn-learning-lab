# Pilot Workshop: ASAP-CRN Learning Lab

A guided, hands-on introduction to the ASAP-CRN Learning Lab. Three notebooks walk you through dataset discovery, exploration, and basic analysis using shared CRN resources.
 
The workshop is self-contained, reproducible, and runnable directly in Verily Workbench.
 
> **This is a pilot workshop** — feedback is encouraged. If you have suggestions, questions, or run into issues, please open an issue or share feedback with the CRN team.

---

Run these in order:
 
| Notebook | Focus | What you'll do |
|----------|-------|----------------|
| `01_getting_started.ipynb` | Orientation & data scoping | Locate data, understand naming conventions, inspect dataset-level metadata, and navigate the Learning Lab filesystem |
| `02_data_exploration.ipynb` | Curated Data loading & exploration | Load curated outputs (matrices, annotations), inspect dimensions and feature space, and run basic QC checks |
| `03_downstream_analysis.ipynb` | Analysis & interpretation | Perform lightweight downstream analysis, create visualizations, and interpret results in context |

## Getting Started
 
1. Launch a JupyterLab app in your Verily Workbench workspace.
2. Navigate to the workshop folder.
3. Open the notebooks in order and run cells top-to-bottom.

## Environment & Dependencies
 
Each notebook installs its own dependencies in the first cells, so **no manual setup is required**. This lets you run the workshop directly in any Workbench app with minimal friction.
 
An `environment.yml` is included for reproducibility. If you prefer a fully controlled or local setup:
 
```bash
conda env create -f environment.yml
conda activate <environment-name>   # see top of environment.yml
```
 
This is useful if you want to run notebooks outside Workbench, enforce strict version consistency, or customize the environment for your own work.

## Notes
 
- Intermediate outputs generated during the workshop are for demonstration only.
- To extend analyses, fork the Learning Lab repository or copy notebooks into your own workspace.
