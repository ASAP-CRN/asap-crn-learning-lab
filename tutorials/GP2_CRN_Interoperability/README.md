# GP2 × CRN Interoperability

Link ASAP CRN PMDBS sc/snRNA-seq samples to GP2 participants, and add GP2 study, phenotype, and genetic data availability (NBA, WGS) to each CRN sample. This is the first step toward analyses that combine CRN single-cell data with GP2 genetics.

**Notebook:** [`GP2_ASAPCRN_Interoperability.ipynb`](GP2_ASAPCRN_Interoperability.ipynb)
**Built in:** [GP2 × ASAP CRN Verily Workbench workspace](https://workbench.verily.com/workspaces/gp2)

> ⚠️ **Built for the PMDBS sc/snRNA-seq collection and GP2 release 12.** Other CRN datasets or GP2 releases may use different file names, column names, or ID formats, so you may need to edit the notebook. The most likely places to change are the GP2 release and file paths (Section 1), the GP2 ID cleaning (Section 2), the brain bank to GP2 study map (Section 2.2), and the GP2 column renames (Section 3).

## What you'll learn
- How CRN samples connect to GP2 participants through the GP2 ID
- How to clean IDs and join two programs' metadata without duplicating samples
- How to check how many samples matched, and follow up on IDs that didn't
- Which matched participants have GP2 array (NBA) and whole genome (WGS) data

## Before you begin
- **Data access:** approved access to both CRN Cloud and GP2 Tier 2 data. For GP2 workspace access, contact [pm@gp2.org](mailto:pm@gp2.org).
- **Workspace:** the [GP2 × ASAP CRN workspace](https://workbench.verily.com/workspaces/gp2), or a duplicate of it, with these resources:
  - `ASAPCRN_PMDBS_scRNAseq/pmdbs-sc-rnaseq-v3`
  - `GP2_Tier2/gp2_tier2_eu_release12`
- **Prerequisite:** run [Metadata_Assembly](../Metadata_Assembly/) for `cohort-pmdbs-sc-rnaseq` first. This notebook reads its cleaned metadata table.
- **App:** the default JupyterLab app. The notebook only needs pandas and numpy, which are preinstalled.

## How to run
1. Run the [Metadata_Assembly](../Metadata_Assembly/) notebook for the PMDBS cohort.
2. Open `GP2_CRN_Interoperability.ipynb` in a JupyterLab app.
3. Check the paths in Section 1:
   ```python
   GP2_RELEASE = "release12"
   CRN_METADATA_PATH = (WS_ROOT / "ws_files" / "crn_metadata" / "cohort-pmdbs-sc-rnaseq"
                        / "cohort-pmdbs-sc-rnaseq_cleanedmetadata.csv")
   ```
4. Select **Run > Run All Cells**.
5. Review the checks in Section 5, especially the unmatched IDs.

Before running, read the GP2 release README in `gp2_tier2_eu_release12`. It lists sample counts, QC thresholds, and ancestry definitions, which change every release.

## Notebook sections
| Section | What it does |
|---|---|
| 1. Setup | Sets the GP2 release and paths |
| 2. Load CRN Metadata | Loads the cleaned CRN table, cleans GP2 IDs, and reports GP2 ID coverage |
| 3. Load the GP2 Master Key | Collapses the master key to one row per GP2 ID and prefixes its columns with `gp2_` |
| 4. Join GP2 onto CRN | Joins the two tables and labels each sample's match status |
| 5. Checks | Lists unmatched IDs, compares brain bank vs GP2 study, and counts NBA and WGS availability |
| 6. Save Outputs | Saves the joined table and check results |

## Outputs
Saved to `ws_files/GP2xASAPCRN/interoperability/`:

| File | Description |
|---|---|
| `joined_ASAPCRN-GP2_metadata.csv` | CRN metadata with GP2 master columns added (prefixed `gp2_`) |
| `gp2_coverage.csv` | CRN samples and subjects with a GP2 ID |
| `gp2_match_summary.csv` | Samples by match status |
| `gp2_unmatched_ids.csv` | CRN GP2 IDs not found in the GP2 master key, for follow-up |
| `gp2_master_conflicts.csv` | GP2 IDs whose master key rows disagree (only written if there are any) |

**Match status**

| Status | Meaning |
|---|---|
| `matched` | The CRN GP2 ID is in the GP2 master key |
| `not_in_gp2_master` | CRN has a GP2 ID, but it isn't in this GP2 release |
| `no_gp2_id` | CRN has no GP2 ID for the sample |

## Key decisions
- **ID cleaning:** CRN GP2 IDs are trimmed, uppercased, and stripped of sample suffixes (`_s1`, `_S2`, ...) so they point to the person, matching the GP2 master format.
- **One row per GP2 participant:** some participants have more than one master key row (for example, separate NBA and WGS records). These are collapsed first so the join doesn't duplicate CRN samples. A participant has NBA or WGS data if any of their rows says so; other fields keep the first non-empty value, and disagreements are logged.
- **Every CRN sample is kept:** the join is a left join, checked so that each sample matches at most one GP2 participant and no rows are added or lost.
- **Column naming:** unprefixed columns come from CRN, and `gp2_` columns come from the GP2 master key. CRN's own copy of the GP2 phenotype is renamed `crn_gp2_phenotype` to avoid confusion.
- **Brain bank map:** the CRN brain bank to GP2 study map is only a cross-check. The GP2 master key is the authoritative source for study.

## Data use
Outputs contain individual-level GP2 Tier 2 data. Keep them in your workspace, follow your GP2 data use agreement, and clear notebook outputs before committing to GitHub.

## Tested with
CRN Cloud v5.0.0 (`cohort-pmdbs-sc-rnaseq`) and GP2 release 12. See [RELEASE_COMPATIBILITY.md](../../RELEASE_COMPATIBILITY.md).

## Resources
- [GP2 code and pipelines](https://github.com/GP2code)
- [GP2 training materials](https://gp2.org/training)
- [CRN Cloud Data Dictionary](https://storage.googleapis.com/asap-public-assets/wayfinding/ASAP-CRN-Cloud-Data-Dictionary.pdf)

## Contact
- **CRN Cloud data:** [cloud@parkinsonsroadmap.org](mailto:cloud@parkinsonsroadmap.org)
- **GP2 workspace access:** [pm@gp2.org](mailto:pm@gp2.org)
- **GP2 release availability:** [admin@gp2.org](mailto:admin@gp2.org)
- **GP2 Office Hours:** Tuesdays at 11 AM ET, [meet.google.com/jdg-rmav-pwt](https://meet.google.com/jdg-rmav-pwt)
