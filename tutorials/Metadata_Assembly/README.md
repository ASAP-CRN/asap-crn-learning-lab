# Metadata Assembly

Build one cleaned, sample-level metadata table for a CRN Cloud cohort by merging its SAMPLE, SUBJECT, and CLINPATH tables. Use the output as the starting point for any analysis that needs sample, subject, and clinical metadata in one place.

**Notebook:** [`Assembling_CRN_Metadata.ipynb`](Assembling_CRN_Metadata.ipynb)
**Built in:** [GP2 × ASAP CRN Verily Workbench workspace](https://workbench.verily.com/workspaces/gp2)

> ⚠️ **Built for the PMDBS sc/snRNA-seq collection.** This notebook was developed and tested on the `pmdbs-sc-rnaseq` datasets. Other dataset types may have different tables, column names, or duplicate patterns, so you may need to edit it. The most likely places to change are the SUBJECT columns list (Section 4), the CLINPATH ID columns (Section 5), and `MISSING_LABELS` (Section 3). Check the duplicate check in Section 5.1 and the summary in Section 7 to confirm the results make sense for your data.

## What you'll learn
- How CRN Cloud metadata tables relate to each other (sample → subject → clinical data)
- How to find and combine duplicate records without losing information
- How to check merges so no samples are added or lost
- How to review the records where duplicate submissions disagree

## Before you begin
- **Workbench access:** a Verily Workbench account with a billing pod. See the [Getting Started guide](https://asap-crn.github.io/asap-crn-learning-lab/getting-started/).
- **Workspace:** duplicate the [GP2 × ASAP CRN workspace](https://workbench.verily.com/workspaces/gp2), or use any workspace with a CRN Cloud cohort mounted as a resource.
- **Data:** a cohort with SAMPLE, SUBJECT, and CLINPATH tables in its `metadata/` folder. Tested on the PMDBS sc/snRNA-seq collection; see the note at the top for other dataset types.
- **App:** the default JupyterLab app. The notebook only needs pandas and numpy, which are preinstalled.

## How to run
1. Open `Assembling_CRN_Metadata.ipynb` in a JupyterLab app.
2. Edit the **parameters block** in Section 1 for your cohort:
   ```python
   COLLECTION = "ASAPCRN_PMDBS_scRNAseq"   # resource folder in the workspace
   DATASET    = "pmdbs-sc-rnaseq-v3"
   COHORT     = "cohort-pmdbs-sc-rnaseq"
   RELEASE    = "v5.0.0"                   # CRN Cloud release, for your records
   ```
3. Select **Run > Run All Cells**. 
4. Review the conflicts in Section 8 before using disputed fields in an analysis.

## Notebook sections
| Section | What it does |
|---|---|
| 1. Setup | Sets the cohort and paths |
| 2. Load Metadata Tables | Loads SAMPLE, SUBJECT, and CLINPATH |
| 3. Helper Functions | Standardizes missing values and combines duplicate records |
| 4. Merge SAMPLE with SUBJECT | Adds demographics to each sample |
| 5. Merge with CLINPATH | Checks CLINPATH duplicates, combines them per person, and adds clinical fields |
| 6. Final Cleanup | Standardizes missing values and drops empty columns |
| 7. Save Outputs and Summary | Checks the final table and saves all outputs |
| 8. Extra Investigation of Conflicts | Sorts each CLINPATH conflict by type |
| 9. Summary and Next Steps | What to do with the outputs |

## Outputs
Saved to `ws_files/crn_metadata/<cohort>/`:

| File | Description |
|---|---|
| `<cohort>_cleanedmetadata.csv` | One row per sample per dataset |
| `subject_conflicts.csv` | SUBJECT fields where duplicate records disagreed, with the value kept |
| `clinpath_conflicts.csv` | CLINPATH fields where duplicate records disagreed, with the value kept |
| `clinpath_selection_ties.csv` | Subjects with more than one equally complete record |
| `clinpath_conflicts_review.csv` | CLINPATH conflicts sorted by type: formatting only, or a real disagreement between or within datasets |

`ws_files` is shared across apps and users in the workspace, so outputs persist between sessions.

## Key decisions
- **Unique key:** a sample can appear in more than one dataset, so rows are unique on `ASAP_dataset_id` + `ASAP_sample_id`. Join to other data on both IDs, and count people with `ASAP_subject_id`.
- **SUBJECT** is deduplicated within each dataset. **CLINPATH** is deduplicated per person, because the same person can be submitted under more than one dataset.
- **Duplicates:** records that each hold part of the data are combined into one. When values disagree, the value from the most complete record is kept and the disagreement is logged. No values are changed silently.
- **Missing values:** blank strings and labels like `NA`, `NULL`, `Unknown`, and `Not Reported` become empty values. To keep `Unknown` as a real answer, remove it from `MISSING_LABELS` in Section 3.
- **Synonyms:** `VOCAB_MAPS` in Section 5.2 merges confirmed synonyms before collapsing. It's empty by default.

## Data use
Outputs contain subject-level clinical data. Keep them in your workspace, share conflict reports within the program only, and clear notebook outputs before committing to GitHub.

## Tested with
CRN Cloud v5.0.0, cohort `cohort-pmdbs-sc-rnaseq`. See [RELEASE_COMPATIBILITY.md](../../RELEASE_COMPATIBILITY.md).

## Used by
- [GP2_CRN_Interoperability](../GP2_CRN_Interoperability/): links these samples to GP2 participants and their genetic data

## Contact
Questions about CRN Cloud data: [cloud@parkinsonsroadmap.org](mailto:cloud@parkinsonsroadmap.org)