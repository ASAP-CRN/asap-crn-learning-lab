"""
rosetta_helpers.py
Shared data-loading, curation logic, and HTML primitives for build_rosetta_stone.py.
"""

from pathlib import Path
import json
import re
import html as _html


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


def version_key(version):
    nums = re.findall(r"\d+", str(version))
    return tuple(int(n) for n in nums) if nums else (0,)


# ─────────────────────────────────────────────────────────────────────────────
# JSON loading
# ─────────────────────────────────────────────────────────────────────────────

def load_json(path):
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def deep_merge(base, extra):
    merged = dict(base)
    for k, v in extra.items():
        if k in merged and isinstance(merged[k], dict) and isinstance(v, dict):
            merged[k] = deep_merge(merged[k], v)
        else:
            merged[k] = v
    return merged


# ─────────────────────────────────────────────────────────────────────────────
# Collections index
# ─────────────────────────────────────────────────────────────────────────────

def load_collections_index(collections_file: Path) -> dict:
    """
    Load cloud-collections/collections.json.
    Returns a dict keyed by collection name.
    Accepts both list and dict shapes.
    """
    if not collections_file.exists():
        print(f"WARNING: Collections file not found: {collections_file}")
        return {}
    try:
        data = load_json(collections_file)
    except Exception as exc:
        print(f"WARNING: Could not load collections file: {exc}")
        return {}

    if isinstance(data, dict):
        result = {}
        for key, value in data.items():
            if isinstance(value, dict):
                rec = dict(value)
                rec.setdefault("name", key)
                result[key] = rec
        return result

    if isinstance(data, list):
        return {item["name"]: item for item in data if isinstance(item, dict) and item.get("name")}

    return {}


def get_collection_record(collections_index: dict, name: str) -> dict:
    if not name or name in ("NA", ""):
        return {}
    return collections_index.get(str(name).strip(), {})


def get_collection_top_doi(collections_index: dict, name: str) -> str:
    rec = get_collection_record(collections_index, name)
    return str(rec.get("collection_doi", "") or rec.get("doi", "") or "")


def get_collection_version_doi(collections_index: dict, name: str, version: str) -> str:
    rec = get_collection_record(collections_index, name)
    versions = rec.get("versions", {})
    if not isinstance(versions, dict):
        return ""
    entry = versions.get(str(version).strip(), {})
    return str(entry.get("doi", "") or "") if isinstance(entry, dict) else ""


# ─────────────────────────────────────────────────────────────────────────────
# Releases index  (cloud-releases/releases.json  — optional)
# ─────────────────────────────────────────────────────────────────────────────

def load_releases_index(releases_file: Path) -> dict:
    """
    Load cloud-releases/releases.json if it exists.
    Returns a dict keyed by release version string.
    """
    if not releases_file.exists():
        print(f"INFO: Releases file not found (optional): {releases_file}")
        return {}
    try:
        data = load_json(releases_file)
    except Exception as exc:
        print(f"WARNING: Could not load releases file: {exc}")
        return {}

    if isinstance(data, dict):
        result = {}
        for key, value in data.items():
            if isinstance(value, dict):
                rec = dict(value)
                rec.setdefault("version", key)
                result[key] = rec
        return result

    if isinstance(data, list):
        result = {}
        for item in data:
            if isinstance(item, dict) and item.get("version"):
                result[item["version"]] = item
        return result

    return {}


# ─────────────────────────────────────────────────────────────────────────────
# Dataset loading
# ─────────────────────────────────────────────────────────────────────────────

def find_dataset_detail_json(dataset_dir: Path, name: str):
    for candidate in [
        dataset_dir / f"{name}.json",
        dataset_dir / name / f"{name}.json",
        dataset_dir / name / "dataset.json",
    ]:
        if candidate.exists():
            return candidate
    return None


def normalize_dataset_index(data) -> list:
    records = []
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, dict):
                rec = dict(value)
                rec.setdefault("id", key)
                rec.setdefault("name", key)
                records.append(rec)
    elif isinstance(data, list):
        for item in data:
            if isinstance(item, dict):
                rec = dict(item)
                rec.setdefault("id", rec.get("name", "unknown"))
                records.append(rec)
    return records


