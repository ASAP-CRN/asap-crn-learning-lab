"""
build_rosetta_stone.py

Generates:
  docs/rosetta-stone/index.md
  docs/rosetta-stone/datasets.md
  docs/rosetta-stone/collections.md
  docs/rosetta-stone/releases.md

Run from inside the asap-crn-learning-lab repo:
  python scripts/build_rosetta_stone.py
"""

import sys
from pathlib import Path
from collections import defaultdict

# Allow running from repo root or scripts/ directory
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from rosetta_helpers import (
    esc, safe_id, doi_link, doi_link_or, version_key,
    load_datasets, load_collections_index, load_releases_index,
    get_dataset_id, get_dataset_title, get_tags,
    get_curation, get_collection_name, get_dataset_version,
    get_release_version, get_collection_version, get_collection_doi,
    get_curation_release_history, get_dataset_release_history,
    get_all_releases, get_all_versions, get_cde_version,
    get_collection_top_doi, get_collection_version_doi, get_collection_record,
    has_curation, derive_curation_status, all_releases_for_dataset,
    curation_badge_html, badge_latest_html,
    render_curation_card, render_bucket_card,
    render_full_history_table,
    render_bucket_rows, build_select, LEGEND_HTML,
)


# ─────────────────────────────────────────────────────────────────────────────
# Paths
# ─────────────────────────────────────────────────────────────────────────────

def find_repo_root(start: Path) -> Path:
    for p in [start] + list(start.parents):
        if (p / "mkdocs.yml").exists():
            return p
    raise FileNotFoundError("mkdocs.yml not found. Run from inside the Learning Lab repo.")


ROOT             = find_repo_root(Path.cwd())
DATASET_REPO     = ROOT.parent / "cloud-datasets"
COLLECTIONS_REPO = ROOT.parent / "cloud-collections"
RELEASES_REPO    = ROOT.parent / "cloud-releases"

DATASET_INDEX    = DATASET_REPO / "datasets.json"
DATASET_DIR      = DATASET_REPO / "datasets"
COLLECTIONS_FILE = COLLECTIONS_REPO / "collections.json"
RELEASES_FILE    = RELEASES_REPO   / "releases.json"

OUT_DIR     = ROOT / "docs" / "rosetta-stone"
CSS_DIR     = ROOT / "docs" / "stylesheets"
JS_DIR      = ROOT / "docs" / "javascripts"

for d in (OUT_DIR, CSS_DIR, JS_DIR):
    d.mkdir(parents=True, exist_ok=True)

print("Root:           ", ROOT)
print("Dataset repo:   ", DATASET_REPO)
print("Collections:    ", COLLECTIONS_REPO)
print("Releases:       ", RELEASES_REPO)


# ─────────────────────────────────────────────────────────────────────────────
# Load data
# ─────────────────────────────────────────────────────────────────────────────

if not DATASET_INDEX.exists():
    raise FileNotFoundError(f"Dataset index not found: {DATASET_INDEX}")
if not DATASET_DIR.exists():
    raise FileNotFoundError(f"Dataset detail dir not found: {DATASET_DIR}")

datasets         = load_datasets(DATASET_INDEX, DATASET_DIR)
collections_idx  = load_collections_index(COLLECTIONS_FILE)
releases_idx     = load_releases_index(RELEASES_FILE)

if not datasets:
    raise ValueError("No dataset records loaded.")

print(f"Datasets:    {len(datasets)}")
print(f"Collections: {len(collections_idx)}")
print(f"Releases:    {len(releases_idx)}")


# ─────────────────────────────────────────────────────────────────────────────
# Pre-compute filter option lists
# ─────────────────────────────────────────────────────────────────────────────

all_tags = sorted(
    {t for d in datasets for t in get_tags(d)},
    key=str.lower,
)
all_releases_opts = sorted(
    {get_release_version(d) for d in datasets if get_release_version(d) != "TBD"},
    key=version_key, reverse=True,
)
all_cde_opts = sorted(
    {
        ri.get("cde_version", "")
        for d in datasets
        for ri in get_dataset_release_history(d).values()
        if isinstance(ri, dict) and ri.get("cde_version")
    },
    key=version_key, reverse=True,
)
all_collection_opts = sorted(
    {get_collection_name(d) for d in datasets if get_collection_name(d) not in ("NA", "", "TBD")},
    key=str.lower,
)


