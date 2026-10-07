"""
rosetta_helpers.py
HTML primitives and fragments for build_rosetta_stone.py.

All data access goes through crn_rosetta.Catalog; nothing in this file reads JSON.
"""

import html as _html
import re

from crn_rosetta import Catalog, Dataset, version_key  # noqa: F401  (version_key re-exported)

DATASETS_REPO_URL = "https://github.com/ASAP-CRN/cloud-datasets/blob/main/datasets"
NA_HTML = '<span class="rs-na">—</span>'


# ─────────────────────────────────────────────────────────────────────────────
# Basic HTML utilities
# ─────────────────────────────────────────────────────────────────────────────

def esc(value):
    if value is None:
        return ""
    return _html.escape(str(value), quote=True)


def safe_id(value):
    value = str(value).lower().strip()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "item"


def doi_url(doi):
    if not doi:
        return ""
    doi = str(doi).strip()
    if doi.startswith("http://") or doi.startswith("https://"):
        return doi
    return f"https://doi.org/{doi}"


def doi_link(doi):
    if not doi:
        return ""
    doi = str(doi).strip()
    url = doi_url(doi)
    label = doi.replace("https://doi.org/", "").replace("http://doi.org/", "")
    return f'<a href="{esc(url)}" target="_blank" rel="noopener">{esc(label)} ↗</a>'


def doi_link_or(doi, missing="—"):
    result = doi_link(doi)
    return result if result else f'<span class="rs-na">{esc(missing)}</span>'


def mono(value, missing=NA_HTML):
    """Monospace span, or an em-dash placeholder when there is no value."""
    return f'<span class="rs-mono">{esc(value)}</span>' if value else missing


def dataset_anchor(dataset_id: str) -> str:
    return f"dataset-{safe_id(dataset_id)}"


def dataset_href(dataset_id: str) -> str:
    """Link from the collections/releases pages to a row on the datasets page."""
    return f"../datasets/#{dataset_anchor(dataset_id)}"


# ─────────────────────────────────────────────────────────────────────────────
# Curation status badge  (colours for .rs-badge--<status> live in rosetta-stone.css)
# ─────────────────────────────────────────────────────────────────────────────

# status -> (label, background, text colour, border, description)
STATUS_CFG = {
    "added":       ("added",       "#e8f5ee", "#0d6b3f", "#6fcf97",
                    "Curation files first produced in this release."),
    "updated":     ("updated",     "#e8f0fb", "#1a4fa0", "#7baee8",
                    "Curation files re-run or changed since the prior release."),
    "unchanged":   ("unchanged",   "#f0eeea", "#5a5850", "#bbb9b0",
                    "Included but files resolve to an earlier release."),
    "not-curated": ("not curated", "#fef3e2", "#8a5a00", "#f0b429",
                    "No curated outputs for this dataset in this release."),
}
STATUS_ORDER = list(STATUS_CFG)


def curation_badge_html(status: str) -> str:
    if status not in STATUS_CFG:
        status = "not-curated"
    return f'<span class="rs-badge rs-badge--{status}"><i></i>{esc(STATUS_CFG[status][0])}</span>'


def status_counts_html(counts: dict) -> str:
    return " ".join(
        curation_badge_html(s) + f' <span style="font-size:0.78rem">{counts[s]}</span>'
        for s in STATUS_ORDER if counts.get(s)
    )


def badge_latest_html() -> str:
    return '<span class="rs-latest-badge">latest</span>'


def change_badge_html(change) -> str:
    """Pill for a dataset version that was new or updated in a release."""
    return f'<span class="rs-change-badge">{esc(change)}</span>' if change else ""


LEGEND_HTML = (
    '\n<div class="rs-legend">\n'
    '  <span class="rs-legend-title">Curation status:</span>\n'
    + "".join(
        f'  <span class="rs-legend-item">{curation_badge_html(s)} — '
        f'{esc(STATUS_CFG[s][4].rstrip("."))}</span>\n'
        for s in STATUS_ORDER
    )
    + '</div>\n'
)


# ─────────────────────────────────────────────────────────────────────────────
# Dataset drawer fragments
# ─────────────────────────────────────────────────────────────────────────────