def load_datasets(index_file: Path, dataset_dir: Path) -> list:
    index_records = normalize_dataset_index(load_json(index_file))
    results = []
    for rec in index_records:
        name        = get_dataset_id(rec)
        detail_file = find_dataset_detail_json(dataset_dir, name)
        if detail_file:
            try:
                detail = load_json(detail_file)
                # unwrap {"dataset-name": {...}} shape
                if isinstance(detail, dict) and name in detail and isinstance(detail[name], dict):
                    detail = detail[name]
                merged = deep_merge(rec, detail) if isinstance(detail, dict) else rec
                merged["_detail_file"] = str(detail_file)
            except Exception as exc:
                print(f"Could not load detail JSON for {name}: {exc}")
                merged = rec
                merged["_detail_file"] = ""
        else:
            print(f"No detail JSON found for {name}")
            merged = rec
            merged["_detail_file"] = ""
        merged["_index_file"] = str(index_file)
        results.append(merged)

    # Deduplicate, keeping first occurrence
    seen, deduped = set(), []
    for d in results:
        did = get_dataset_id(d)
        if did not in seen:
            seen.add(did)
            deduped.append(d)

    return sorted(deduped, key=lambda d: get_dataset_id(d).lower())


# ─────────────────────────────────────────────────────────────────────────────
# Dataset field accessors
# ─────────────────────────────────────────────────────────────────────────────

def get_dataset_id(d: dict) -> str:
    return str(d.get("id") or d.get("name") or "unknown-dataset")


def get_dataset_title(d: dict) -> str:
    return str(d.get("title") or d.get("dataset_title") or d.get("name") or get_dataset_id(d))


def get_tags(d: dict) -> list:
    tags     = d.get("tags", [])
    keywords = d.get("keywords", [])
    if not isinstance(tags, list):     tags     = [tags]
    if not isinstance(keywords, list): keywords = [keywords]
    return sorted(
        {str(t).strip() for t in tags + keywords if t is not None and str(t).strip()},
        key=str.lower,
    )


def get_curation(d: dict) -> dict:
    c = d.get("curation", {})
    return c if isinstance(c, dict) else {}


def get_collection_object(d: dict) -> dict:
    c = get_curation(d).get("collection", {})
    return c if isinstance(c, dict) else {}


def get_collection_name(d: dict) -> str:
    cur = get_curation(d)
    col = get_collection_object(d)
    if col.get("name"):        return str(col["name"])
    if cur.get("name"):        return str(cur["name"])
    raw = d.get("collection")
    if raw is None:            return "NA"
    if isinstance(raw, list):  return ", ".join(str(i) for i in raw) if raw else "NA"
    return str(raw).strip() or "NA"


def get_dataset_version(d: dict) -> str:
    cur = get_curation(d)
    if cur.get("dataset_version"): return str(cur["dataset_version"])
    if d.get("dataset_version"):   return str(d["dataset_version"])
    all_v = d.get("all_versions", [])
    if isinstance(all_v, list) and all_v:
        return str(sorted(all_v, key=version_key, reverse=True)[0])
    return "TBD"


def get_release_version(d: dict) -> str:
    """Return the materialized/curation release version for this dataset."""
    cur = get_curation(d)
    if cur.get("release_version"): return str(cur["release_version"])
    all_r = d.get("all_releases", [])
    if isinstance(all_r, list) and all_r:
        return str(sorted(all_r, key=version_key, reverse=True)[0])
    rels = d.get("releases", {})
    if isinstance(rels, dict) and rels:
        return str(sorted(rels.keys(), key=version_key, reverse=True)[0])
    return "TBD"


def get_collection_version(d: dict) -> str:
    cur = get_curation(d)
    col = get_collection_object(d)
    if col.get("version"):              return str(col["version"])
    if cur.get("collection_version"):   return str(cur["collection_version"])
    return "NA"


def get_collection_doi(d: dict, collections_index: dict) -> str:
    name = get_collection_name(d)
    top  = get_collection_top_doi(collections_index, name)
    if top:
        return top
    col = get_collection_object(d)
    cur = get_curation(d)
    return str(col.get("collection_doi", "") or cur.get("collection_doi", "") or "")


def get_curation_release_history(d: dict) -> dict:
    h = get_curation(d).get("releases", {})
    return h if isinstance(h, dict) else {}


def get_dataset_release_history(d: dict) -> dict:
    h = d.get("releases", {})
    return h if isinstance(h, dict) else {}