# ─────────────────────────────────────────────────────────────────────────────
# Helper: dataset anchor id
# ─────────────────────────────────────────────────────────────────────────────

def dataset_anchor(dataset_id: str) -> str:
    return f"dataset-{safe_id(dataset_id)}"


def dataset_link(dataset_id: str, label: str = "") -> str:
    anchor = dataset_anchor(dataset_id)
    text   = esc(label or dataset_id)
    return f'<a href="datasets/#{anchor}">{text}</a>'


# ─────────────────────────────────────────────────────────────────────────────
# ① index.md
# ─────────────────────────────────────────────────────────────────────────────

def build_index() -> str:
    lines = [
        "# CRN Cloud Rosetta Stone",
        "",
        "The Rosetta Stone helps you find datasets, understand curation history, "
        "and locate the right bucket paths for each release.",
        "",
        "## Pages",
        "",
        "| Page | Purpose |",
        "| ---- | ------- |",
        "| [Dataset Finder](datasets.md) | Search and filter all datasets. View curation details, release history, and bucket paths. |",
        "| [Collection Manifest](collections.md) | Review which datasets belong to each collection and where files resolve per release. |",
        "| [Release View](releases.md) | See what changed in each release — added, updated, and unchanged datasets. |",
        "",
        "## Curation status legend",
        "",
        LEGEND_HTML,
        "",
        "## Key concepts",
        "",
        "**Release** — the CRN Cloud release in which a dataset's curated files "
        "were last produced. If a dataset is unchanged in the latest release, its files may "
        "still resolve to an earlier release path.",
        "",
        "**Collection version** — a versioned snapshot of a collection. A single collection "
        "version can include datasets whose files were materialized in different releases.",
        "",
        "**Bucket paths** — `prod` contains curated outputs; `raw` contains unprocessed source files.",
        "",
    ]
    return "\n".join(lines)


# ─────────────────────────────────────────────────────────────────────────────
# ② datasets.md
# ─────────────────────────────────────────────────────────────────────────────

def _render_meta_strip(dataset_doi, license_val, col_name, col_doi, ds_version):
    doi_cell  = doi_link(dataset_doi) or "TBD"
    cdoi_cell = doi_link(col_doi)     or "TBD"

    def item(label, value, extra_cls=""):
        return (
            f'<div class="rs-meta-item">'
            f'<span class="rs-meta-label">{label}</span>'
            f'<span class="rs-meta-value {extra_cls}">{value}</span>'
            f'</div>'
        )

    col_na    = col_name in ("NA", "", "TBD", None)
    col_doi_na = not col_doi

    return (
        '<div class="rs-meta-strip">'
        + item("License",        esc(license_val))
        + item("Dataset DOI",    doi_cell)
        + item("Collection",     '<span class="rs-na">—</span>' if col_na else esc(col_name),
               "rs-na" if col_na else "")
        + item("Collection DOI", '<span class="rs-na">—</span>' if col_doi_na else cdoi_cell,
               "rs-na" if col_doi_na else "")
        + item("Latest version", f'<span class="rs-mono">{esc(ds_version)}</span>')
        + '</div>'
    )


