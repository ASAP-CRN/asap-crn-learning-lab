# Release Compatibility

This document tracks compatibility between the Learning Lab repository and major CRN data releases.

It is intended to help users identify:
- which CRN release is currently supported in this repo
- which datasets and tutorials are aligned to that release
- the recommended Verily Workbench workspaces and data collections to use

## Current Supported Release

**Current CRN Release:** `v4`  
**Status:** `current`  
**Validated on:** `2026-04-24`  
**Repo tag:** `crn-v4`

### Recommended Verily Workbench Resources

| Resource Type | Name | Purpose | Link | Notes |
|---------------|------|---------|------|-------|
| Workspace | `ASAP CRN Learning Lab Workspace` | Primary recommended workspace for current tutorials | [`https://workbench.verily.com/workspaces/asap-crn-learning-lab-ws-v4`](https://workbench.verily.com/workspaces/asap-crn-learning-lab-ws-v4)| 
| Data Collection | `ASAP CRN Harmonized Data Collection` | Current recommended CRN data collection for this release | [`https://workbench.verily.com/exchange/asap-crn-pmdbs-scrnaseq-collection`](https://workbench.verily.com/exchange/asap-crn-pmdbs-scrnaseq-collection) |

---

## Release Summary

| CRN Release | Repo Tag | Status | Validated On | Notes |
|-------------|----------|--------|--------------|-------|
| `v4` | `crn-v4` | `current` | `2026-04-24` | `compatible with v4 release of asap-crn` |

---

## Tutorials by Release

### CRN Release `v4`

#### Supported tutorials

| Tutorial / Notebook | Dataset(s) | Collection | Workspace | Data Collection | Status | Notes |
|---------------------|------------|------------|-----------|-----------------|--------|-------|
| `tutorials/00_pilot_workshop` | `asap-curated-cohort-pmdbs-sc-rnaseq` | `PMDBS` | `ASAP CRN Learning Lab Workspace` | `ASAP CRN Harmonized Data Collection` | `supported` |
| `tutorials/Sample_Notebooks` | `asap-curated-cohort-pmdbs-sc-rnaseq` | `PMDBS` | `ASAP CRN Learning Lab Workspace` | `ASAP CRN Harmonized Data Collection` | `supported` |
| `case_studies/SN_CellType_Annotation` | `asap-curated-cohort-pmdbs-sc-rnaseq` | `PMDBS` | `ASAP CRN Learning Lab Workspace` | `ASAP CRN Harmonized Data Collection` | `supported` |


---

## Workspace Guidance

Use the workspace and data collection links above as the recommended starting point for this release.

General guidance:
- prefer the workspace listed for the current release
- prefer the most up-to-date data collection listed for the tutorial or dataset
- if multiple workspaces are listed, choose the one aligned to your dataset or workflow
- older releases may remain documented for reference but are not actively maintained