def get_all_releases(d: dict) -> list:
    v = d.get("all_releases", [])
    return [str(i) for i in v] if isinstance(v, list) else []


def get_all_versions(d: dict) -> list:
    v = d.get("all_versions", [])
    return [str(i) for i in v] if isinstance(v, list) else []


def get_cde_version(d: dict) -> str:
    """Return CDE version for the dataset's materialized release."""
    cur     = get_curation(d)
    rel_key = cur.get("release_version", "")
    hist    = get_dataset_release_history(d)
    return str(hist.get(rel_key, {}).get("cde_version", "") or "TBD")


# ─────────────────────────────────────────────────────────────────────────────
# Curation status
# ─────────────────────────────────────────────────────────────────────────────

def has_curation(d: dict) -> bool:
    cur = d.get("curation")
    if not isinstance(cur, dict) or not cur:
        return False
    return bool(cur.get("dataset_version") or cur.get("release_version"))


def all_releases_for_dataset(dataset: dict) -> list:
    """
    Return ALL release versions for this dataset, newest-first.
    Merges all_releases list + releases dict keys so nothing is missed.
    """
    from_list = set(str(r) for r in dataset.get("all_releases", []) if r)
    from_dict = set(get_dataset_release_history(dataset).keys())
    merged    = from_list | from_dict
    return sorted(merged, key=version_key, reverse=True)


def derive_curation_status(release_key: str, dataset: dict,
                            releases_newest_first: list = None) -> str:
    """
    Returns "added" | "updated" | "unchanged" | "not-curated".

    releases_newest_first is optional; if omitted it is derived from the dataset.

    Logic:
    - No meaningful curation block → not-curated
    - Release predates curation.release_version → not-curated
    - Release is not curation.release_version but follows it → unchanged
    - Release IS curation.release_version:
        - Any earlier release appears in curation.releases history → updated
        - Otherwise → added
    """
    if not has_curation(dataset):
        return "not-curated"

    if releases_newest_first is None:
        releases_newest_first = all_releases_for_dataset(dataset)

    # Ensure the release key is in the list so comparisons work
    all_keys = releases_newest_first
    if release_key not in all_keys:
        # Add it in sorted position so version comparisons are correct
        all_keys = sorted(set(releases_newest_first) | {release_key},
                          key=version_key, reverse=True)

    cur         = dataset.get("curation", {})
    cur_release = cur.get("release_version", "")

    if not cur_release:
        return "not-curated"

    if version_key(release_key) < version_key(cur_release):
        return "not-curated"
    if release_key != cur_release:
        return "unchanged"

    # This IS the curation release — determine added vs updated
    chronological = list(reversed(all_keys))   # oldest→newest
    idx           = chronological.index(release_key) if release_key in chronological else 0
    prior         = chronological[:idx]
    cur_rel_hist  = get_curation_release_history(dataset)
    prior_curated = [
        r for r in prior
        if r in cur_rel_hist
        or any(isinstance(v, dict) and v.get("release_version") == r
               for v in cur_rel_hist.values())
    ]
    return "updated" if prior_curated else "added"


# ─────────────────────────────────────────────────────────────────────────────
# Curation status badge  (inline styles so CSS file isn't required)
# ─────────────────────────────────────────────────────────────────────────────

_STATUS_CFG = {
    "added":       ("added",       "#e8f5ee", "#0d6b3f", "#6fcf97"),
    "updated":     ("updated",     "#e8f0fb", "#1a4fa0", "#7baee8"),
    "unchanged":   ("unchanged",   "#f0eeea", "#5a5850", "#bbb9b0"),
    "not-curated": ("not curated", "#fef3e2", "#8a5a00", "#f0b429"),
}


def curation_badge_html(status: str) -> str:
    label, bg, color, border = _STATUS_CFG.get(status, _STATUS_CFG["not-curated"])
    dot = (
        f'<span style="display:inline-block;width:6px;height:6px;border-radius:50%;'
        f'background:{color};margin-right:4px;vertical-align:middle"></span>'
    )
    return (
        f'<span class="rs-badge rs-badge--{esc(status)}" '
        f'style="display:inline-flex;align-items:center;font-size:0.72rem;padding:2px 8px;'
        f'border-radius:3px;font-weight:500;white-space:nowrap;font-family:monospace;'
        f'background:{bg};color:{color};border:1px solid {border}">'
        f'{dot}{esc(label)}</span>'
    )


