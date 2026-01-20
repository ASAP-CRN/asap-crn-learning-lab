# Pilot Workshop: ASAP-CRN Learning Lab

This pilot workshop introduces users to the **ASAP-CRN Learning Lab** through a guided, hands-on workflow using three notebooks. Together, these notebooks walk through dataset discovery, exploration, and basic analysis using shared CRN resources.

The workshop is designed to be **self-contained**, reproducible, and runnable directly in Verily Workbench. 

---

## Workshop Notebooks

The workshop consists of three notebooks, intended to be run in order:

### Notebook 1: Workspace Orientation & Data Scoping

**Purpose:**
Introduces the dataset, directory structure, and key metadata. Users learn how to locate data, understand naming conventions, and inspect dataset-level context.

**Topics covered:**

- Overview of the dataset and collection
- Navigating the Learning Lab filesystem
- Reading dataset and file metadata
- Understanding curated vs. intermediate outputs

---

### Notebook 2: Data Loading & Exploration

**Purpose:**
Demonstrates how to load curated outputs into the analysis environment and perform basic exploratory checks.

**Topics covered:**

- Loading curated data objects (e.g., matrices, annotations)
- Inspecting dimensions, metadata, and feature space
- Basic QC summaries and sanity checks
- Familiarization with curated data formats

---

### Notebook 3: Downstream Analysis & Interpretation

**Purpose:**
Walks through a lightweight downstream analysis to illustrate how curated outputs can be used for biological or technical interpretation.

**Topics covered:**
- Simple analysis or aggregation steps
- Example visualizations
- Interpreting results in the context of the dataset
- Pointers to where more advanced analyses would fit

---
## Environment & Dependencies

### `environment.yml`

An `environment.yml` file is included to document the intended software environment for this workshop and support reproducibility.

- It lists the core Python packages and versions used across the notebooks.
- Users do not need to manually create this environment to run the workshop.

### Notebook-Based Package Installation
Each notebook includes package installation checks in the first cells, allowing the workshop to run smoothly even if the environment is not pre-configured.

This approach:

- Reduces setup friction for first-time users
- Allows notebooks to be run directly in existing Workbench apps
- Still preserves reproducibility through the provided environment.yml

---  

## How to Run the Workshop
1. Launch a JupyterLab app in your Verily Workbench workspace.
2. Navigate to the workshop folder.
3. Open the notebooks in order:
    1. `01_getting_started.ipynb`
    2. `02_data_exploration.ipynb`
    3. `03_downstream_analysis.ipynb`
4. Run cells top-to-bottom in each notebook.

---

## Notes & Best Practices
- Intermediate outputs generated during the workshop are for demonstration only.
- Users interested in extending analyses should fork the Learning Lab repository or copy notebooks into their own workspace.

---

## Feedback 
This is a **pilot workshop**, and feedback is encouraged.
If you have suggestions, questions, or run into issues, please open an issue or share feedback with the CRN team.