def build_datasets_page() -> str:
    tag_opts = ['<option value="">All tags</option>']
    for t in all_tags:
        tag_opts.append(f'<option value="{esc(t.lower())}">{esc(t)}</option>')

    # ── Guidance block — simple and plain
    guidance_html = (
        '<div class="rs-guidance">'
        '<p class="rs-guidance-intro">Find datasets, review curation details, and copy bucket paths.</p>'
        '<div class="rs-guidance-steps">'
        '<div class="rs-guidance-step"><span class="rs-guidance-num">1</span>'
        '<span>Search by dataset ID, title, keyword, DOI, or bucket path.</span></div>'
        '<div class="rs-guidance-step"><span class="rs-guidance-num">2</span>'
        '<span>Filter by release, CDE version, collection, or tag.</span></div>'
        '<div class="rs-guidance-step"><span class="rs-guidance-num">3</span>'
        '<span>Click <strong>View</strong> to see curation details, bucket paths, and release history.</span></div>'
        '</div>'
        '</div>'
    )

    # ── Curation status legend — card grid layout
    def _legend_item(bg, color, border, label, description):
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
        + _legend_item("#e8f5ee", "#0d6b3f", "#6fcf97", "added",
                       "Curation files first produced in this release.")
        + _legend_item("#e8f0fb", "#1a4fa0", "#7baee8", "updated",
                       "Curation files re-run or changed since the prior release.")
        + _legend_item("#f0eeea", "#5a5850", "#bbb9b0", "unchanged",
                       "Included but files resolve to an earlier release.")
        + _legend_item("#fef3e2", "#8a5a00", "#f0b429", "not curated",
                       "No curated outputs for this dataset in this release.")
        + '</div>'
        '</div>'
    )

    # Build filter bar HTML
    filter_bar = (
        '<div class="rs-filters">'
        f'<input id="rsSearch" class="rs-search" type="text"'
        f' placeholder="Search by dataset ID, title, keyword, DOI, or bucket path…">'
        + build_select("rsReleaseFilter",    "releases",     all_releases_opts)
        + build_select("rsCdeFilter",        "CDE versions", all_cde_opts)
        + build_select("rsCollectionFilter", "collections",  all_collection_opts)
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
        '<th class="sortable" data-col="4">Release <i class="rs-sort-icon">⇅</i></th>',
        '<th class="sortable" data-col="5">Collection<br>version <i class="rs-sort-icon">⇅</i></th>',
        "<th>Details</th>",
        "</tr></thead>",
        "<tbody>",
    ]
    drawers = []

    def dash_if_na(val):
        """Return em-dash for NA/TBD/empty values in the summary table."""
        return "—" if str(val).strip() in ("NA", "TBD", "") else val

    def short_path(path):
        """Trim absolute path to start from 'GitHub/' if present."""
        marker = "GitHub/"
        idx2 = path.find(marker)
        if idx2 != -1:
            return path[idx2:]
        parts = path.replace("\\", "/").rstrip("/").split("/")
        return "/".join(parts[-3:]) if len(parts) >= 3 else path

    for idx, ds in enumerate(datasets):
        ds_id       = get_dataset_id(ds)
        ds_title    = get_dataset_title(ds)
        description = str(ds.get("description", ""))
        license_val = str(ds.get("license", "TBD"))
        keywords    = ds.get("keywords", [])
        buckets     = ds.get("buckets", {})
        ds_doi      = ds.get("doi", "")

        if not isinstance(keywords, list): keywords = [keywords]
        keywords = [str(k) for k in keywords if k is not None]
        if not isinstance(buckets, dict):  buckets  = {}

        tags       = get_tags(ds)
        col_name   = get_collection_name(ds)
        ds_version = get_dataset_version(ds)
        rel_ver    = get_release_version(ds)
        col_ver    = get_collection_version(ds)
        col_doi    = get_collection_doi(ds, collections_idx)

        cur         = get_curation(ds)
        cur_rel_key = cur.get("release_version", "")
        hist        = get_dataset_release_history(ds)
        all_rel     = get_all_releases(ds)
        all_ver     = get_all_versions(ds)

        all_cde_attr = "||".join(
            ri.get("cde_version", "")
            for ri in hist.values()
            if isinstance(ri, dict) and ri.get("cde_version")
        )

        # Build search text
        cur_hist = get_curation_release_history(ds)
        cur_rel_search = " ".join(
            f"{rk} {ri.get('collection_version','')} {ri.get('release_version','')} {ri.get('collection_version_doi','')}"
            for rk, ri in cur_hist.items() if isinstance(ri, dict)
        )
        ds_rel_search = " ".join(
            f"{rk} {ri.get('dataset_version','')} {ri.get('cde_version','')}"
            for rk, ri in hist.items() if isinstance(ri, dict)
        )
        search_text = " ".join([
            ds_id, ds_title, description, col_name,
            ds_version, rel_ver, col_ver, col_doi, ds_doi,
            " ".join(tags), " ".join(keywords),
            " ".join(all_rel), " ".join(all_ver),
            " ".join(str(v) for v in buckets.values()),
            cur_rel_search, ds_rel_search,
        ]).lower()

        anchor       = dataset_anchor(ds_id)
        detail_id    = f"rs-detail-{safe_id(ds_id)}-{idx}"
        releases_sorted = all_releases_for_dataset(ds)

        # ── Summary row — View button opens side drawer
        body_parts.append(
            f'<tr id="{esc(anchor)}" class="rs-dataset-row"'
            f' data-detail="{esc(detail_id)}"'
            f' data-search="{esc(search_text)}"'
            f' data-tags="{esc("||".join(t.lower() for t in tags))}"'
            f' data-release="{esc(rel_ver)}"'
            f' data-cde="{esc(all_cde_attr)}"'
            f' data-collection="{esc(col_name)}">'
            f'<td><code>{esc(ds_id)}</code></td>'
            f'<td>{esc(ds_title)}</td>'
            f'<td>{esc(dash_if_na(col_name))}</td>'
            f'<td>{esc(dash_if_na(ds_version))}</td>'
            f'<td>{esc(dash_if_na(rel_ver))}</td>'
            f'<td>{esc(dash_if_na(col_ver))}</td>'
            f'<td><button class="rs-toggle" data-target="{esc(detail_id)}" onclick="rsOpenDrawer(this)">View</button></td>'
            f'</tr>'
        )

        # ── Side drawer — appended after the table, shown/hidden via JS
        tags_html   = (
            " ".join(f'<span class="rs-tag-pill">{esc(t)}</span>' for t in tags)
            if tags else '<span class="rs-na">—</span>'
        )
        meta_strip  = _render_meta_strip(ds_doi, license_val, col_name, col_doi, ds_version)
        cur_card    = render_curation_card(ds, collections_idx)
        bucket_card = render_bucket_card(buckets)
        hist_table  = render_full_history_table(releases_sorted, ds, collections_idx, releases_idx)

        drawers.append(
            f'<div id="{esc(detail_id)}" class="rs-drawer" role="dialog" aria-label="{esc(ds_title)}">'
            f'<div class="rs-drawer-inner">'
            f'<div class="rs-drawer-header">'
            f'<div>'
            f'<div class="rs-drawer-title">{esc(ds_title)}</div>'
            f'<div class="rs-detail-id">{esc(ds_id)}</div>'
            f'</div>'
            f'<button class="rs-drawer-close" onclick="rsCloseDrawer(this)" aria-label="Close">✕</button>'
            f'</div>'
            f'<div class="rs-drawer-body">'
            f'<div class="rs-tag-row">{tags_html}</div>'
            + meta_strip
            + f'<div class="rs-section"><div class="rs-section-header">Description</div>'
            f'<p class="rs-description">{esc(description) if description else "TBD"}</p></div>'
            + f'<div class="rs-panel-sections">'
            f'{cur_card}{bucket_card}'
            f'</div>'
            + hist_table
            + f'<div class="rs-section"><div class="rs-section-header">Source</div>'
            f'<div class="rs-field">'
            f'<span class="rs-field-label">Detail JSON</span>'
            f'<span class="rs-field-value rs-mono" style="font-size:0.7rem">'
            f'{esc(short_path(ds.get("_detail_file","") or ""))}</span></div></div>'
            f'</div>'  # drawer-body
            f'</div>'  # drawer-inner
            f'</div>'  # drawer
        )

    body_parts += ["</tbody>", "</table>"]
    # Overlay backdrop (hidden by default, shown when a drawer is open)
    body_parts.append('<div id="rsDrawerOverlay" class="rs-drawer-overlay" onclick="rsCloseAllDrawers()"></div>')
    # All side drawers
    body_parts += drawers
    body_parts.append("</div>")  # close rs-page-body
    return header_md + "\n".join(body_parts)