# ─────────────────────────────────────────────────────────────────────────────
# Shared HTML fragments reused across all three pages
# ─────────────────────────────────────────────────────────────────────────────

def badge_latest_html() -> str:
    return '<span class="rs-latest-badge">latest</span>'


def render_bucket_rows(buckets: dict) -> str:
    """Render prod + raw bucket rows with copy buttons. UAT/DEV excluded."""
    env_order  = ["prod", "raw"]
    env_colors = {"prod": "#0d6b3f", "raw": "#5a5850"}
    filtered   = {k: v for k, v in buckets.items() if k in env_order}

    if not filtered:
        return '<div class="rs-no-buckets">No bucket paths listed.</div>'

    rows = []
    for env in sorted(filtered, key=lambda e: env_order.index(e)):
        path  = filtered[env]
        color = env_colors.get(env, "#5a5850")
        rows.append(
            f'<div class="rs-env-row">'
            f'<span class="rs-env-dot" style="background:{color}"></span>'
            f'<span class="rs-env-name" style="color:{color}">{esc(env)}</span>'
            f'<span class="rs-env-path">{esc(path)}</span>'
            f'<button class="rs-copy-btn" data-path="{esc(path)}" onclick="rsCopyPath(this)">Copy</button>'
            f'</div>'
        )
    return "".join(rows)


def render_curation_card(dataset: dict, collections_index: dict) -> str:
    """
    Static curation details card — shows fixed curation block data.
    No per-release switching. If no curation, shows empty state.
    """
    if not has_curation(dataset):
        return (
            '<div class="rs-card">'
            '<div class="rs-card-header">'
            '<span class="rs-card-title">Curation details</span>'
            f'{curation_badge_html("not-curated")}'
            '</div>'
            '<div class="rs-no-curation">'
            '<span class="rs-no-curation-icon">∅</span>'
            '<p>No curation files have been produced for this dataset.</p>'
            '</div></div>'
        )

    cur     = get_curation(dataset)
    col_obj = get_collection_object(dataset)
    hist    = get_dataset_release_history(dataset)

    ds_ver      = esc(cur.get("dataset_version", "TBD"))
    rel_ver     = esc(cur.get("release_version",  "TBD"))
    cur_rel_key = cur.get("release_version", "")
    cde_ver     = esc(hist.get(cur_rel_key, {}).get("cde_version") or "TBD")

    col_ver  = col_obj.get("version") or cur.get("collection_version") or None
    col_name_val = col_obj.get("name") or cur.get("name") or None
    col_name_cell = esc(col_name_val) if col_name_val else '<span class="rs-na">—</span>'
    col_ver_cell  = (
        f'<span class="rs-mono">{esc(col_ver)}</span>' if col_ver
        else '<span class="rs-na">—</span>'
    )

    col_name_str = get_collection_name(dataset)
    col_doi      = get_collection_top_doi(collections_index, col_name_str)
    if not col_doi:
        col_doi = col_obj.get("collection_doi") or cur.get("collection_doi") or ""
    col_ver_doi = get_collection_version_doi(collections_index, col_name_str, col_ver) if col_ver else ""

    # Derive status using the full release list
    all_rels = all_releases_for_dataset(dataset)
    status   = derive_curation_status(cur_rel_key, dataset, all_rels)
    badge    = curation_badge_html(status)

    def field(label, value_html):
        return (
            f'<div class="rs-field">'
            f'<span class="rs-field-label">{label}</span>'
            f'<span class="rs-field-value">{value_html}</span>'
            f'</div>'
        )

    body = "".join([
        field("Dataset version",        f'<span class="rs-highlight rs-mono">{ds_ver}</span>'),
        field("Release",                f'<span class="rs-highlight rs-mono">{rel_ver}</span>'),
        field("CDE version",            f'<span class="rs-mono">{cde_ver}</span>'),
        field("Collection",             col_name_cell),
        field("Collection version",     col_ver_cell),
        field("Collection DOI",         doi_link_or(col_doi, "TBD")),
        field("Collection version DOI", doi_link_or(col_ver_doi, "—")),
    ])

    return (
        f'<div class="rs-card">'
        f'<div class="rs-card-header">'
        f'<span class="rs-card-title">Curation details</span>'
        f'</div>'
        f'<div class="rs-card-body">{body}</div>'
        f'</div>'
    )


