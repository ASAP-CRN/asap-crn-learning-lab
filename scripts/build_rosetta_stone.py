"""
build_rosetta_stone.py

Generates the data-driven Rosetta Stone pages:
  docs/rosetta-stone/datasets.md
  docs/rosetta-stone/collections.md
  docs/rosetta-stone/releases.md

docs/rosetta-stone/index.md is written by hand and is never touched.

Data comes from the cloud-datasets, cloud-releases and cloud-collections repos,
read through crn_rosetta.Catalog. By default they are expected as sibling
directories of this repo:

  python scripts/build_rosetta_stone.py
  python scripts/build_rosetta_stone.py --data-root /path/to/parent/of/cloud-repos
  python scripts/build_rosetta_stone.py --github              # no clones needed
"""

import argparse
import sys
from collections import Counter
from pathlib import Path

# Allow running from repo root or scripts/ directory
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from crn_rosetta import Catalog, version_key
from rosetta_helpers import (
    DATASETS_REPO_URL, NA_HTML, LEGEND_HTML, STATUS_CFG, STATUS_ORDER,
    esc, safe_id, doi_link, doi_link_or, mono,
    dataset_anchor, dataset_href,
    curation_badge_html, status_counts_html, change_badge_html,
    collection_version_doi,
    render_curation_card, render_bucket_card,
    render_full_history_table, render_curation_history_table,
    build_select,
)


def find_repo_root(start: Path) -> Path:
    for p in [start] + list(start.parents):
        if (p / "mkdocs.yml").exists():
            return p
    raise FileNotFoundError("mkdocs.yml not found. Run from inside the Learning Lab repo.")


# ─────────────────────────────────────────────────────────────────────────────
# ① datasets.md
# ─────────────────────────────────────────────────────────────────────────────

def _tags(ds) -> list:
    return sorted(ds.keywords, key=str.lower)


def _render_meta_strip(dataset_doi, license_val, col_name, col_doi, ds_version):
    def item(label, value, extra_cls=""):
        return (
            f'<div class="rs-meta-item">'
            f'<span class="rs-meta-label">{label}</span>'
            f'<span class="rs-meta-value {extra_cls}">{value}</span>'
            f'</div>'
        )

    return (
        '<div class="rs-meta-strip">'
        + item("License",        esc(license_val) or "TBD")
        + item("Dataset DOI",    doi_link(dataset_doi) or "TBD")
        + item("Collection",     esc(col_name) if col_name else NA_HTML, "" if col_name else "rs-na")
        + item("Collection DOI", doi_link(col_doi) if col_doi else NA_HTML, "" if col_doi else "rs-na")
        + item("Latest version", f'<span class="rs-mono">{esc(ds_version)}</span>')
        + '</div>'
    )


