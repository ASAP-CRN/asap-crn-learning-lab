!!!warning "Work In Progress Section"

# CRN Cloud Rosetta Stone

The **CRN Cloud Rosetta Stone** helps you understand how datasets, collections, releases, and bucket paths fit together across CRN Cloud versions.

Use this section when you need to:

* Find a dataset and its current curated outputs
* Check which datasets are included in a collection
* Understand what changed between CRN Cloud releases
* Locate the correct GCS bucket path for a dataset or release
* Trace curation history across dataset, collection, and release versions

## Pages

| Page                                  | Purpose                                                                                                    |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| [Dataset Finder](datasets.md)         | Search and filter datasets. View dataset versions, curation details, release history, and bucket paths.    |    |
| [Release View](releases.md)           | See what changed in each CRN Cloud release, including added, updated, unchanged, and not curated datasets. |

## Curation Status Legend

Curation status describes how a dataset relates to a specific CRN Cloud release.

<div class="rs-legend">
  <span class="rs-legend-title">Curation status:</span>
  <span class="rs-legend-item"><span class="rs-badge rs-badge--added"
    style="display:inline-flex;align-items:center;font-size:0.72rem;padding:2px 8px;border-radius:3px;font-weight:500;white-space:nowrap;font-family:monospace;background:#e8f5ee;color:#0d6b3f;border:1px solid #6fcf97">
    <span style="display:inline-block;width:6px;height:6px;border-radius:50%;background:#0d6b3f;margin-right:4px;vertical-align:middle"></span>added</span>
    — first appeared in this release</span>
  <span class="rs-legend-item"><span class="rs-badge rs-badge--updated"
    style="display:inline-flex;align-items:center;font-size:0.72rem;padding:2px 8px;border-radius:3px;font-weight:500;white-space:nowrap;font-family:monospace;background:#e8f0fb;color:#1a4fa0;border:1px solid #7baee8">
    <span style="display:inline-block;width:6px;height:6px;border-radius:50%;background:#1a4fa0;margin-right:4px;vertical-align:middle"></span>updated</span>
    — new or changed curated outputs were produced</span>
  <span class="rs-legend-item"><span class="rs-badge rs-badge--unchanged"
    style="display:inline-flex;align-items:center;font-size:0.72rem;padding:2px 8px;border-radius:3px;font-weight:500;white-space:nowrap;font-family:monospace;background:#f0eeea;color:#5a5850;border:1px solid #bbb9b0">
    <span style="display:inline-block;width:6px;height:6px;border-radius:50%;background:#5a5850;margin-right:4px;vertical-align:middle"></span>unchanged</span>
    — included in this release, but files resolve to an earlier release path</span>
  <span class="rs-legend-item"><span class="rs-badge rs-badge--not-curated"
    style="display:inline-flex;align-items:center;font-size:0.72rem;padding:2px 8px;border-radius:3px;font-weight:500;white-space:nowrap;font-family:monospace;background:#fef3e2;color:#8a5a00;border:1px solid #f0b429">
    <span style="display:inline-block;width:6px;height:6px;border-radius:50%;background:#8a5a00;margin-right:4px;vertical-align:middle"></span>not curated</span>
    — no curated outputs are available for this dataset in this release</span>
</div>

## Key Concepts

**CRN Cloud Release**
A platform-wide release that captures which datasets, collections, curated outputs, and documentation are supported at a point in time. A release may include datasets whose curated files were produced in the current release or in an earlier release.

**Dataset Version**
The version of an individual dataset. Dataset versions change when the dataset content changes, such as metadata updates, added samples, or changes to underlying data.

**Collection Version**
The version of a grouped set of related datasets, such as a harmonized collection. A single collection version can include datasets whose files were materialized in different CRN Cloud releases.

**Curation Status**
A release-specific label that tells you whether a dataset was newly added, updated, unchanged, or not curated in that release.

**Bucket Paths**
Google Cloud Storage paths where files are stored.

* `prod` paths contain curated outputs.
* `raw` paths contain unprocessed source files.
* Some datasets in a current release may still point to curated files from an earlier release if their outputs did not change.

## How to Use the Rosetta Stone

Use the **Dataset Finder** when you know the dataset name and want to find its versions, curation history, and bucket paths.

Use the **Release View** when you want to understand what changed between CRN Cloud releases.

!!! tip "Version numbers are not interchangeable"
Dataset versions, collection versions, CRN Cloud releases, CDE schema versions, and pipeline versions track different things. Always check which version type you are using before citing, downloading, or comparing data. For definitions on the types of versions, refer to the [Glossary](../glossary.md)