def _field(label, value_html):
    return (
        f'<div class="rs-field">'
        f'<span class="rs-field-label">{label}</span>'
        f'<span class="rs-field-value">{value_html}</span>'
        f'</div>'
    )


def _copy_btn(path):
    return f'<button class="rs-copy-btn" data-path="{esc(path)}" onclick="rsCopyPath(this)">Copy</button>'


def collection_version_doi(cat: Catalog, rec) -> str:
    """DOI for the collection version a curation record points at: cloud-collections first."""
    return cat.collection_version_doi(rec.collection, rec.collection_version) or rec.collection_version_doi


def render_bucket_rows(paths: dict) -> str:
    """
    Bucket rows with copy buttons. UAT/DEV are never shown.
    `paths` is Catalog.paths(): raw, prod, and (for curated datasets) the curated
    output path for the latest release plus its location in the collection bucket.
    """
    rows_cfg = [
        ("prod",       "#0d6b3f"),
        ("raw",        "#5a5850"),
        ("curated",    "#1a4fa0"),
        ("collection", "#1a4fa0"),
    ]
    rows = []
    for key, color in rows_cfg:
        path = paths.get(key)
        if not path:
            continue
        rows.append(
            f'<div class="rs-env-row">'
            f'<span class="rs-env-dot" style="background:{color}"></span>'
            f'<span class="rs-env-name" style="color:{color}">{esc(key)}</span>'
            f'<span class="rs-env-path rs-env-path--wrap">{esc(path)}</span>'
            f'{_copy_btn(path)}'
            f'</div>'
        )
    return "".join(rows) or '<div class="rs-no-buckets">No bucket paths listed.</div>'


def render_bucket_card(paths: dict) -> str:
    hint = ""
    if paths.get("curated"):
        hint = (
            f'<p class="rs-table-hint"><strong>curated</strong> is where this dataset\'s curated '
            f'outputs live as of the latest release (produced in '
            f'{esc(paths.get("curated_release"))}). <strong>collection</strong> is the same '
            f'output inside the collection bucket.</p>'
        )
    return (
        '<div class="rs-card">'
        '<div class="rs-card-header">'
        '<span class="rs-card-title">Bucket access</span>'
        '</div>'
        f'<div class="rs-card-body rs-bucket-body">'
        f'{render_bucket_rows(paths)}{hint}'
        f'</div></div>'
    )


def render_curation_card(cat: Catalog, ds: Dataset) -> str:
    """Curation details as of the latest release, or an empty state if never curated."""
    status = cat.status(ds) or "not-curated"
    badge  = curation_badge_html(status)
    rec    = cat.curation(ds)

    if rec is None:
        return (
            '<div class="rs-card">'
            '<div class="rs-card-header">'
            '<span class="rs-card-title">Curation details</span>'
            f'<span class="rs-card-header-right">{badge}</span>'
            '</div>'
            '<div class="rs-no-curation">'
            '<span class="rs-no-curation-icon">∅</span>'
            '<p>No curation files have been produced for this dataset.</p>'
            '</div></div>'
        )

    workflow = esc(rec.workflow)
    if rec.workflow_version:
        workflow += f' <span class="rs-mono">{esc(rec.workflow_version)}</span>'
    if rec.workflow_url:
        workflow = f'<a href="{esc(rec.workflow_url)}" target="_blank" rel="noopener">{workflow} ↗</a>'
    steps = " · ".join(
        f'{esc(name)} <span class="rs-mono">{esc(ver)}</span>' for name, ver in rec.components.items()
    )
    collection = cat.collection(rec.collection) if rec.collection in cat.collection_names else None

    body = "".join([
        _field("Curated in release",     f'<span class="rs-highlight rs-mono">{esc(rec.release)}</span>'),
        _field("Dataset version",        f'<span class="rs-highlight rs-mono">'
                                         f'{esc(cat.dataset_version(ds, rec.release) or "TBD")}</span>'),
        _field("CDE version",            mono(cat.release(rec.release).cde_version, "TBD")),
        _field("Workflow",               workflow or NA_HTML),
        _field("Workflow steps",         steps or NA_HTML),
        _field("Collection",             esc(rec.collection) or NA_HTML),
        _field("Collection version",     mono(rec.collection_version)),
        _field("Collection DOI",         doi_link_or(collection.doi if collection else "", "TBD")),
        _field("Collection version DOI", doi_link_or(collection_version_doi(cat, rec), "—")),
    ])

    return (
        f'<div class="rs-card">'
        f'<div class="rs-card-header">'
        f'<span class="rs-card-title">Curation details</span>'
        f'<span class="rs-card-header-right">{badge}</span>'
        f'</div>'
        f'<div class="rs-card-body">{body}</div>'
        f'</div>'
    )