def build_datasets_page(cat: Catalog) -> str:
    datasets = cat.datasets()
    releases_newest = list(reversed(cat.release_versions))
    cde_opts = sorted({r.cde_version for r in cat.releases() if r.cde_version},
                      key=version_key, reverse=True)
    collection_opts = sorted({d.collection for d in datasets if d.collection}, key=str.lower)
    all_tags = sorted({t for d in datasets for t in _tags(d)}, key=str.lower)

    tag_opts = ['<option value="">All tags</option>']
    for t in all_tags:
        tag_opts.append(f'<option value="{esc(t.lower())}">{esc(t)}</option>')

    guidance_html = (
        '<div class="rs-guidance">'
        '<p class="rs-guidance-intro">Find datasets, review curation details, and copy bucket paths.</p>'
        '<div class="rs-guidance-steps">'
        '<div class="rs-guidance-step"><span class="rs-guidance-num">1</span>'
        '<span>Search by dataset ID, title, keyword, DOI, or bucket path.</span></div>'
        '<div class="rs-guidance-step"><span class="rs-guidance-num">2</span>'
        '<span>Filter by release or CDE version (datasets included in it), collection, or tag.</span></div>'
        '<div class="rs-guidance-step"><span class="rs-guidance-num">3</span>'
        '<span>Click <strong>View</strong> to see curation details, bucket paths, and release history.</span></div>'
        '</div>'
        '<p class="rs-table-hint"><strong>Curated in</strong> is the release whose path holds a '
        'dataset\'s current curated outputs. It can be older than the latest release when the '
        'outputs have not changed since.</p>'
        '</div>'
    )

    def _legend_item(status):
        label, bg, color, border, description = STATUS_CFG[status]
        return (
            f'<div class="rs-legend-card">'
            f'<span class="rs-legend-badge" style="background:{bg};color:{color};border-color:{border}">'
            f'<span style="display:inline-block;width:6px;height:6px;border-radius:50%;'
            f'background:{color};margin-right:5px;vertical-align:middle"></span>'
            f'{label}</span>'
            f'<span class="rs-legend-desc">{description}</span>'
            f'</div>'
        )

    legend_html = (
        '<div class="rs-legend-section">'
        '<div class="rs-legend-section-header">'
        '<span class="rs-legend-section-title">Curation status</span>'
        '</div>'
        '<div class="rs-legend-grid">'
        + "".join(_legend_item(s) for s in STATUS_ORDER)
        + '</div>'
        '</div>'
    )

    filter_bar = (
        '<div class="rs-filters">'
        f'<input id="rsSearch" class="rs-search" type="text"'
        f' placeholder="Search by dataset ID, title, keyword, DOI, or bucket path…">'
        + build_select("rsReleaseFilter",    "releases",     releases_newest)
        + build_select("rsCdeFilter",        "CDE versions", cde_opts)
        + build_select("rsCollectionFilter", "collections",  collection_opts)
        + f'<select id="rsTagFilter" class="rs-filter-select" aria-label="Filter by tag">'
        + "".join(tag_opts)
        + '</select>'
        + '<div class="rs-filter-actions">'
        + '<button id="rsClearFilters" class="rs-btn rs-btn--clear">Clear filters</button>'
        + '</div>'
        + '</div>'
    )

    header_md = "\n".join([
        "# Dataset Finder",
        "",
    ])

    body_parts = [
        '<div class="rs-page-body">',
        guidance_html,
        legend_html,
        filter_bar,
        '<p id="rsCount" class="rs-count"></p>',
        '<table class="rs-table rs-dataset-table" id="rsDatasetTable">',
        "<thead><tr>",
        '<th class="sortable" data-col="0">Dataset <i class="rs-sort-icon">⇅</i></th>',
        '<th class="sortable" data-col="1">Title <i class="rs-sort-icon">⇅</i></th>',
        '<th class="sortable" data-col="2">Collection <i class="rs-sort-icon">⇅</i></th>',
        '<th class="sortable" data-col="3">Dataset<br>version <i class="rs-sort-icon">⇅</i></th>',
        '<th class="sortable" data-col="4">Curated<br>in <i class="rs-sort-icon">⇅</i></th>',
        '<th class="sortable" data-col="5">Collection<br>version <i class="rs-sort-icon">⇅</i></th>',
        "<th>Details</th>",
        "</tr></thead>",
        "<tbody>",
    ]
    drawers = []

    for idx, ds in enumerate(datasets):
        tags       = _tags(ds)
        rec        = cat.curation(ds)
        collection = cat.collection(ds.collection) if ds.collection in cat.collection_names else None
        col_ver    = collection.version if collection else ""
        col_doi    = collection.doi if collection else ""
        included   = cat.releases_including(ds)
        cde_seen   = list(dict.fromkeys(cat.release(v).cde_version for v in included))
        paths      = cat.paths(ds)

        search_text = " ".join([
            ds.name, ds.title, ds.description, ds.collection or "",
            ds.version, col_ver, col_doi, ds.doi,
            " ".join(tags), " ".join(included), " ".join(ds.all_versions),
            " ".join(v for k, v in ds.buckets.items() if k in ("prod", "raw")),
            " ".join(
                f"{r.workflow} {r.workflow_version} {r.collection_version} "
                f"{collection_version_doi(cat, r)} {r.dataset_bucket} {r.collection_bucket}"
                for r in ds.curation.values()
            ),
        ]).lower()

        anchor    = dataset_anchor(ds.name)
        detail_id = f"rs-detail-{safe_id(ds.name)}-{idx}"

        # ── Summary row — View button opens side drawer
        body_parts.append(
            f'<tr id="{esc(anchor)}" class="rs-dataset-row"'
            f' data-detail="{esc(detail_id)}"'
            f' data-search="{esc(search_text)}"'
            f' data-tags="{esc("||".join(t.lower() for t in tags))}"'
            f' data-release="{esc("||".join(included))}"'
            f' data-cde="{esc("||".join(cde_seen))}"'
            f' data-collection="{esc(ds.collection or "")}">'
            f'<td><code>{esc(ds.name)}</code></td>'
            f'<td>{esc(ds.title)}</td>'
            f'<td>{esc(ds.collection or "—")}</td>'
            f'<td>{esc(ds.version or "—")}</td>'
            f'<td>{esc(rec.release if rec else "—")}</td>'
            f'<td>{esc(col_ver or "—")}</td>'
            f'<td><button class="rs-toggle" data-target="{esc(detail_id)}" onclick="rsOpenDrawer(this)">View</button></td>'
            f'</tr>'
        )

        # ── Side drawer — appended after the table, shown/hidden via JS
        tags_html = (
            " ".join(f'<span class="rs-tag-pill">{esc(t)}</span>' for t in tags)
            if tags else NA_HTML
        )
        source_url = f"{DATASETS_REPO_URL}/{ds.name}/dataset.json"

        drawers.append(
            f'<div id="{esc(detail_id)}" class="rs-drawer" role="dialog" aria-label="{esc(ds.title)}">'
            f'<div class="rs-drawer-inner">'
            f'<div class="rs-drawer-header">'
            f'<div>'
            f'<div class="rs-drawer-title">{esc(ds.title)}</div>'
            f'<div class="rs-detail-id">{esc(ds.name)}</div>'
            f'</div>'
            f'<button class="rs-drawer-close" onclick="rsCloseDrawer(this)" aria-label="Close">✕</button>'
            f'</div>'
            f'<div class="rs-drawer-body">'
            f'<div class="rs-tag-row">{tags_html}</div>'
            + _render_meta_strip(ds.doi, ds.license, ds.collection, col_doi, ds.version)
            + f'<div class="rs-section"><div class="rs-section-header">Description</div>'
            f'<p class="rs-description">{esc(ds.description) if ds.description else "TBD"}</p></div>'
            + f'<div class="rs-panel-sections">'
            f'{render_curation_card(cat, ds)}{render_bucket_card(paths)}'
            f'</div>'
            + render_curation_history_table(cat, ds)
            + render_full_history_table(cat, ds)
            + f'<div class="rs-section"><div class="rs-section-header">Source</div>'
            f'<div class="rs-field">'
            f'<span class="rs-field-label">Detail JSON</span>'
            f'<span class="rs-field-value rs-mono" style="font-size:0.7rem">'
            f'<a href="{esc(source_url)}" target="_blank" rel="noopener">'
            f'cloud-datasets/datasets/{esc(ds.name)}/dataset.json ↗</a></span></div></div>'
            f'</div>'  # drawer-body
            f'</div>'  # drawer-inner
            f'</div>'  # drawer
        )

    body_parts += ["</tbody>", "</table>"]
    # Overlay backdrop (hidden by default, shown when a drawer is open)
    body_parts.append('<div id="rsDrawerOverlay" class="rs-drawer-overlay" onclick="rsCloseAllDrawers()"></div>')
    body_parts += drawers
    body_parts.append("</div>")  # close rs-page-body
    return header_md + "\n".join(body_parts)


