# Release Compatibility

This document tracks compatibility between the Learning Lab repository and major CRN data releases.

It is intended to help users identify:
- which CRN release is currently supported in this repo
- which datasets and tutorials are aligned to that release
- the recommended Verily Workbench workspaces and data collections to use

## Current Supported Release

**Current CRN Release:** `v5`  
**Status:** `current`  
**Validated on:** `2026-06-11`  
**Repo tag:** `crn-v5.0`

### Recommended Verily Workbench Resources

| Resource Type | Name | Purpose | Link | Notes |
|---------------|------|---------|------|-------|
| Workspace | `ASAP CRN Learning Lab Workspace V5` | Primary recommended workspace for current tutorials |https://workbench.verily.com/workspaces/asap-crn-learning-lab-ws-v5 | 
| Data Collection | `PMDBS Single-cell RNAseq Collection V3` | Current recommended PMDBS scRNAseq data collection for this release |https://workbench.verily.com/data-collections/asap-crn-pmdbs-scrnaseq-collection |
| Data Collection | `PMDBS Spatial RNAseq Collection V1` | Current recommended PMDBS Spatial data collection for this release | https://workbench.verily.com/data-collections/asap-crn-pmdbs-spatial-rnaseq-collection

---

## Release Summary

| CRN Release | Repo Tag | Status | Validated On | Notes |
|-------------|----------|--------|--------------|-------|
| `v5` | `crn-v5.0` | `current` | `2026-06-11` | `compatible with v5 release of asap-crn` |
| `v4` | `crn-v4.0` | `archived` | `2026-04-24` | `compatible with v4 release of asap-crn` |

---

## Tutorials by Release

### CRN Release `v5`

#### Supported tutorials

| Tutorial / Notebook | Dataset(s) | Collection | Workspace | Data Collection | Status |
|---------------------|------------|------------|-----------|-----------------|--------|
| `tutorials/Workshops/00_pilot_workshop` | `cohort-pmdbs-sc-rnaseq` | `PMDBS` | `ASAP CRN Learning Lab Workspace V5` | `PMDBS Single-cell RNAseq Collection V3` | `supported` |
| `tutorials/Sample_Notebooks/` | `cohort-pmdbs-sc-rnaseq` | `PMDBS` | `ASAP CRN Learning Lab Workspace V5` | `PMDBS Single-cell RNAseq Collection V3` | `supported` |
| `tutorials/01_load_spatial_data_visium_geomx.ipynb` | `edwards-pmdbs-spatial-geomx-th`, `scherzer-pmdbs-spatial-visium-mtg` | `PMDBS` | `ASAP CRN Learning Lab Workspace V5` | `PMDBS Spatial RNAseq Collection V1` | `supported` |
| `case_studies/SN_CellType_Annotation` | `cohort-pmdbs-sc-rnaseq` | `PMDBS` | `ASAP CRN Learning Lab Workspace V5` | `PMDBS Single-cell RNAseq Collection V3` | `supported` |

### CRN Release `v4`

#### Supported tutorials

| Tutorial / Notebook | Dataset(s) | Collection | Workspace | Data Collection | Status
|---------------------|------------|------------|-----------|-----------------|--------|
| `tutorials/00_pilot_workshop` | `cohort-pmdbs-sc-rnaseq` | `PMDBS` | `ASAP CRN Learning Lab Workspace V4` | `PMDBS Single-cell RNAseq Collection V3` | `supported` |
| `case_studies/SN_CellType_Annotation` | `cohort-pmdbs-sc-rnaseq` | `PMDBS` | `ASAP CRN Learning Lab Workspace V4` | `PMDBS Single-cell RNAseq Collection V3` | `supported` | 


---

## Workspace Guidance

Use the workspace and data collection links above as the recommended starting point for this release.

General guidance:
- prefer the workspace listed for the current release
- prefer the most up-to-date data collection listed for the tutorial or dataset
- if multiple workspaces are listed, choose the one aligned to your dataset or workflow
- older releases may remain documented for reference but are not actively maintained

