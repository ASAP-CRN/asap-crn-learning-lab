# CRN Cloud Rosetta Stone

The Rosetta Stone helps you find datasets, understand curation history, and locate the right bucket paths for each release.

## Pages

| Page | Purpose |
| ---- | ------- |
| [Dataset Finder](datasets.md) | Search and filter all datasets. View curation details, release history, and bucket paths. |
| [Collection Manifest](collections.md) | Review which datasets belong to each collection and where files resolve per release. |
| [Release View](releases.md) | See what changed in each release — added, updated, and unchanged datasets. |

## Curation status legend


<div class="rs-legend">
  <span class="rs-legend-title">Curation status:</span>
  <span class="rs-legend-item"><span class="rs-badge rs-badge--added"
    style="display:inline-flex;align-items:center;font-size:0.72rem;padding:2px 8px;border-radius:3px;font-weight:500;white-space:nowrap;font-family:monospace;background:#e8f5ee;color:#0d6b3f;border:1px solid #6fcf97">
    <span style="display:inline-block;width:6px;height:6px;border-radius:50%;background:#0d6b3f;margin-right:4px;vertical-align:middle"></span>added</span>
    — first appeared in this release</span>
  <span class="rs-legend-item"><span class="rs-badge rs-badge--updated"
    style="display:inline-flex;align-items:center;font-size:0.72rem;padding:2px 8px;border-radius:3px;font-weight:500;white-space:nowrap;font-family:monospace;background:#e8f0fb;color:#1a4fa0;border:1px solid #7baee8">
    <span style="display:inline-block;width:6px;height:6px;border-radius:50%;background:#1a4fa0;margin-right:4px;vertical-align:middle"></span>updated</span>
    — new or changed curated outputs</span>
  <span class="rs-legend-item"><span class="rs-badge rs-badge--unchanged"
    style="display:inline-flex;align-items:center;font-size:0.72rem;padding:2px 8px;border-radius:3px;font-weight:500;white-space:nowrap;font-family:monospace;background:#f0eeea;color:#5a5850;border:1px solid #bbb9b0">
    <span style="display:inline-block;width:6px;height:6px;border-radius:50%;background:#5a5850;margin-right:4px;vertical-align:middle"></span>unchanged</span>
    — included but files resolve to an earlier release</span>
  <span class="rs-legend-item"><span class="rs-badge rs-badge--not-curated"
    style="display:inline-flex;align-items:center;font-size:0.72rem;padding:2px 8px;border-radius:3px;font-weight:500;white-space:nowrap;font-family:monospace;background:#fef3e2;color:#8a5a00;border:1px solid #f0b429">
    <span style="display:inline-block;width:6px;height:6px;border-radius:50%;background:#8a5a00;margin-right:4px;vertical-align:middle"></span>not curated</span>
    — no curation outputs for this release</span>
</div>


## Key concepts

**Release** — the CRN Cloud release in which a dataset's curated files were last produced. If a dataset is unchanged in the latest release, its files may still resolve to an earlier release path.

**Collection version** — a versioned snapshot of a collection. A single collection version can include datasets whose files were materialized in different releases.

**Bucket paths** — `prod` contains curated outputs; `raw` contains unprocessed source files.