# ─────────────────────────────────────────────────────────────────────────────
# ② collections.md
# ─────────────────────────────────────────────────────────────────────────────

def _dataset_cell(name: str) -> str:
    return f'<td><a href="{esc(dataset_href(name))}"><code>{esc(name)}</code></a></td>'


def _details_cell(name: str) -> str:
    return f'<td><a href="{esc(dataset_href(name))}">→ details</a></td>'


def build_collections_page(cat: Catalog) -> str:
    latest = cat.latest_release

    header_md = "\n".join([
        "# Collection Manifest",
        "",
        "Each section below lists the datasets in a collection and shows where each "
        "dataset's curated files were last materialized.",
        "",
    ])

    body = ['<div class="rs-page-body">']
    body.append(
        '<div class="rs-collection-note">'
        "A collection version may include datasets that were last materialized in different "
        "CRN Cloud releases. If a dataset was unchanged in the latest release, its metadata, "
        "file metadata, and curated outputs may still resolve to an earlier release path. "
        f"Curation status below is as of release {esc(latest)}."
        '</div>'
    )
    body.append(LEGEND_HTML)

    def render_collection_section(col) -> str:
        members = cat.collection_members(col.name)
        counts  = Counter(cat.status(ds) or "not-curated" for ds in members)

        meta_parts = []
        if col.version:
            meta_parts.append(f'<span>Current version: <span class="rs-mono">{esc(col.version)}</span></span>')
        if col.doi:
            meta_parts.append(f'<span>Collection DOI: {doi_link(col.doi)}</span>')
        if col.release:
            meta_parts.append(f'<span>Latest release: <span class="rs-mono">{esc(col.release)}</span></span>')
        meta_parts.append(f'<span>{len(members)} dataset{"" if len(members) == 1 else "s"}</span>')

        sec_html = (
            f'<h2 id="col-{esc(safe_id(col.name))}">{esc(col.title)}</h2>'
            f'<div class="rs-collection-header">'
            f'<span class="rs-collection-header-name rs-mono">{esc(col.name)}</span>'
            f'<span class="rs-collection-header-meta">{"".join(meta_parts)}</span>'
            f'<div class="rs-status-counts">{status_counts_html(counts)}</div>'
            f'</div>'
            f'<div style="overflow-x:auto">'
            f'<table class="rs-table rs-collection-table">'
            f'<thead><tr>'
            f'<th>Dataset</th><th>Dataset version</th><th>Curation status</th>'
            f'<th>Curated in</th><th>Collection version<br>when curated</th>'
            f'<th>Workflow version</th><th>Dataset DOI</th><th>Details</th>'
            f'</tr></thead><tbody>'
        )
        for ds in members:
            rec = cat.curation(ds)
            sec_html += (
                f'<tr>'
                + _dataset_cell(ds.name)
                + f'<td>{mono(ds.version)}</td>'
                f'<td>{curation_badge_html(cat.status(ds) or "not-curated")}</td>'
                f'<td>{mono(rec.release if rec else "")}</td>'
                f'<td>{mono(rec.collection_version if rec else "")}</td>'
                f'<td>{mono(rec.workflow_version if rec else "")}</td>'
                f'<td>{doi_link_or(ds.doi, "—")}</td>'
                + _details_cell(ds.name)
                + f'</tr>'
            )
        if not members:
            sec_html += '<tr><td colspan="8">No datasets listed.</td></tr>'
        sec_html += '</tbody></table></div>'

        if col.versions:
            rows = "".join(
                f'<tr>'
                f'<td><span class="rs-mono">{esc(v.version)}</span>'
                f'{" " + _latest_pill() if v.version == col.version else ""}</td>'
                f'<td>{mono(v.release)}</td>'
                f'<td>{mono(v.cde_version)}</td>'
                f'<td>{doi_link_or(v.doi, "—")}</td>'
                f'<td>{len(v.datasets)}</td>'
                f'</tr>'
                for v in reversed(list(col.versions.values()))
            )
            sec_html += (
                '<div class="rs-section rs-collection-versions">'
                '<div class="rs-section-header">Version history</div>'
                '<div class="rs-card rs-card--table">'
                '<table class="rs-mini-table">'
                '<thead><tr><th>Collection version</th><th>Published with release</th>'
                '<th>CDE version</th><th>Version DOI</th><th>Datasets</th></tr></thead>'
                f'<tbody>{rows}</tbody>'
                '</table></div></div>'
            )
        return sec_html

    def _latest_pill() -> str:
        return '<span class="rs-latest-badge">current</span>'

    for col in cat.collections():
        body.append(render_collection_section(col))

    uncollected = [ds for ds in cat.datasets() if not ds.collection]
    if uncollected:
        unc_html = (
            '<h2 id="uncollected">Uncollected datasets</h2>'
            '<p style="font-size:0.85rem;margin-bottom:0.6rem">These datasets are not assigned to '
            'any collection and have no curated outputs. Their files are in each dataset\'s own bucket.</p>'
            '<div style="overflow-x:auto">'
            '<table class="rs-table">'
            '<thead><tr>'
            '<th>Dataset</th><th>Dataset version</th><th>First released</th>'
            '<th>Dataset DOI</th><th>Details</th>'
            '</tr></thead><tbody>'
        )
        for ds in uncollected:
            unc_html += (
                f'<tr>'
                + _dataset_cell(ds.name)
                + f'<td>{mono(ds.version)}</td>'
                f'<td>{mono(cat.first_release(ds))}</td>'
                f'<td>{doi_link_or(ds.doi, "—")}</td>'
                + _details_cell(ds.name)
                + f'</tr>'
            )
        unc_html += '</tbody></table></div>'
        body.append(unc_html)

    body.append('</div>')
    return header_md + "\n".join(body)


