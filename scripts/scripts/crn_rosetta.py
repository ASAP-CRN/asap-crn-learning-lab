"""
crn_rosetta.py — queryable catalog of CRN Cloud datasets, releases and collections.

This is the data layer behind the Learning Lab "Rosetta Stone" pages. It has no
HTML in it and no dependencies outside the standard library (pandas is optional,
only for ``Catalog.to_frame``), so it can be imported on its own:

    from crn_rosetta import Catalog

    cat = Catalog.from_github()            # reads the three index files from GitHub
    cat = Catalog.from_local("..")         # or from sibling clones of the cloud-* repos

    cat.latest_release                     # 'v5.1.0'
    ds = cat.dataset("hafler-pmdbs-sn-rnaseq-pfc")
    cat.status(ds, "v5.0.0")               # 'unchanged'
    cat.paths(ds)["curated"]               # gs://…/pmdbs_sc_rnaseq/release/v3.0.0
    cat.datasets(collection="pmdbs-sc-rnaseq", release="v4.0.0")
    cat.diff("v5.0.0", "v5.1.0")
    cat.to_frame("release_datasets")       # one row per dataset per release

Where each fact comes from
--------------------------
cloud-datasets/datasets.json        what a dataset is, its version history, and its
                                    curation records (workflow, bucket paths)
cloud-releases/releases.json        which datasets and collection versions are in each
                                    release, which datasets changed, CDE version, DOI
cloud-collections/collections.json  collection titles, DOIs and version history

Curation status of a dataset in a release
-----------------------------------------
A dataset has a curation record for every release in which its curated outputs were
produced. For release R, the record that applies is the newest one at or before R:

    added        outputs were produced in R, for the first time
    updated      outputs were produced in R, and an earlier record exists
    unchanged    the dataset is in R but its outputs resolve to an earlier release path
    not-curated  no curation record at or before R
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Union

__all__ = [
    "Catalog", "Dataset", "CurationRecord", "Release", "VersionRef",
    "Collection", "CollectionVersion", "Issue", "version_key",
]

GITHUB_ORG = "ASAP-CRN"
REPOS = {
    "datasets":    ("cloud-datasets",    "datasets.json"),
    "releases":    ("cloud-releases",    "releases.json"),
    "collections": ("cloud-collections", "collections.json"),
}
STATUSES = ("added", "updated", "unchanged", "not-curated")

_RELEASE_RE        = re.compile(r"^v\d+\.\d+\.\d+$")
_BUCKET_RELEASE_RE = re.compile(r"/release/(v\d+\.\d+\.\d+)/?$")
_BUCKET_COLLECTION_RE = re.compile(r"^gs://asap-crn-(.+)-collection-v[\w.]+/")
_CURATION_CORE = {
    "workflow", "workflow_version", "workflow_url", "collection_version",
    "collection_version_doi", "gcp_uri",
}


def version_key(version: Any) -> tuple:
    """Sort key for 'v4.1.0'-style strings. Compares numerically, not as text."""
    nums = re.findall(r"\d+", str(version))
    return tuple(int(n) for n in nums) if nums else (0,)


# ─────────────────────────────────────────────────────────────────────────────
# Records
# ─────────────────────────────────────────────────────────────────────────────

@dataclass(frozen=True)
class Issue:
    """One inconsistency found in the source JSON. See ``Catalog.validate``."""
    repo: str
    subject: str
    message: str

    def __str__(self) -> str:
        return f"[{self.repo}] {self.subject}: {self.message}"


@dataclass(frozen=True)
class VersionRef:
    """A version of something as pinned by a release, with the DOI the release lists."""
    version: str
    doi: str = ""


@dataclass(frozen=True)
class CurationRecord:
    """Curated outputs produced for one dataset in one release."""
    release: str                 # release whose path holds these outputs
    workflow: str
    workflow_version: str
    workflow_url: str
    collection: str              # collection the outputs were published into
    collection_version: str      # that collection's version at the time
    collection_version_doi: str
    dataset_bucket: str          # gs://asap-curated-…/<workflow>/release/<release>
    collection_bucket: str       # gs://asap-crn-<collection>-collection-…/<dataset>/…
    components: Dict[str, str]   # per-step versions, e.g. preprocess_cellranger
    raw: Dict[str, Any] = field(repr=False, compare=False, default_factory=dict)


@dataclass
class Dataset:
    name: str
    title: str
    description: str
    short_description: str
    doi: str
    version: str                         # current dataset version
    all_versions: List[str]
    license: str
    keywords: List[str]
    creators: List[Dict[str, Any]]
    team: str                            # first token of the name, e.g. 'hafler', 'cohort'
    collection: Optional[str]            # see Catalog docs for how this is resolved
    buckets: Dict[str, str]              # raw / dev / uat / prod
    version_changes: Dict[str, str]      # release -> dataset version, for releases where it was added or updated
    curation: Dict[str, CurationRecord]  # release -> record, oldest first; only releases with outputs
    raw: Dict[str, Any] = field(repr=False, default_factory=dict)

    @property
    def is_curated(self) -> bool:
        return bool(self.curation)

    @property
    def latest_curation(self) -> Optional[CurationRecord]:
        return next(reversed(list(self.curation.values())), None)

    def __repr__(self) -> str:
        return f"Dataset({self.name!r}, version={self.version!r}, collection={self.collection!r})"


@dataclass
class Release:
    version: str
    cde_version: str
    doi: str
    created: str                         # when the JSON record was written; not a reliable release date
    datasets: Dict[str, VersionRef]      # every dataset in the release -> its version then
    changed: List[str]                   # datasets added or updated in this release
    collections: Dict[str, VersionRef]   # collection -> its version in this release
    raw: Dict[str, Any] = field(repr=False, default_factory=dict)

    def __repr__(self) -> str:
        return (f"Release({self.version!r}, cde={self.cde_version!r}, "
                f"datasets={len(self.datasets)}, collections={len(self.collections)})")


@dataclass(frozen=True)
class CollectionVersion:
    version: str
    doi: str
    date: str
    datasets: List[str]
    release: str                         # release this version was published with
    cde_version: str


@dataclass
class Collection:
    name: str
    title: str
    doi: str                             # concept DOI (all versions)
    version: str                         # current version
    version_doi: str
    date: str
    types: List[str]
    teams: List[str]
    datasets: List[str]                  # members of the current version, as listed in cloud-collections
    release: str
    cde_version: str
    versions: Dict[str, CollectionVersion]   # oldest first
    raw: Dict[str, Any] = field(repr=False, default_factory=dict)

    def __repr__(self) -> str:
        return f"Collection({self.name!r}, version={self.version!r}, datasets={len(self.datasets)})"


# ─────────────────────────────────────────────────────────────────────────────
# Parsing
# ─────────────────────────────────────────────────────────────────────────────

def _s(value: Any) -> str:
    return "" if value is None else str(value).strip()


def _str_list(value: Any) -> List[str]:
    if value is None:
        return []
    if not isinstance(value, (list, tuple)):
        value = [value]
    seen, out = set(), []
    for item in value:
        text = _s(item)
        if text and text not in seen:
            seen.add(text)
            out.append(text)
    return out


def _keyed(data: Any, key: str = "name") -> Dict[str, dict]:
    """Accept {'name': {...}} or [{'name': ..., ...}] and return the dict form."""
    if isinstance(data, dict):
        return {k: v for k, v in data.items() if isinstance(v, dict)}
    if isinstance(data, list):
        return {_s(i.get(key)): i for i in data if isinstance(i, dict) and i.get(key)}
    return {}


def _version_refs(data: Any) -> Dict[str, VersionRef]:
    out = {}
    for name, item in _keyed(data).items():
        ver = item.get("dataset_version") or item.get("version")
        out[name] = VersionRef(_s(ver), _s(item.get("doi")))
    return out


def _parse_curation(name: str, raw: Any, issues: List[Issue]) -> Dict[str, CurationRecord]:
    entries = raw.items() if isinstance(raw, dict) else []
    # Well-formed keys first, so a stray duplicate never displaces a proper entry.
    entries = sorted(entries, key=lambda kv: not _RELEASE_RE.match(str(kv[0])))
    out: Dict[str, CurationRecord] = {}
    for key, rec in entries:
        if not isinstance(rec, dict) or not rec:
            continue                      # {} means: touched in this release, no new outputs
        gcp = rec.get("gcp_uri") if isinstance(rec.get("gcp_uri"), dict) else {}
        ds_bucket, col_bucket = _s(gcp.get("dataset_bucket")), _s(gcp.get("collection_bucket"))
        m = _BUCKET_RELEASE_RE.search(ds_bucket)
        path_release = m.group(1) if m else ""

        release = str(key)
        if not _RELEASE_RE.match(release):
            if not path_release:
                issues.append(Issue("cloud-datasets", name,
                    f"curation key {key!r} is not a release version and its bucket path "
                    f"names no release; entry ignored"))
                continue
            release = path_release
            if release in out and out[release].raw == rec:
                issues.append(Issue("cloud-datasets", name,
                    f"curation key {key!r} is not a release version; it duplicates the "
                    f"{release} entry and was ignored"))
                continue
            issues.append(Issue("cloud-datasets", name,
                f"curation key {key!r} is not a release version; read as {release} "
                f"from its dataset_bucket path"))
        elif path_release and path_release != release:
            issues.append(Issue("cloud-datasets", name,
                f"curation {release}: dataset_bucket path ends in release/{path_release}"))

        if release in out:
            issues.append(Issue("cloud-datasets", name,
                f"two different curation entries resolve to {release}; kept the one keyed {release}"))
            continue

        workflow = _s(rec.get("workflow"))
        m = _BUCKET_COLLECTION_RE.match(col_bucket)
        collection = m.group(1) if m else workflow
        if m and workflow and workflow != collection:
            issues.append(Issue("cloud-datasets", name,
                f"curation {release}: workflow is {workflow!r} but collection_bucket is in "
                f"{collection!r}; using {collection!r} as the collection"))
        url = _s(rec.get("workflow_url"))
        if url and not url.startswith(("http://", "https://")):
            url = "https://" + url
        out[release] = CurationRecord(
            release=release,
            workflow=workflow,
            workflow_version=_s(rec.get("workflow_version")),
            workflow_url=url,
            collection=collection,
            collection_version=_s(rec.get("collection_version")),
            collection_version_doi=_s(rec.get("collection_version_doi")),
            dataset_bucket=ds_bucket,
            collection_bucket=col_bucket,
            components={k: _s(v) for k, v in rec.items()
                        if k not in _CURATION_CORE and not isinstance(v, (dict, list))},
            raw=rec,
        )
    return dict(sorted(out.items(), key=lambda kv: version_key(kv[0])))


def _parse_dataset(name: str, raw: dict, issues: List[Issue]) -> Dataset:
    curation = _parse_curation(name, raw.get("curation"), issues)
    declared = raw.get("collection")
    if isinstance(declared, list):
        declared = declared[0] if declared else None
    declared = _s(declared) or None
    inferred = next(reversed(list(curation.values()))).collection if curation else None
    if not declared and inferred:
        issues.append(Issue("cloud-datasets", name,
            f"'collection' is null but the dataset has curated outputs in {inferred!r}; "
            f"treated as a member of {inferred!r}"))
    elif declared and inferred and declared != inferred:
        issues.append(Issue("cloud-datasets", name,
            f"'collection' is {declared!r} but its latest curated outputs are in {inferred!r}"))

    changes = raw.get("releases") if isinstance(raw.get("releases"), dict) else {}
    # Older schema stored {'dataset_version': ..} per release; accept both.
    changes = {str(r): _s(v.get("dataset_version") if isinstance(v, dict) else v)
               for r, v in changes.items()}
    all_versions = sorted(_str_list(raw.get("all_versions")), key=version_key)
    version = _s(raw.get("version")) or (all_versions[-1] if all_versions else "")
    buckets = raw.get("buckets") if isinstance(raw.get("buckets"), dict) else {}
    creators = raw.get("creators") if isinstance(raw.get("creators"), list) else []

    return Dataset(
        name=name,
        title=_s(raw.get("title") or raw.get("dataset_title") or name),
        description=_s(raw.get("description")),
        short_description=_s(raw.get("short_description")),
        doi=_s(raw.get("doi")),
        version=version,
        all_versions=all_versions,
        license=_s(raw.get("license")),
        keywords=_str_list(raw.get("keywords")),
        creators=[c for c in creators if isinstance(c, dict)],
        team=name.split("-")[0],
        collection=declared or inferred,
        buckets={str(k): _s(v) for k, v in buckets.items()},
        version_changes=dict(sorted(changes.items(), key=lambda kv: version_key(kv[0]))),
        curation=curation,
        raw=raw,
    )


def _parse_release(version: str, raw: dict) -> Release:
    datasets = _version_refs(raw.get("datasets") or raw.get("all_datasets"))
    changed = raw.get("new_datasets") or []
    changed = [_s(i.get("name") if isinstance(i, dict) else i) for i in changed]
    return Release(
        version=version,
        cde_version=_s(raw.get("cde_version")),
        doi=_s(raw.get("release_doi") or raw.get("doi")),
        created=_s(raw.get("created")),
        datasets=datasets,
        changed=[n for n in dict.fromkeys(changed) if n],
        collections=_version_refs(raw.get("collections") or raw.get("all_collections")),
        raw=raw,
    )


def _parse_collection(name: str, raw: dict) -> Collection:
    def rel(d: Any, key: str) -> str:
        return _s(d.get(key)) if isinstance(d, dict) else ""

    versions = {}
    for ver, v in _keyed(raw.get("versions")).items():
        versions[ver] = CollectionVersion(
            version=ver, doi=_s(v.get("doi")), date=_s(v.get("date")),
            datasets=_str_list(v.get("datasets")),
            release=rel(v.get("release"), "version"),
            cde_version=rel(v.get("release"), "cde_version"),
        )
    versions = dict(sorted(versions.items(), key=lambda kv: version_key(kv[0])))
    version = _s(raw.get("version") or raw.get("current_version")) or next(reversed(list(versions)), "")
    return Collection(
        name=name,
        title=_s(raw.get("title") or name),
        doi=_s(raw.get("collection_doi")),
        version=version,
        version_doi=_s(raw.get("doi")),
        date=_s(raw.get("date")),
        types=_str_list(raw.get("types")),
        teams=_str_list(raw.get("teams")),
        datasets=_str_list(raw.get("datasets")),
        release=rel(raw.get("release"), "version"),
        cde_version=rel(raw.get("release"), "cde_version"),
        versions=versions,
        raw=raw,
    )


# ─────────────────────────────────────────────────────────────────────────────
# Catalog
# ─────────────────────────────────────────────────────────────────────────────

DatasetLike = Union[str, Dataset]


class Catalog:
    """
    All datasets, releases and collections, with the cross-references resolved.

    Build one with ``Catalog.from_local`` or ``Catalog.from_github``.

    A dataset's collection is the ``collection`` field of its cloud-datasets record.
    Where that is null but the dataset has curated outputs, the collection is read
    from the bucket those outputs were published into. Collection membership
    (``collection_members``) follows from that, so it can differ from the ``datasets``
    list in cloud-collections; ``validate()`` reports every such difference.
    """

    def __init__(self, datasets: Any, releases: Any, collections: Any,
                 source: str = "", local_repos: Optional[Dict[str, Path]] = None):
        self.source = source
        self._local = local_repos or {}
        self._issues: List[Issue] = []
        self._datasets = {
            n: _parse_dataset(n, r, self._issues)
            for n, r in sorted(_keyed(datasets).items(), key=lambda kv: kv[0].lower())
        }
        self._releases = {
            v: _parse_release(v, r)
            for v, r in sorted(_keyed(releases, "release_version").items(),
                               key=lambda kv: version_key(kv[0]))
        }
        self._collections = {
            n: _parse_collection(n, r)
            for n, r in sorted(_keyed(collections).items(), key=lambda kv: kv[0].lower())
        }
        if not self._datasets:
            raise ValueError("No datasets found in the dataset index.")
        if not self._releases:
            raise ValueError("No releases found in the release index.")

    # ── Constructors ─────────────────────────────────────────────────────────

    @classmethod
    def from_local(cls, root: Union[str, Path] = "..", *,
                   datasets_repo: Union[str, Path, None] = None,
                   releases_repo: Union[str, Path, None] = None,
                   collections_repo: Union[str, Path, None] = None) -> "Catalog":
        """Load from local clones. ``root`` is the directory holding the three cloud-* repos."""
        root = Path(root).expanduser().resolve()
        overrides = {"datasets": datasets_repo, "releases": releases_repo,
                     "collections": collections_repo}
        repos, loaded = {}, {}
        for kind, (repo, index) in REPOS.items():
            path = Path(overrides[kind]).expanduser().resolve() if overrides[kind] else root / repo
            if not (path / index).exists():
                raise FileNotFoundError(
                    f"{path / index} not found. Clone https://github.com/{GITHUB_ORG}/{repo} "
                    f"into {root}, point to the folder holding the clones (--root on the "
                    f"command line), or use Catalog.from_github() / --github.")
            repos[kind] = path
            loaded[kind] = json.loads((path / index).read_text(encoding="utf-8"))
        return cls(loaded["datasets"], loaded["releases"], loaded["collections"],
                   source=str(root), local_repos=repos)

    @classmethod
    def from_github(cls, ref: str = "main", *, org: str = GITHUB_ORG,
                    timeout: float = 30.0) -> "Catalog":
        """Load the three index files straight from GitHub (three requests, no clone needed)."""
        from urllib.request import urlopen

        loaded = {}
        for kind, (repo, index) in REPOS.items():
            url = f"https://raw.githubusercontent.com/{org}/{repo}/{ref}/{index}"
            with urlopen(url, timeout=timeout) as resp:      # noqa: S310 (fixed https host)
                loaded[kind] = json.loads(resp.read().decode("utf-8"))
        return cls(loaded["datasets"], loaded["releases"], loaded["collections"],
                   source=f"github:{org}@{ref}")

    def __repr__(self) -> str:
        return (f"Catalog({len(self._datasets)} datasets, {len(self._releases)} releases, "
                f"{len(self._collections)} collections, latest={self.latest_release!r})")

    # ── Lookups ──────────────────────────────────────────────────────────────

    @property
    def release_versions(self) -> List[str]:
        """Release versions, oldest first."""
        return list(self._releases)

    @property
    def latest_release(self) -> str:
        return self.release_versions[-1]

    @property
    def collection_names(self) -> List[str]:
        return list(self._collections)

    @property
    def dataset_names(self) -> List[str]:
        return list(self._datasets)

    def dataset(self, name: DatasetLike) -> Dataset:
        if isinstance(name, Dataset):
            return name
        try:
            return self._datasets[name]
        except KeyError:
            raise KeyError(f"Unknown dataset {name!r}{self._suggest(name, self._datasets)}") from None

    def release(self, version: Optional[str] = None) -> Release:
        version = version or self.latest_release
        try:
            return self._releases[version]
        except KeyError:
            raise KeyError(f"Unknown release {version!r}. Known: {', '.join(self._releases)}") from None

    def collection(self, name: str) -> Collection:
        try:
            return self._collections[name]
        except KeyError:
            raise KeyError(f"Unknown collection {name!r}. Known: {', '.join(self._collections)}") from None

    def releases(self) -> List[Release]:
        """All releases, oldest first."""
        return list(self._releases.values())

    def collections(self) -> List[Collection]:
        return list(self._collections.values())

    @staticmethod
    def _suggest(name: str, pool: Iterable[str]) -> str:
        import difflib
        close = difflib.get_close_matches(str(name), list(pool), n=3)
        return f". Did you mean: {', '.join(close)}?" if close else ""

    # ── Queries ──────────────────────────────────────────────────────────────

    def datasets(self, *, release: Optional[str] = None, collection: Optional[str] = None,
                 team: Optional[str] = None, keyword: Optional[str] = None,
                 curated: Optional[bool] = None, changed_in: Optional[str] = None,
                 search: Optional[str] = None) -> List[Dataset]:
        """
        Datasets matching every filter given, sorted by name.

        release     included in this release
        collection  member of this collection
        team        e.g. 'hafler' (first token of the dataset name)
        keyword     exact keyword, case-insensitive
        curated     True: has curated outputs (as of ``release`` if given). False: has none.
        changed_in  dataset version added/updated, or curated outputs produced, in this release
        search      substring of name, title, description, keywords or DOI
        """
        out = []
        in_release = set(self.release(release).datasets) if release else None
        in_changed = self.release(changed_in) if changed_in else None
        needle = search.lower() if search else None
        for ds in self._datasets.values():
            if in_release is not None and ds.name not in in_release:
                continue
            if collection is not None and ds.collection != collection:
                continue
            if team is not None and ds.team != team.lower():
                continue
            if keyword is not None and keyword.lower() not in (k.lower() for k in ds.keywords):
                continue
            if curated is not None and bool(self.curation(ds, release)) != curated:
                continue
            if in_changed is not None and not (
                    ds.name in in_changed.changed or in_changed.version in ds.curation):
                continue
            if needle is not None and needle not in " ".join(
                    [ds.name, ds.title, ds.description, ds.doi, *ds.keywords]).lower():
                continue
            out.append(ds)
        return out

    def collection_members(self, name: str, release: Optional[str] = None) -> List[Dataset]:
        """Datasets belonging to a collection, optionally only those present in a release."""
        self.collection(name)
        return self.datasets(collection=name, release=release)

    def first_release(self, dataset: DatasetLike) -> Optional[str]:
        """Earliest release that includes the dataset."""
        name = self.dataset(dataset).name
        return next((v for v, r in self._releases.items() if name in r.datasets), None)

    def releases_including(self, dataset: DatasetLike) -> List[str]:
        """Every release that includes the dataset, oldest first."""
        name = self.dataset(dataset).name
        return [v for v, r in self._releases.items() if name in r.datasets]

    def dataset_version(self, dataset: DatasetLike, release: Optional[str] = None) -> Optional[str]:
        """The dataset's version as of a release (None if it is not in that release)."""
        ref = self.release(release).datasets.get(self.dataset(dataset).name)
        return ref.version if ref else None

    def collection_version(self, collection: str, release: Optional[str] = None) -> Optional[str]:
        """The collection's version in a release (None if the release does not include it)."""
        ref = self.release(release).collections.get(collection)
        return ref.version if ref else None

    def collection_version_doi(self, collection: str, version: str) -> str:
        """DOI of one collection version, from cloud-collections ('' if not recorded)."""
        col = self._collections.get(collection)
        cv = col.versions.get(version) if col else None
        return cv.doi if cv else ""

    def change(self, dataset: DatasetLike, release: Optional[str] = None) -> Optional[str]:
        """'new' or 'updated' if the dataset version changed in this release, else None."""
        ds, rel = self.dataset(dataset), self.release(release)
        if ds.name not in rel.changed:
            return None
        return "new" if self.first_release(ds) == rel.version else "updated"

    def curation(self, dataset: DatasetLike, release: Optional[str] = None) -> Optional[CurationRecord]:
        """The curation record that applies in a release: the newest one at or before it."""
        ds = self.dataset(dataset)
        limit = version_key(self.release(release).version)
        found = None
        for rel, rec in ds.curation.items():
            if version_key(rel) <= limit:
                found = rec
        return found

    def status(self, dataset: DatasetLike, release: Optional[str] = None) -> Optional[str]:
        """
        Curation status of a dataset in a release: 'added', 'updated', 'unchanged'
        or 'not-curated'. None if the dataset is not in that release.
        """
        ds, rel = self.dataset(dataset), self.release(release)
        if ds.name not in rel.datasets:
            return None
        rec = self.curation(ds, rel.version)
        if rec is None:
            return "not-curated"
        if rec.release != rel.version:
            return "unchanged"
        return "updated" if next(iter(ds.curation)) != rec.release else "added"

    def paths(self, dataset: DatasetLike, release: Optional[str] = None) -> Dict[str, Optional[str]]:
        """
        Bucket paths for a dataset as of a release.

        raw / prod   the dataset's own buckets
        curated      curated outputs for this release (may sit under an earlier release path)
        collection   the same outputs inside the collection bucket
        curated_release  the release named in the curated path
        """
        ds = self.dataset(dataset)
        rec = self.curation(ds, release)
        return {
            "raw": ds.buckets.get("raw") or None,
            "prod": ds.buckets.get("prod") or None,
            "curated": rec.dataset_bucket if rec else None,
            "collection": rec.collection_bucket if rec else None,
            "curated_release": rec.release if rec else None,
        }

    # ── Row-shaped views ─────────────────────────────────────────────────────

    def _row(self, ds: Dataset, rel: Release) -> Dict[str, Any]:
        rec = self.curation(ds, rel.version)
        return {
            "release": rel.version,
            "dataset": ds.name,
            "team": ds.team,
            "dataset_version": rel.datasets[ds.name].version,
            "change": self.change(ds, rel.version),
            "collection": rec.collection if rec else None,
            "collection_version": self.collection_version(rec.collection, rel.version) if rec else None,
            "cde_version": rel.cde_version,
            "status": self.status(ds, rel.version),
            "curated_release": rec.release if rec else None,
            "workflow": rec.workflow if rec else None,
            "workflow_version": rec.workflow_version if rec else None,
            "curated_path": rec.dataset_bucket if rec else None,
            "collection_path": rec.collection_bucket if rec else None,
        }

    def release_view(self, release: Optional[str] = None) -> List[Dict[str, Any]]:
        """One row per dataset in a release."""
        rel = self.release(release)
        return [self._row(self._datasets[n], rel) for n in sorted(rel.datasets, key=str.lower)
                if n in self._datasets]

    def history(self, dataset: DatasetLike) -> List[Dict[str, Any]]:
        """One row per release that includes the dataset, oldest first."""
        ds = self.dataset(dataset)
        return [self._row(ds, self._releases[v]) for v in self.releases_including(ds)]

    def diff(self, old: str, new: str) -> Dict[str, list]:
        """What differs between two releases."""
        a, b = self.release(old), self.release(new)
        both = sorted(set(a.datasets) & set(b.datasets), key=str.lower)
        known = [n for n in both if n in self._datasets]
        return {
            "datasets_added":   sorted(set(b.datasets) - set(a.datasets), key=str.lower),
            "datasets_removed": sorted(set(a.datasets) - set(b.datasets), key=str.lower),
            "dataset_versions": [(n, a.datasets[n].version, b.datasets[n].version)
                                 for n in both if a.datasets[n].version != b.datasets[n].version],
            "curation":         [(n, getattr(self.curation(n, a.version), "release", None),
                                  getattr(self.curation(n, b.version), "release", None))
                                 for n in known
                                 if self.curation(n, a.version) != self.curation(n, b.version)],
            "collections":      [(c, getattr(a.collections.get(c), "version", None),
                                  getattr(b.collections.get(c), "version", None))
                                 for c in sorted(set(a.collections) | set(b.collections))
                                 if a.collections.get(c) != b.collections.get(c)],
            "cde_version":      [a.cde_version, b.cde_version] if a.cde_version != b.cde_version else [],
        }

    def to_records(self, table: str = "datasets") -> List[Dict[str, Any]]:
        """
        Flat rows for one of:
          'datasets'          one row per dataset, as of the latest release
          'releases'          one row per release
          'collections'       one row per collection version
          'release_datasets'  one row per dataset per release
        """
        if table == "datasets":
            rows = []
            for ds in self._datasets.values():
                rec = ds.latest_curation
                rows.append({
                    "dataset": ds.name, "title": ds.title, "team": ds.team,
                    "collection": ds.collection, "dataset_version": ds.version,
                    "doi": ds.doi, "license": ds.license, "keywords": list(ds.keywords),
                    "first_release": self.first_release(ds),
                    "status": self.status(ds),
                    "curated_release": rec.release if rec else None,
                    "workflow": rec.workflow if rec else None,
                    "workflow_version": rec.workflow_version if rec else None,
                    "raw_bucket": ds.buckets.get("raw"), "prod_bucket": ds.buckets.get("prod"),
                    "curated_path": rec.dataset_bucket if rec else None,
                    "collection_path": rec.collection_bucket if rec else None,
                })
            return rows
        if table == "releases":
            return [{
                "release": r.version, "cde_version": r.cde_version, "doi": r.doi,
                "created": r.created, "n_datasets": len(r.datasets), "n_changed": len(r.changed),
                "collections": {c: ref.version for c, ref in r.collections.items()},
            } for r in self._releases.values()]
        if table == "collections":
            return [{
                "collection": c.name, "title": c.title, "version": v.version,
                "is_current": v.version == c.version, "doi": v.doi, "concept_doi": c.doi,
                "release": v.release, "cde_version": v.cde_version, "date": v.date,
                "n_datasets": len(v.datasets), "datasets": list(v.datasets),
            } for c in self._collections.values() for v in c.versions.values()]
        if table == "release_datasets":
            return [row for v in self._releases for row in self.release_view(v)]
        raise ValueError("table must be 'datasets', 'releases', 'collections' or 'release_datasets'")

    def to_frame(self, table: str = "datasets"):
        """Same as ``to_records`` but as a pandas DataFrame (requires pandas)."""
        import pandas as pd
        return pd.DataFrame(self.to_records(table))

    # ── Consistency checks ───────────────────────────────────────────────────

    def validate(self) -> List[Issue]:
        """
        Inconsistencies within and between the three source repos.

        Nothing here stops the catalog from loading: each issue says what was found
        and, where the catalog had to choose, what it chose.
        """
        issues = list(self._issues)
        issues += self._check_datasets()
        issues += self._check_collections()
        issues += self._check_releases()
        issues += self._check_local_drift()
        return issues

    def _check_datasets(self) -> List[Issue]:
        out, repo = [], "cloud-datasets"
        for ds in self._datasets.values():
            listed = {v for v, r in self._releases.items() if ds.name in r.changed}
            for v in sorted(set(ds.version_changes) - listed, key=version_key):
                out.append(Issue(repo, ds.name, f"'releases' lists {v} but {v} does not name it in new_datasets"))
            for v in sorted(listed - set(ds.version_changes), key=version_key):
                out.append(Issue(repo, ds.name, f"{v} names it in new_datasets but 'releases' has no {v} entry"))
            first = self.first_release(ds)
            if first is None:
                out.append(Issue(repo, ds.name, "is not included in any release"))
            elif ds.version_changes and first != next(iter(ds.version_changes)):
                out.append(Issue(repo, ds.name,
                    f"first appears in release {first} but its 'releases' history starts at "
                    f"{next(iter(ds.version_changes))}"))
            for v, rec in ds.curation.items():
                if v not in self._releases:
                    out.append(Issue(repo, ds.name, f"curation entry for unknown release {v}"))
                    continue
                pinned = self.collection_version(rec.collection, v)
                if pinned and pinned != rec.collection_version:
                    out.append(Issue(repo, ds.name,
                        f"curation {v} says {rec.collection} {rec.collection_version}; "
                        f"release {v} pins {rec.collection} {pinned}"))
                col = self._collections.get(rec.collection)
                cv = col.versions.get(rec.collection_version) if col else None
                if col is None:
                    out.append(Issue(repo, ds.name, f"curation {v} names unknown collection {rec.collection!r}"))
                elif cv is None:
                    out.append(Issue(repo, ds.name,
                        f"curation {v} names {rec.collection} {rec.collection_version}, "
                        f"which cloud-collections does not list"))
                else:
                    if cv.doi and rec.collection_version_doi and cv.doi != rec.collection_version_doi:
                        out.append(Issue(repo, ds.name,
                            f"curation {v} gives DOI {rec.collection_version_doi} for {rec.collection} "
                            f"{rec.collection_version}; cloud-collections gives {cv.doi}"))
                    if ds.name not in cv.datasets:
                        out.append(Issue(repo, ds.name,
                            f"curated into {rec.collection} {rec.collection_version} in {v}, but that "
                            f"collection version does not list it"))
        return out

    def _check_collections(self) -> List[Issue]:
        out, repo = [], "cloud-collections"
        seen_doi: Dict[str, str] = {}
        for col in self._collections.values():
            members = {d.name for d in self.datasets(collection=col.name)}
            listed = set(col.datasets)
            if listed - members:
                out.append(Issue(repo, col.name,
                    "lists datasets whose own records place them elsewhere: "
                    + ", ".join(f"{n} ({getattr(self._datasets.get(n), 'collection', 'unknown dataset')})"
                                for n in sorted(listed - members))))
            if members - listed:
                out.append(Issue(repo, col.name,
                    "does not list datasets whose own records place them here: "
                    + ", ".join(sorted(members - listed))))
            if col.types and col.name not in col.types:
                out.append(Issue(repo, col.name, f"'types' is {col.types}, which does not include the collection itself"))
            if col.doi and col.doi == col.version_doi:
                out.append(Issue(repo, col.name, f"concept DOI and current version DOI are the same ({col.doi})"))
            if col.version and col.version not in col.versions:
                out.append(Issue(repo, col.name, f"current version {col.version} is missing from 'versions'"))
            for label, doi in [("concept", col.doi)] + [(v.version, v.doi) for v in col.versions.values()]:
                if not doi or (label != "concept" and doi == col.doi):
                    continue
                owner = f"{col.name} {label}"
                if doi in seen_doi and seen_doi[doi].split()[0] != col.name:
                    out.append(Issue(repo, col.name, f"{label} DOI {doi} is also used by {seen_doi[doi]}"))
                seen_doi.setdefault(doi, owner)
            prev = None
            for v in col.versions.values():
                if v.release and v.release not in self._releases:
                    out.append(Issue(repo, col.name, f"{v.version} is tied to unknown release {v.release}"))
                elif v.release:
                    first = next((r.version for r in self._releases.values()
                                  if getattr(r.collections.get(col.name), "version", None) == v.version), None)
                    if first and first != v.release:
                        out.append(Issue(repo, col.name,
                            f"{v.version} is tied to release {v.release}, but cloud-releases first "
                            f"pins it in {first}"))
                    elif first is None:
                        out.append(Issue(repo, col.name,
                            f"{v.version} is tied to release {v.release}, but no release pins that version"))
                if prev and v.date and prev.date and v.date < prev.date:
                    out.append(Issue(repo, col.name,
                        f"{v.version} is dated {v.date}, before {prev.version} ({prev.date})"))
                prev = v
        return out

    def _check_releases(self) -> List[Issue]:
        from datetime import date
        out, repo = [], "cloud-releases"
        seen_doi: Dict[str, str] = {}
        prev: Optional[Release] = None
        for rel in self._releases.values():
            raw = rel.raw
            names = raw.get("datasets_names")
            if isinstance(names, list):
                if len(names) != len(set(names)):
                    dupes = sorted({n for n in names if names.count(n) > 1})
                    out.append(Issue(repo, rel.version, f"datasets_names repeats: {', '.join(dupes)}"))
                if set(names) != set(rel.datasets):
                    out.append(Issue(repo, rel.version, "datasets_names and datasets disagree: "
                        + ", ".join(sorted(set(names) ^ set(rel.datasets)))))
            cnames = raw.get("collection_names")
            if isinstance(cnames, list) and set(cnames) != set(rel.collections):
                out.append(Issue(repo, rel.version,
                    f"collection_names has {sorted(set(cnames) - set(rel.collections))} "
                    f"where collections has {sorted(set(rel.collections) - set(cnames))}"))
            unknown = sorted(set(rel.datasets) - set(self._datasets))
            if unknown:
                out.append(Issue(repo, rel.version, f"includes datasets missing from cloud-datasets: {', '.join(unknown)}"))
            stray = sorted(set(rel.changed) - set(rel.datasets))
            if stray:
                out.append(Issue(repo, rel.version, f"new_datasets names datasets not in the release: {', '.join(stray)}"))
            if prev:
                dropped = sorted(set(prev.datasets) - set(rel.datasets))
                if dropped:
                    out.append(Issue(repo, rel.version, f"drops datasets that were in {prev.version}: {', '.join(dropped)}"))
            for cname, ref in rel.collections.items():
                col = self._collections.get(cname)
                if col is None:
                    out.append(Issue(repo, rel.version, f"pins unknown collection {cname!r}"))
                elif ref.version not in col.versions:
                    out.append(Issue(repo, rel.version, f"pins {cname} {ref.version}, which cloud-collections does not list"))
                before = prev.collections.get(cname) if prev else None
                if before and version_key(ref.version) < version_key(before.version):
                    out.append(Issue(repo, rel.version,
                        f"pins {cname} {ref.version}, older than {before.version} in {prev.version}"))
                if col and col.doi and ref.doi and ref.doi != col.doi:
                    out.append(Issue(repo, rel.version,
                        f"gives DOI {ref.doi} for {cname}; its concept DOI in cloud-collections is {col.doi}"))
            if rel.doi:
                if rel.doi in seen_doi:
                    out.append(Issue(repo, rel.version, f"shares release DOI {rel.doi} with {seen_doi[rel.doi]}"))
                seen_doi.setdefault(rel.doi, rel.version)
            else:
                out.append(Issue(repo, rel.version, "has no release DOI"))
            if not rel.cde_version:
                out.append(Issue(repo, rel.version, "has no CDE version"))
            if rel.created:
                try:
                    date.fromisoformat(rel.created[:10])
                except ValueError:
                    out.append(Issue(repo, rel.version, f"'created' is not a real date: {rel.created}"))
            prev = rel
        return out

    def _check_local_drift(self) -> List[Issue]:
        """With local clones: do the per-item JSON files still match the index files?"""
        out: List[Issue] = []

        def load(path: Path) -> Any:
            try:
                return json.loads(path.read_text(encoding="utf-8"))
            except (OSError, ValueError):
                return None

        def differing(a: dict, b: dict) -> str:
            return ", ".join(sorted(k for k in set(a) | set(b) if a.get(k) != b.get(k)))

        repo = self._local.get("datasets")
        if repo:
            for ds in self._datasets.values():
                item = load(repo / "datasets" / ds.name / "dataset.json")
                if item is None:
                    out.append(Issue("cloud-datasets", ds.name, "has no datasets/<name>/dataset.json"))
                elif item != ds.raw:
                    out.append(Issue("cloud-datasets", ds.name,
                        f"dataset.json differs from datasets.json in: {differing(item, ds.raw)}"))
        repo = self._local.get("releases")
        if repo:
            for rel in self._releases.values():
                item = load(repo / rel.version / "release.json")
                if item is None:
                    out.append(Issue("cloud-releases", rel.version, "has no <version>/release.json"))
                elif item != rel.raw:
                    out.append(Issue("cloud-releases", rel.version,
                        f"release.json differs from releases.json in: {differing(item, rel.raw)}"))
            mirror = load(repo / "releases" / "releases.json")
            if isinstance(mirror, dict) and mirror != {v: r.raw for v, r in self._releases.items()}:
                stale = [v for v in self._releases if mirror.get(v) != self._releases[v].raw]
                out.append(Issue("cloud-releases", "releases/releases.json",
                    f"mirror differs from the root releases.json for: {', '.join(stale)}"))
        repo = self._local.get("collections")
        if repo:
            for col in self._collections.values():
                item = load(repo / col.name / "collection.json")
                if item is None:
                    out.append(Issue("cloud-collections", col.name, "has no <name>/collection.json"))
                elif item != col.raw:
                    out.append(Issue("cloud-collections", col.name,
                        f"collection.json differs from collections.json in: {differing(item, col.raw)}"))
        return out