# ─────────────────────────────────────────────────────────────────────────────
# ③ collections.md
# ─────────────────────────────────────────────────────────────────────────────

def build_collections_page() -> str:
    # Group datasets by collection name
    by_collection = defaultdict(list)
    uncollected   = []
    for ds in datasets:
        col = get_collection_name(ds)
        if col == "NA":
            uncollected.append(ds)
        else:
            by_collection[col].append(ds)

    def col_sort_key(name):
        keys = list(collections_idx.keys())
        return (keys.index(name) if name in keys else len(keys), name.lower())

    sorted_collections = sorted(by_collection.keys(), key=col_sort_key)

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
        "file metadata, and curated outputs may still resolve to an earlier release path."
        '</div>'
    )
    body.append(LEGEND_HTML)

    def render_collection_section(col_name: str, col_datasets: list) -> list:
        col_rec     = get_collection_record(collections_idx, col_name)
        col_title   = col_rec.get("title", col_name)
        col_doi     = get_collection_top_doi(collections_idx, col_name)
        cur_ver     = col_rec.get("current_version", "")
        col_release = (col_rec.get("release") or {}).get("version", "")

        # Count statuses across all datasets in this collection
        status_counts: dict = defaultdict(int)
        for ds in col_datasets:
            status = derive_curation_status(
                get_release_version(ds), ds, all_releases_for_dataset(ds)
            )
            status_counts[status] += 1

        status_html = " ".join(
            curation_badge_html(s) + f' <span style="font-size:0.78rem">{c}</span>'
            for s, c in sorted(status_counts.items())
        )

        meta_parts = []
        if cur_ver:
            meta_parts.append(f'<span>Current version: <span class="rs-mono">{esc(cur_ver)}</span></span>')
        if col_doi:
            meta_parts.append(f'<span>Collection DOI: {doi_link(col_doi)}</span>')
        if col_release:
            meta_parts.append(f'<span>Latest release: <span class="rs-mono">{esc(col_release)}</span></span>')
        meta_parts.append(f'<span>{len(col_datasets)} datasets</span>')

        sec_html = (
            f'<h2 id="col-{esc(safe_id(col_name))}">{esc(col_title)}</h2>'
            f'<div class="rs-collection-header">'
            f'<span class="rs-collection-header-name rs-mono">{esc(col_name)}</span>'
            f'<span class="rs-collection-header-meta">{"".join(meta_parts)}</span>'
            f'<div class="rs-status-counts">{status_html}</div>'
            f'</div>'
            f'<div style="overflow-x:auto">'
            f'<table class="rs-table rs-collection-table">'
            f'<thead><tr>'
            f'<th>Dataset</th><th>Dataset version</th><th>Curation status</th>'
            f'<th>Release</th><th>Collection version</th>'
            f'<th>CDE version</th><th>Dataset DOI</th><th>Details</th>'
            f'</tr></thead><tbody>'
        )

        for ds in sorted(col_datasets, key=lambda d: get_dataset_id(d).lower()):
            ds_id   = get_dataset_id(ds)
            ds_ver  = get_dataset_version(ds)
            rel_ver = get_release_version(ds)
            col_ver = get_collection_version(ds)
            cde_ver = get_cde_version(ds)
            ds_doi  = ds.get("doi", "")
            status  = derive_curation_status(rel_ver, ds, all_releases_for_dataset(ds))
            badge   = curation_badge_html(status)
            anchor  = dataset_anchor(ds_id)
            sec_html += (
                f'<tr>'
                f'<td><a href="datasets/#{esc(anchor)}"><code>{esc(ds_id)}</code></a></td>'
                f'<td><span class="rs-mono">{esc(ds_ver)}</span></td>'
                f'<td>{badge}</td>'
                f'<td><span class="rs-mono">{esc(rel_ver)}</span></td>'
                f'<td><span class="rs-mono">{esc(col_ver)}</span></td>'
                f'<td><span class="rs-mono">{esc(cde_ver)}</span></td>'
                f'<td>{doi_link_or(ds_doi, "—")}</td>'
                f'<td><a href="datasets/#{esc(anchor)}">→ details</a></td>'
                f'</tr>'
            )

        sec_html += '</tbody></table></div>'
        return sec_html

    for col_name in sorted_collections:
        body.append(render_collection_section(col_name, by_collection[col_name]))

    if uncollected:
        unc_html = (
            '<h2>Uncollected datasets</h2>'
            '<p style="font-size:0.85rem;margin-bottom:0.6rem">These datasets are not assigned to any collection.</p>'
            '<div style="overflow-x:auto">'
            '<table class="rs-table rs-collection-table">'
            '<thead><tr>'
            '<th>Dataset</th><th>Dataset version</th><th>Curation status</th>'
            '<th>Release</th><th>Collection version</th>'
            '<th>CDE version</th><th>Dataset DOI</th><th>Details</th>'
            '</tr></thead><tbody>'
        )
        for ds in sorted(uncollected, key=lambda d: get_dataset_id(d).lower()):
            ds_id   = get_dataset_id(ds)
            ds_ver  = get_dataset_version(ds)
            rel_ver = get_release_version(ds)
            col_ver = get_collection_version(ds)
            cde_ver = get_cde_version(ds)
            ds_doi  = ds.get("doi", "")
            status  = derive_curation_status(rel_ver, ds, all_releases_for_dataset(ds))
            badge   = curation_badge_html(status)
            anchor  = dataset_anchor(ds_id)
            unc_html += (
                f'<tr>'
                f'<td><a href="datasets/#{esc(anchor)}"><code>{esc(ds_id)}</code></a></td>'
                f'<td><span class="rs-mono">{esc(ds_ver)}</span></td>'
                f'<td>{badge}</td>'
                f'<td><span class="rs-mono">{esc(rel_ver)}</span></td>'
                f'<td><span class="rs-mono">{esc(col_ver)}</span></td>'
                f'<td><span class="rs-mono">{esc(cde_ver)}</span></td>'
                f'<td>{doi_link_or(ds_doi, "—")}</td>'
                f'<td><a href="datasets/#{esc(anchor)}">→ details</a></td>'
                f'</tr>'
            )
        unc_html += '</tbody></table></div>'
        body.append(unc_html)

    body.append('</div>')
    return header_md + "\n".join(body)