def render_full_history_table(cat: Catalog, ds: Dataset) -> str:
    """One row per release that includes the dataset, newest first."""
    rows = []
    for i, row in enumerate(reversed(cat.history(ds))):
        rel     = cat.release(row["release"])
        col_ver = row["collection_version"]
        col_doi = cat.collection_version_doi(row["collection"], col_ver) if col_ver else ""
        rows.append(
            f'<tr>'
            f'<td><span class="rs-mono">{esc(rel.version)}</span> {badge_latest_html() if i == 0 else ""}</td>'
            f'<td>{mono(row["dataset_version"], "TBD")} {change_badge_html(row["change"])}</td>'
            f'<td>{mono(col_ver)}</td>'
            f'<td>{doi_link_or(col_doi, "—")}</td>'
            f'<td>{mono(rel.cde_version, "TBD")}</td>'
            f'<td>{doi_link_or(rel.doi, "—")}</td>'
            f'<td>{curation_badge_html(row["status"])}</td>'
            f'</tr>'
        )

    empty = '<tr><td colspan="7">Not included in any release yet.</td></tr>'
    return (
        '<div class="rs-section">'
        '<div class="rs-section-header">Release history</div>'
        '<div class="rs-card rs-card--table">'
        '<table class="rs-mini-table">'
        '<thead><tr>'
        '<th>Release</th><th>Dataset version</th><th>Collection version</th>'
        '<th>Collection DOI</th><th>CDE version</th><th>Release DOI</th><th>Curation</th>'
        '</tr></thead>'
        f'<tbody>{"".join(rows) if rows else empty}</tbody>'
        '</table></div>'
        '</div>'
    )


def render_curation_history_table(cat: Catalog, ds: Dataset) -> str:
    """Every release in which curated outputs were produced, with the path to each."""
    if not ds.curation:
        return ""
    items = []
    for rec in reversed(list(ds.curation.values())):
        workflow = f'workflow <span class="rs-mono">{esc(rec.workflow_version or "—")}</span>'
        if rec.workflow_url:
            workflow = f'<a href="{esc(rec.workflow_url)}" target="_blank" rel="noopener">{workflow} ↗</a>'
        items.append(
            f'<div class="rs-curated-item">'
            f'<div class="rs-curated-meta">'
            f'<span class="rs-curated-release rs-mono">{esc(rec.release)}</span>'
            f'<span>collection <span class="rs-mono">{esc(rec.collection_version or "—")}</span></span>'
            f'<span>{workflow}</span>'
            f'</div>'
            f'<div class="rs-env-row">'
            f'<span class="rs-env-path rs-env-path--wrap">{esc(rec.dataset_bucket)}</span>'
            f'{_copy_btn(rec.dataset_bucket)}'
            f'</div>'
            f'</div>'
        )
    return (
        '<div class="rs-section">'
        '<div class="rs-section-header">Curated outputs by release</div>'
        f'<div class="rs-card">{"".join(items)}</div>'
        '<p class="rs-table-hint">Each entry is a release in which this dataset\'s curated outputs '
        'were produced. Releases in between reuse the entry before them.</p>'
        '</div>'
    )


# ─────────────────────────────────────────────────────────────────────────────
# Filter <select> builder
# ─────────────────────────────────────────────────────────────────────────────

def build_select(element_id: str, all_label: str, values: list,
                 css_class: str = "rs-filter-select") -> str:
    opts = [f'<option value="">All {esc(all_label)}</option>']
    for v in values:
        opts.append(f'<option value="{esc(v)}">{esc(v)}</option>')
    return (
        f'<select id="{element_id}" class="{css_class}" '
        f'aria-label="Filter by {esc(all_label)}">'
        + "".join(opts) + "</select>"
    )