def render_bucket_card(buckets: dict) -> str:
    """Static bucket access card — always shows prod + raw."""
    return (
        '<div class="rs-card">'
        '<div class="rs-card-header">'
        '<span class="rs-card-title">Bucket access</span>'
        '</div>'
        f'<div class="rs-card-body rs-bucket-body">'
        f'{render_bucket_rows(buckets)}'
        f'</div></div>'
    )


def render_full_history_table(releases_sorted: list, dataset: dict,
                              collections_index: dict,
                              releases_index: dict = None) -> str:
    """Full release history table — static, no row interactivity."""
    hist      = get_dataset_release_history(dataset)
    cur_hist  = get_curation_release_history(dataset)
    col_name  = get_collection_name(dataset)
    all_rels  = all_releases_for_dataset(dataset)
    rows      = []
    if releases_index is None:
        releases_index = {}

    for i, rk in enumerate(releases_sorted):
        info        = hist.get(rk, {})
        status      = derive_curation_status(rk, dataset, all_rels)
        badge       = curation_badge_html(status)
        ds_ver      = info.get("dataset_version", "TBD")
        cde_ver     = info.get("cde_version",     "TBD")
        is_latest   = (i == 0)
        latest_html = badge_latest_html() if is_latest else ""

        col_ver = "—"
        col_doi = ""
        for ck, ci in cur_hist.items():
            if isinstance(ci, dict) and ci.get("release_version") == rk:
                col_ver = ci.get("collection_version", ck) or "—"
                # Enrich DOI: collections_index first, then curation block
                col_doi = get_collection_version_doi(collections_index, col_name, col_ver)
                if not col_doi:
                    col_doi = ci.get("collection_version_doi", "")
                break

        # Enrich release DOI from releases_index if available
        rel_doi = ""
        rel_rec = releases_index.get(rk, {})
        if isinstance(rel_rec, dict):
            rel_doi = str(rel_rec.get("doi", "") or "")

        rows.append(
            f'<tr>'
            f'<td><span class="rs-mono">{esc(rk)}</span> {latest_html}</td>'
            f'<td><span class="rs-mono">{esc(ds_ver)}</span></td>'
            f'<td><span class="rs-mono">{esc(col_ver)}</span></td>'
            f'<td>{doi_link_or(col_doi, "—")}</td>'
            f'<td><span class="rs-mono">{esc(cde_ver)}</span></td>'
            f'<td>{doi_link_or(rel_doi, "—")}</td>'
            f'<td>{badge}</td>'
            f'</tr>'
        )

    empty = '<tr><td colspan="7">No release history listed.</td></tr>'
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


def render_collection_release_history(dataset: dict, collections_index: dict) -> str:
    cur_hist = get_curation_release_history(dataset)
    if not cur_hist:
        return ""
    col_name = get_collection_name(dataset)
    rows = []
    for ck in sorted(cur_hist.keys(), key=version_key, reverse=True):
        ci = cur_hist.get(ck, {})
        if not isinstance(ci, dict):
            ci = {}
        col_ver = ci.get("collection_version", ck)
        rel_ver = ci.get("release_version", "TBD")
        col_doi = get_collection_version_doi(collections_index, col_name, col_ver)
        if not col_doi:
            col_doi = ci.get("collection_version_doi", "")
        rows.append(
            f'<tr><td>{esc(col_ver)}</td><td>{esc(rel_ver)}</td>'
            f'<td>{doi_link_or(col_doi, "—")}</td></tr>'
        )
    return (
        '<div class="rs-section">'
        '<div class="rs-section-header">Collection release history</div>'
        '<div class="rs-card rs-card--table">'
        '<table class="rs-mini-table">'
        '<thead><tr>'
        '<th>Collection version</th><th>Release version</th><th>Collection version DOI</th>'
        '</tr></thead>'
        f'<tbody>{"".join(rows)}</tbody>'
        '</table></div></div>'
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


# ─────────────────────────────────────────────────────────────────────────────
# Status legend (shared across pages)
# ─────────────────────────────────────────────────────────────────────────────

LEGEND_HTML = """
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
"""
