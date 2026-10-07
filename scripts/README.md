# crn_rosetta: look up CRN Cloud datasets, releases and collections from Python

`crn_rosetta.py` answers questions like these:

- Which datasets are in release v5.1.0?
- Which version of a dataset was in an earlier release?
- Where are a dataset's curated files, and which release produced them?
- What changed between two releases?

It reads the same records as the [Rosetta Stone](https://asap-crn.github.io/learning-lab/rosetta-stone/) pages. These come from [cloud-datasets](https://github.com/ASAP-CRN/cloud-datasets), [cloud-releases](https://github.com/ASAP-CRN/cloud-releases) and [cloud-collections](https://github.com/ASAP-CRN/cloud-collections).

## Setup

You need Python 3.9 or newer and no other packages. pandas is optional and only used for tables.

The module is a single file. Copy it next to your notebook or script:

```bash
wget https://raw.githubusercontent.com/ASAP-CRN/asap-crn-learning-lab/dev/scripts/crn_rosetta.py
```

## Load the catalog

```python
from crn_rosetta import Catalog

cat = Catalog.from_github()     # reads the latest records from GitHub
cat
# Catalog(74 datasets, 15 releases, 8 collections, latest='v5.1.0')
```

You can also load from local clones of the three repos instead. Put them all in one folder and pass that folder:

```python
cat = Catalog.from_local("path/to/folder")
# folder/cloud-datasets  folder/cloud-releases  folder/cloud-collections
```

## Common tasks

### Look up a dataset

```python
ds = cat.dataset("hafler-pmdbs-sn-rnaseq-pfc")

ds.title        # 'Single-cell transcriptomic and proteomic analysis of Parkinson's disease brains'
ds.version      # 'v1.1'  (current dataset version)
ds.collection   # 'pmdbs-sc-rnaseq'
ds.doi          # '10.5281/zenodo.15490150'
```

If you misspell a name, the error suggests close matches.

### Find the files

```python
cat.paths("hafler-pmdbs-sn-rnaseq-pfc")
# {'raw':        'gs://asap-raw-team-hafler-pmdbs-sn-rnaseq-pfc',
#  'prod':       'gs://asap-curated-team-hafler-pmdbs-sn-rnaseq-pfc',
#  'curated':    'gs://asap-curated-team-hafler-pmdbs-sn-rnaseq-pfc/pmdbs_sc_rnaseq/release/v3.0.0',
#  'collection': 'gs://asap-crn-pmdbs-sc-rnaseq-collection-v1/hafler-pmdbs-sn-rnaseq-pfc/pmdbs_sc_rnaseq',
#  'curated_release': 'v3.0.0'}
```

The `curated` path in this example ends in `v3.0.0`, even though the latest release is v5.1.0. That is expected: this dataset's curated outputs have not changed since v3.0.0, so later releases still point to the v3.0.0 files.

Pass a release to get the paths as they were at that release:

```python
cat.paths("hafler-pmdbs-sn-rnaseq-pfc", "v2.0.1")["curated"]
# 'gs://asap-curated-team-hafler-pmdbs-sn-rnaseq-pfc/pmdbs_sc_rnaseq/release/v2.0.0'
```

### Filter datasets

```python
cat.datasets(collection="pmdbs-sc-rnaseq", release="v4.0.0")   # members of a collection in a release
cat.datasets(team="sulzer")                                     # by team
cat.datasets(curated=True)                                      # only datasets with curated outputs
cat.datasets(changed_in="v5.1.0")                               # added or updated in a release
cat.datasets(search="striatum")                                 # text search
```

You can combine filters. The result is a list of datasets; use `[d.name for d in ...]` to get just the names.

### Trace a dataset through releases

```python
cat.status("hafler-pmdbs-sn-rnaseq-pfc", "v1.0.0")   # 'added'
cat.status("hafler-pmdbs-sn-rnaseq-pfc")             # 'unchanged'  (no release given = latest)

cat.history("hafler-pmdbs-sn-rnaseq-pfc")            # one row per release the dataset is in
```

### Releases and collections

```python
rel = cat.release("v5.1.0")
rel.cde_version            # 'v4.5'
rel.doi                    # '10.5281/zenodo.20186059'

col = cat.collection("pmdbs-sc-rnaseq")
col.version                # 'v3.1.2'  (current)
list(col.versions)         # ['v1.0.0', 'v2.0.0', 'v3.0.0', 'v3.1.0', 'v3.1.1', 'v3.1.2']

cat.collection_version("pmdbs-sc-rnaseq", "v4.0.0")   # 'v3.1.0'
```

### Compare two releases

```python
cat.diff("v5.0.0", "v5.1.0")
# {'datasets_added':   [... 12 names ...],
#  'datasets_removed': [],
#  'dataset_versions': [('cragg-mouse-sn-rnaseq-striatum', 'v1.0', 'v2.0'), ...],
#  'curation':         [(dataset, curated_release_before, curated_release_after), ...],
#  'collections':      [('mouse-bulk-rnaseq', None, 'v1.0.0'), ('mouse-sc-rnaseq', 'v1.0.1', 'v1.1.0')],
#  'cde_version':      ['v4.4', 'v4.5']}
```

### Get a table (pandas)

```python
df = cat.to_frame("release_datasets")    # one row per dataset per release
df[df.release == "v5.1.0"].status.value_counts()
```

| Table | One row per |
| --- | --- |
| `"datasets"` | dataset, as of the latest release |
| `"releases"` | release |
| `"collections"` | collection version |
| `"release_datasets"` | dataset per release |

Without pandas, `cat.to_records(...)` returns the same rows as a list of dicts.

## What the curation statuses mean

For a given release, each dataset in it has one of these statuses:

| Status | Meaning |
| --- | --- |
| `added` | Curated outputs were produced for the first time in this release. |
| `updated` | Curated outputs were produced again in this release. |
| `unchanged` | Curated outputs exist, but they come from an earlier release. |
| `not-curated` | The dataset has no curated outputs yet. Use its `raw` or `prod` bucket. |

`status()` returns `None` when the dataset is not in that release at all.

Several version numbers move independently: the release (`v5.1.0`), the dataset version (`v1.1`), the collection version (`v3.1.2`) and the CDE version (`v4.5`). Check which one you mean before citing or comparing.

## Command line

```bash
python crn_rosetta.py summary --github      # counts per release
python crn_rosetta.py validate --github     # list problems in the source records
```

Without `--github`, they read local clones of the three repos. Use `--root path/to/folder` to say where those clones are.

## Good to know

- The data comes from the source repos, so it is only as accurate as they are. `cat.validate()` lists known inconsistencies. Where the module had to choose between conflicting records, the issue says which one it used.
- `Catalog.from_github()` reads the `main` branch. Pass `ref="<branch or tag>"` to read a different one.
- Results are plain Python objects, and nothing is cached between sessions. Load the catalog again to pick up new releases.

## For maintainers

- `build_rosetta_stone.py` regenerates the Rosetta Stone pages from this module. Run it with `python scripts/build_rosetta_stone.py`, or add `--github` if you don't have local clones.
- `test_crn_rosetta.py` has the tests. Run them with `python scripts/test_crn_rosetta.py`.