# ─────────────────────────────────────────────────────────────────────────────
# ③ releases.md
# ─────────────────────────────────────────────────────────────────────────────

_RELEASE_TABLE_HEAD = (
    '<thead><tr>'
    '<th>Dataset</th><th>Collection</th><th>Dataset version</th>'
    '<th>Collection version</th><th>Dataset change</th><th>Curation status</th>'
    '</tr></thead>'
)


def _release_row(row: dict) -> str:
    return (
        f'<tr>'
        + _dataset_cell(row["dataset"])
        + f'<td>{esc(row["collection"]) if row["collection"] else NA_HTML}</td>'
        f'<td>{mono(row["dataset_version"])}</td>'
        f'<td>{mono(row["collection_version"])}</td>'
        f'<td>{change_badge_html(row["change"]) or NA_HTML}</td>'
        f'<td>{curation_badge_html(row["status"])}</td>'
        f'</tr>'
    )


def build_releases_page(cat: Catalog) -> str:
    header_md = "\n".join([
        "# Release View",
        "",
        "Datasets grouped by CRN Cloud release, sorted newest first. Each release lists "
        "the datasets that changed in it; datasets carried forward unchanged are folded "
        "underneath. Dataset names link to the Dataset Finder for full detail.",
        "",
    ])

    body = ['<div class="rs-page-body">', LEGEND_HTML]

    for rel in reversed(cat.releases()):
        rows = cat.release_view(rel.version)
        if not rows:
            continue

        counts  = Counter(r["status"] for r in rows)
        changed = [r for r in rows if r["change"] or r["status"] in ("added", "updated")]
        carried = [r for r in rows if r not in changed]

        meta_spans = []
        if rel.cde_version:
            meta_spans.append(f'<span>CDE: <span class="rs-mono">{esc(rel.cde_version)}</span></span>')
        if rel.doi:
            meta_spans.append(f'<span>DOI: {doi_link(rel.doi)}</span>')
        meta_spans.append(f'<span>{len(rows)} datasets</span>')
        meta_spans.append(f'<span>{len(changed)} changed</span>')

        col_note = ""
        if rel.collections:
            col_list = ", ".join(
                f'{esc(name)} <span class="rs-mono">{esc(ref.version)}</span>'
                for name, ref in sorted(rel.collections.items())
            )
            col_note = (
                f'<p style="font-size:0.8rem;margin-bottom:0.6rem;color:var(--md-default-fg-color--light)">'
                f'Collections: {col_list}</p>'
            )

        if changed:
            changed_html = (
                '<table class="rs-table rs-release-table">'
                + _RELEASE_TABLE_HEAD
                + f'<tbody>{"".join(_release_row(r) for r in changed)}</tbody>'
                '</table>'
            )
        else:
            changed_html = '<p class="rs-table-hint">No dataset or curation changes in this release.</p>'

        carried_html = ""
        if carried:
            carried_html = (
                f'<details class="rs-carried">'
                f'<summary>{len(carried)} datasets carried forward unchanged</summary>'
                '<table class="rs-table rs-release-table">'
                + _RELEASE_TABLE_HEAD
                + f'<tbody>{"".join(_release_row(r) for r in carried)}</tbody>'
                '</table>'
                '</details>'
            )

        body.append(
            f'<div class="rs-release-section" id="release-{esc(safe_id(rel.version))}">'
            f'<div class="rs-release-section-header">'
            f'<span class="rs-release-version">{esc(rel.version)}</span>'
            f'<span class="rs-release-meta">{"".join(meta_spans)}</span>'
            f'<div class="rs-status-counts">{status_counts_html(counts)}</div>'
            f'</div>'
            f'<div class="rs-release-section-body">'
            + col_note + changed_html + carried_html
            + '</div></div>'
        )

    body.append('</div>')
    return header_md + "\n".join(body)


