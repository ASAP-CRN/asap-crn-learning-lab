"""
Tests for crn_rosetta, on a small made-up catalog (no network, no cloud-* clones).

  pytest scripts/test_crn_rosetta.py        or        python scripts/test_crn_rosetta.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from crn_rosetta import Catalog, version_key


def _curation(collection, col_version, release, dataset, workflow=None):
    return {
        "workflow": workflow or collection,
        "collection_version": col_version,
        "workflow_version": "v1.0.0",
        "workflow_url": "github.com/ASAP-CRN/wf/releases#x",
        "cohort_analysis": "v1.0.0",
        "collection_version_doi": f"10.0/{collection}.{col_version}",
        "gcp_uri": {
            "collection_bucket": f"gs://asap-crn-{collection}-collection-v1/{dataset}/wf",
            "dataset_bucket": f"gs://asap-curated-{dataset}/wf/release/{release}",
        },
    }


def _dataset(name, collection, releases, curation):
    return {
        "name": name, "title": name.upper(), "description": "", "doi": f"10.0/{name}",
        "keywords": ["brain", "brain", name.split("-")[0]], "license": "CC-BY-4.0",
        "collection": collection, "version": list(releases.values())[-1],
        "all_versions": sorted(set(releases.values())), "releases": releases, "curation": curation,
        "buckets": {"raw": f"gs://asap-raw-{name}", "prod": f"gs://asap-curated-{name}",
                    "dev": "gs://dev", "uat": "gs://uat"},
    }


def make_catalog():
    datasets = {
        # curated in v1 and again in v3; metadata-only bump in v2
        "a-brain-rna": _dataset("a-brain-rna", "brain-rna",
            {"v1.0.0": "v1.0", "v2.0.0": "v1.1"},
            {"v1.0.0": _curation("brain-rna", "v1.0.0", "v1.0.0", "a-brain-rna"),
             "v2.0.0": {},
             "v3.0.0": _curation("brain-rna", "v2.0.0", "v3.0.0", "a-brain-rna")}),
        # joins in v2, first curated in v3; collection left null, stray key, wrong workflow name
        "b-brain-rna": _dataset("b-brain-rna", None,
            {"v2.0.0": "v1.0"},
            {"v2.0.0": {},
             "v1.0": _curation("brain-rna", "v2.0.0", "v3.0.0", "b-brain-rna", workflow="other-wf")}),
        # never curated
        "c-gut-ms": _dataset("c-gut-ms", None, {"v2.0.0": "v1.0"}, {"v2.0.0": {}}),
    }

    def release(version, cde, names, changed, col_version):
        return {
            "release_version": version, "cde_version": cde, "release_doi": f"10.0/rel.{version}",
            "created": "2026-01-01", "new_datasets": changed, "datasets_names": list(names),
            "datasets": {n: {"dataset_version": v, "doi": f"10.0/{n}"} for n, v in names.items()},
            "collections": {"brain-rna": {"version": col_version, "doi": "10.0/brain-rna"}},
            "collection_names": ["brain-rna"],
        }

    releases = {
        # deliberately out of order: the catalog must sort them itself
        "v3.0.0": release("v3.0.0", "v2.0", {"a-brain-rna": "v1.1", "b-brain-rna": "v1.0", "c-gut-ms": "v1.0"}, [], "v2.0.0"),
        "v1.0.0": release("v1.0.0", "v1.0", {"a-brain-rna": "v1.0"}, ["a-brain-rna"], "v1.0.0"),
        "v2.0.0": release("v2.0.0", "v1.0", {"a-brain-rna": "v1.1", "b-brain-rna": "v1.0", "c-gut-ms": "v1.0"},
                          ["a-brain-rna", "b-brain-rna", "c-gut-ms"], "v1.0.0"),
    }
    collections = {"brain-rna": {
        "name": "brain-rna", "title": "Brain RNA", "collection_doi": "10.0/brain-rna",
        "doi": "10.0/brain-rna.v2.0.0", "version": "v2.0.0", "types": ["brain-rna"], "teams": ["a", "b"],
        "datasets": ["a-brain-rna", "b-brain-rna"], "release": {"version": "v3.0.0", "cde_version": "v2.0"},
        "versions": {
            "v1.0.0": {"doi": "10.0/brain-rna.v1.0.0", "datasets": ["a-brain-rna"],
                       "release": {"version": "v1.0.0", "cde_version": "v1.0"}},
            "v2.0.0": {"doi": "10.0/brain-rna.v2.0.0", "datasets": ["a-brain-rna", "b-brain-rna"],
                       "release": {"version": "v3.0.0", "cde_version": "v2.0"}},
        },
    }}
    return Catalog(datasets, releases, collections, source="test")


def test_versions_sort_numerically():
    assert sorted(["v10.0.0", "v9.1.0", "v9.0.10", "v9.0.2"], key=version_key) == \
        ["v9.0.2", "v9.0.10", "v9.1.0", "v10.0.0"]
    cat = make_catalog()
    assert cat.release_versions == ["v1.0.0", "v2.0.0", "v3.0.0"]
    assert cat.latest_release == "v3.0.0"


def test_status_follows_the_newest_record_at_or_before_the_release():
    cat = make_catalog()
    assert [cat.status("a-brain-rna", r) for r in cat.release_versions] == ["added", "unchanged", "updated"]
    assert [cat.status("b-brain-rna", r) for r in cat.release_versions] == [None, "not-curated", "added"]
    assert [cat.status("c-gut-ms", r) for r in cat.release_versions] == [None, "not-curated", "not-curated"]
    assert cat.status("a-brain-rna") == "updated"                      # default is the latest release


def test_paths_resolve_to_the_release_that_produced_the_outputs():
    cat = make_catalog()
    assert cat.paths("a-brain-rna", "v2.0.0")["curated"].endswith("/release/v1.0.0")
    assert cat.paths("a-brain-rna", "v2.0.0")["curated_release"] == "v1.0.0"
    assert cat.paths("a-brain-rna")["curated"].endswith("/release/v3.0.0")
    assert cat.paths("c-gut-ms") == {"raw": "gs://asap-raw-c-gut-ms", "prod": "gs://asap-curated-c-gut-ms",
                                     "curated": None, "collection": None, "curated_release": None}


def test_malformed_curation_is_repaired_and_reported():
    cat = make_catalog()
    b = cat.dataset("b-brain-rna")
    assert list(b.curation) == ["v3.0.0"]                 # key 'v1.0' re-read from the bucket path
    assert b.collection == "brain-rna"                    # null in the record; taken from the bucket
    assert b.latest_curation.workflow == "other-wf"       # reported, not rewritten
    assert b.latest_curation.workflow_url.startswith("https://")
    messages = [str(i) for i in cat.validate() if i.subject == "b-brain-rna"]
    assert any("not a release version" in m for m in messages)
    assert any("'collection' is null" in m for m in messages)
    assert any("workflow is 'other-wf'" in m for m in messages)


def test_versions_and_changes_per_release():
    cat = make_catalog()
    assert cat.dataset_version("a-brain-rna", "v1.0.0") == "v1.0"
    assert cat.dataset_version("b-brain-rna", "v1.0.0") is None
    assert [cat.change("a-brain-rna", r) for r in cat.release_versions] == ["new", "updated", None]
    assert cat.collection_version("brain-rna", "v2.0.0") == "v1.0.0"
    assert cat.dataset("a-brain-rna").keywords == ["brain", "a"]       # duplicates dropped


def test_filters():
    cat = make_catalog()
    names = lambda **kw: [d.name for d in cat.datasets(**kw)]
    assert names(release="v1.0.0") == ["a-brain-rna"]
    assert names(collection="brain-rna") == ["a-brain-rna", "b-brain-rna"]
    assert names(curated=False) == ["c-gut-ms"]
    assert names(curated=True, release="v2.0.0") == ["a-brain-rna"]
    assert names(changed_in="v3.0.0") == ["a-brain-rna", "b-brain-rna"]   # curated outputs count as a change
    assert names(team="C") == ["c-gut-ms"]
    assert names(search="gut") == ["c-gut-ms"]


def test_rows_and_diff():
    cat = make_catalog()
    rows = {r["dataset"]: r for r in cat.release_view("v2.0.0")}
    assert rows["a-brain-rna"]["collection_version"] == "v1.0.0"
    assert rows["b-brain-rna"]["collection"] is None      # not in the collection until curated
    assert len(cat.to_records("release_datasets")) == 1 + 3 + 3
    assert [r["version"] for r in cat.to_records("collections")] == ["v1.0.0", "v2.0.0"]
    d = cat.diff("v2.0.0", "v3.0.0")
    assert d["datasets_added"] == [] and d["dataset_versions"] == []
    assert d["curation"] == [("a-brain-rna", "v1.0.0", "v3.0.0"), ("b-brain-rna", None, "v3.0.0")]
    assert d["collections"] == [("brain-rna", "v1.0.0", "v2.0.0")]
    assert d["cde_version"] == ["v1.0", "v2.0"]


def test_unknown_names_fail_with_a_hint():
    cat = make_catalog()
    for call, arg in [(cat.dataset, "a-brain-rnaseq"), (cat.release, "v9.9.9"), (cat.collection, "nope")]:
        try:
            call(arg)
        except KeyError as exc:
            assert arg in str(exc)
        else:
            raise AssertionError(f"{arg} should not resolve")
    try:
        cat.dataset("a-brain-rnaseq")
    except KeyError as exc:
        assert "a-brain-rna" in str(exc)


if __name__ == "__main__":
    tests = [f for n, f in sorted(globals().items()) if n.startswith("test_")]
    for t in tests:
        t()
        print("ok ", t.__name__)
    print(f"{len(tests)} passed")