# ─────────────────────────────────────────────────────────────────────────────
# ④ releases.md
# ─────────────────────────────────────────────────────────────────────────────

def build_releases_page() -> str:
    # Collect all release versions across all datasets
    all_release_keys = set()
    for ds in datasets:
        all_release_keys.update(get_dataset_release_history(ds).keys())
        all_release_keys.update(get_all_releases(ds))
    all_release_keys.update(releases_idx.keys())

    sorted_releases = sorted(all_release_keys, key=version_key, reverse=True)

    header_md = "\n".join([
        "# Release View",
        "",
        "Datasets grouped by CRN Cloud release, sorted newest first. "
        "Dataset names link to the Dataset Finder for full detail.",
        "",
    ])

    body = ['<div class="rs-page-body">', LEGEND_HTML]

    for rel_ver in sorted_releases:
        rel_meta    = releases_idx.get(rel_ver, {})
        rel_doi     = rel_meta.get("doi", "")
        rel_cde     = rel_meta.get("cde_version", "")
        rel_date    = rel_meta.get("date", "")

        # Find all datasets in this release and their per-release info
        rel_datasets = []
        for ds in datasets:
            hist = get_dataset_release_history(ds)
            if rel_ver in hist:
                rel_datasets.append(ds)

        if not rel_datasets:
            continue

        # Derive status for each dataset in this release
        ds_rows = []
        status_counts: dict = defaultdict(int)
        collections_touched = set()

        for ds in sorted(rel_datasets, key=lambda d: get_dataset_id(d).lower()):
            ds_id      = get_dataset_id(ds)
            hist       = get_dataset_release_history(ds)
            rel_sorted = all_releases_for_dataset(ds)
            status     = derive_curation_status(rel_ver, ds, rel_sorted)
            status_counts[status] += 1

            rel_info   = hist.get(rel_ver, {})
            ds_ver     = rel_info.get("dataset_version", get_dataset_version(ds))
            cde_ver    = rel_info.get("cde_version", "TBD")
            ds_doi     = ds.get("doi", "")
            col_name   = get_collection_name(ds)
            col_ver    = get_collection_version(ds)
            anchor     = dataset_anchor(ds_id)

            if col_name not in ("NA", ""):
                collections_touched.add(col_name)

            ds_rows.append((ds_id, ds_ver, col_name, col_ver, cde_ver, ds_doi, status, anchor))

        status_html = " ".join(
            curation_badge_html(s) + f' <span style="font-size:0.78rem">{c}</span>'
            for s, c in sorted(status_counts.items())
        )
        col_list = ", ".join(sorted(collections_touched)) if collections_touched else "—"

        meta_spans = []
        if rel_cde:  meta_spans.append(f'<span>CDE: <span class="rs-mono">{esc(rel_cde)}</span></span>')
        if rel_date: meta_spans.append(f'<span>Date: {esc(rel_date)}</span>')
        if rel_doi:  meta_spans.append(f'<span>DOI: {doi_link(rel_doi)}</span>')
        meta_spans.append(f'<span>{len(rel_datasets)} datasets</span>')

        rows_html = ""
        for ds_id, ds_ver, col_name, col_ver, cde_ver, ds_doi, status, anchor in ds_rows:
            badge = curation_badge_html(status)
            rows_html += (
                f'<tr>'
                f'<td><a href="datasets/#{esc(anchor)}"><code>{esc(ds_id)}</code></a></td>'
                f'<td>{esc(col_name)}</td>'
                f'<td><span class="rs-mono">{esc(ds_ver)}</span></td>'
                f'<td><span class="rs-mono">{esc(col_ver)}</span></td>'
                f'<td><span class="rs-mono">{esc(cde_ver)}</span></td>'
                f'<td>{badge}</td>'
                f'</tr>'
            )

        col_note = (
            f'<p style="font-size:0.8rem;margin-bottom:0.6rem;color:var(--md-default-fg-color--light)">'
            f'Collections: {esc(col_list)}</p>'
            if collections_touched else ""
        )

        body.append(
            f'<div class="rs-release-section">'
            f'<div class="rs-release-section-header">'
            f'<span class="rs-release-version">{esc(rel_ver)}</span>'
            f'<span class="rs-release-meta">{"".join(meta_spans)}</span>'
            f'<div class="rs-status-counts">{status_html}</div>'
            f'</div>'
            f'<div class="rs-release-section-body">'
            + col_note
            + '<table class="rs-table rs-release-table">'
            '<thead><tr>'
            '<th>Dataset</th><th>Collection</th><th>Dataset version</th>'
            '<th>Collection version</th><th>CDE version</th><th>Curation status</th>'
            '</tr></thead>'
            f'<tbody>{rows_html}</tbody>'
            f'</table></div></div>'
        )

    body.append('</div>')
    return header_md + "\n".join(body)


# ─────────────────────────────────────────────────────────────────────────────
# Write all files
# ─────────────────────────────────────────────────────────────────────────────

def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"Wrote: {path}")


write(OUT_DIR / "index.md",       build_index())
write(OUT_DIR / "datasets.md",    build_datasets_page())
write(OUT_DIR / "collections.md", build_collections_page())
write(OUT_DIR / "releases.md",    build_releases_page())

print("\nDone. Add to mkdocs.yml if not already present:")
print("  extra_css:")
print("    - stylesheets/rosetta-stone.css")
print("  extra_javascript:")
print("    - javascripts/rosetta-stone.js")