# ─────────────────────────────────────────────────────────────────────────────
# Command line:  python crn_rosetta.py [summary|validate] [--root DIR | --github [--ref REF]]
# ─────────────────────────────────────────────────────────────────────────────

def _main(argv: Optional[List[str]] = None) -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Inspect the CRN Cloud catalog.")
    parser.add_argument("command", nargs="?", default="summary", choices=["summary", "validate"])
    parser.add_argument("--root", default=None,
                        help="directory holding cloud-datasets, cloud-releases and cloud-collections")
    parser.add_argument("--github", action="store_true", help="read the index files from GitHub instead")
    parser.add_argument("--ref", default="main", help="branch or tag to read with --github")
    args = parser.parse_args(argv)

    if args.github:
        cat = Catalog.from_github(args.ref)
    else:
        here = Path(__file__).resolve().parent
        in_repo = (here.parent / "mkdocs.yml").exists()        # inside asap-crn-learning-lab/scripts
        cat = Catalog.from_local(args.root or (here.parents[1] if in_repo else Path.cwd()))

    if args.command == "validate":
        issues = cat.validate()
        by_repo: Dict[str, List[Issue]] = {}
        for issue in issues:
            by_repo.setdefault(issue.repo, []).append(issue)
        for repo, items in by_repo.items():
            print(f"\n{repo} ({len(items)})")
            for issue in items:
                print(f"  {issue.subject}: {issue.message}")
        print(f"\n{len(issues)} issue(s) in {cat.source}")
        return 0

    print(cat)
    print(f"source: {cat.source}")
    for rel in reversed(cat.releases()):
        counts = {s: 0 for s in STATUSES}
        for name in rel.datasets:
            if name in cat._datasets:
                counts[cat.status(name, rel.version)] += 1
        print(f"  {rel.version:8} CDE {rel.cde_version:5} {len(rel.datasets):3} datasets "
              f"({len(rel.changed)} changed)  " + "  ".join(f"{k} {v}" for k, v in counts.items()))
    return 0


if __name__ == "__main__":
    sys.exit(_main())
