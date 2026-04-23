# Substantia Nigra Single-Cell Cell Typing Case Study

This case study demonstrates a practical workflow for extracting **Substantia Nigra (SN)** cells from a larger cohort, preprocessing the data, and performing **reference-based cell type annotation** using **MapMyCells**.

The workflow is organized into three modular notebooks designed to be run sequentially.

## Case Study Goals

By completing this workflow, users will learn how to:

- Subset a large cohort to a biologically relevant brain region
- Prepare single-cell data for downstream annotation
- Apply reference-based cell type mapping with MapMyCells
- Validate dopaminergic neuron labels using canonical markers
- Generate annotated outputs and pseudobulk matrices for downstream analysis

---

# Notebook Modules

## Part 01 — Setup

📄 `sn_celltyping__part01_setup.ipynb`

Initial project configuration and data access.

### Covers:

- Define paths and output directories
- Copy data to personal workspace bucket
- Load AnnData objects and metadata
- Review cohort structure and available samples
- Prepare inputs for downstream processing

---

## Part 02 — Processing

📄 `sn_celltyping__part02_processing.ipynb`

Subset and preprocess Substantia Nigra cells from the full cohort.

### Covers:

- Identify and subset SN-region samples
- Restore raw counts
- Standard preprocessing workflows
- Feature selection and embeddings
- Save processed SN dataset for annotation

---

## Part 03 — MapMyCells Annotation

📄 `sc_celltyping__part03_mapmycells.ipynb`

Perform reference-based cell type annotation using the Allen Institute Human-Mammalian Brain Basal Ganglia taxonomy.

### Covers:

- Run MapMyCells taxonomy mapping
- Standardize returned labels and confidence metrics
- Validate dopaminergic labels using marker genes
- Refine annotations with confidence thresholds
- Export annotated data and pseudobulk outputs

Reference taxonomy:  
https://alleninstitute.github.io/abc_atlas_access/descriptions/HMBA-BG_dataset.html

---

# Primary Outputs

This workflow may generate:

- **Processed SN AnnData (`.h5ad`)**
- **Annotated AnnData with cell type labels**
- **Pseudobulk matrices** (all / case / control)
- **Cell type summary tables**
- **UMAP and QC figures**

---

# Environment

Recommended conda environment includes:

- `scanpy`
- `scvi-tools`
- `cell_type_mapper`
- `mygene`

## Example Setup

```bash
conda env create -f environment.yml
conda activate sn_celltyping
python -m ipykernel install --user --name=sn_celltyping --display-name "Python (sn_celltyping)"
```

# Suggested Compute Environemnt (based on Verily Workbench Resources) 
| Resource     | Value         |
| ------------ | ------------- |
| Machine type | n1-highmem-16 |
| CPUs         | 16            |
| Memory       | 104 GB        |
| Disk         | 500 GB        |
| Autostop     | 1 hour        |


# Notes 
- This workflow emphasizes reference-based annotation using MapMyCells.
- Additional label transfer methods such as scANVI may be explored as optional extensions.
- Confidence thresholds may be tuned depending on dataset characteristics.
- Rare cell populations may require extra care during model-based label transfer.

# Additional Resources
Explore more workflows and tutorials in the ASAP-CRN Learning Lab:
(https://github.com/ASAP-CRN/asap-crn-learning-lab)[https://github.com/ASAP-CRN/asap-crn-learning-lab]