# ─────────────────────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────────────────────

def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"Wrote: {path}")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Build the Rosetta Stone pages.")
    parser.add_argument("--data-root", default=None,
                        help="directory holding cloud-datasets, cloud-releases and cloud-collections "
                             "(default: the parent of this repo)")
    parser.add_argument("--github", action="store_true",
                        help="read the three index files from GitHub instead of local clones")
    parser.add_argument("--ref", default="main", help="branch or tag to read with --github")
    args = parser.parse_args(argv)

    root    = find_repo_root(HERE)
    out_dir = root / "docs" / "rosetta-stone"

    if args.github:
        cat = Catalog.from_github(args.ref)
    else:
        cat = Catalog.from_local(args.data_root or root.parent)

    print("Root:   ", root)
    print("Source: ", cat.source)
    print(cat)

    write(out_dir / "datasets.md",    build_datasets_page(cat))
    write(out_dir / "collections.md", build_collections_page(cat))
    write(out_dir / "releases.md",    build_releases_page(cat))

    if not (out_dir / "index.md").exists():
        print(f"NOTE: {out_dir / 'index.md'} is missing. It is hand-written and not generated here.")

    issues = cat.validate()
    if issues:
        print(f"\n{len(issues)} inconsistencies found in the source JSON. "
              f"Pages were built anyway; list them with:")
        print("  python scripts/crn_rosetta.py validate")
    return 0


if __name__ == "__main__":
    sys.exit(main())
