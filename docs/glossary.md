# Glossary

Quick reference for terms used across this site. Each entry links to the page where the concept is covered in more detail.

## Commonly Confused Terms

!!! warning "Five different kinds of versioning"
CRN Cloud uses several versioning schemes. These numbers track different things and should not be assumed to match.


| Version type | What it tracks | What changes it | Example |
|---|---|---|---|
| **Dataset Version** | The content of one specific dataset | Metadata updates, new samples, or changes to the underlying data | `v1.1` |
| **Collection Version** | A grouped set of related datasets, such as `pmdbs-sc-rnaseq` | Adding or updating datasets within the collection | `v3.1.0` |
| **CRN Cloud Release** | A platform-wide snapshot of available datasets, collections, documentation, and supported resources | A dated release that bundles specific dataset and collection versions | `v5.0.0` |
| **CDE Schema Version** | The metadata schema and field definitions, also known as the data dictionary | Adding or revising metadata fields or tables to support dataset types | `v4.4` |
| **Pipeline Version** | The processing workflow or software version | Changes to the pipeline code, tools, parameters, or workflow structure | `v4.0.0` |

These five version numbers move independently. For example, a pipeline version and a CRN Cloud release may both use a value like `v4.0.0`, but they do not refer to the same thing. Use the full version type when documenting or discussing data. See the [CRN Cloud Rosetta Stone](rosetta-stone/index.md) for how versions map to each other in practice.

## CRN Cloud & Ecosystem

| Term                       | Definition                                                                                                                                                                                                     |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **ASAP**                   | Aligning Science Across Parkinson's, the organization behind the ASAP CRN ecosystem.                                                                                                                           |
| **CRN**                    | Collaborative Research Network, the ASAP research consortium served by CRN Cloud.                                                                                                                              |
| **CRN Cloud**              | The umbrella name for the ecosystem used to discover, access, govern, and analyze ASAP CRN data. See [What is the CRN Cloud?](getting-started/index.md).                                                       |
| **CRN Cloud Explorer**     | The discovery and browsing tool within CRN Cloud. Use it to search collections, review metadata, and apply for access. It is often called “the Explorer.”                                                      |
| **Data Use Application**   | The per-person application submitted to request access to CRN Cloud data. It is started from the access section of a collection tile. See [Requesting Data Access](getting-started/requesting-data-access.md). |
| **Harmonized Collections** | Collections that standardize data across multiple CRN teams around shared data types or points of commonality, such as the PMDBS collection.                                                                   |
| **Member Collections**     | Collections containing data and background information from an individual CRN team.                                                                                                                            |
| **PMDBS**                  | Postmortem-Derived Brain Sequencing, the human data type behind one of CRN Cloud’s main harmonized collections.                                                                                                |
| **GCP**                    | Google Cloud Platform, the cloud infrastructure that hosts CRN Cloud data and supports backend access control.                                                                                                 |

## Verily Workbench

| Term                                  | Definition                                                                                                                                                                                               |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Verily Workbench**                  | The shared cloud compute environment where approved CRN Cloud data can be analyzed. See the [Verily Workbench Guide](workbench/index.md).                                                                |
| **Reference Workspace**               | A pre-configured, view-only starter workspace connected to CRN Cloud data. Users duplicate it to create their own editable workspace.                                                                    |
| **Personal Workspace**                | Your editable copy of a reference workspace. This is where you launch apps, run notebooks, and perform analyses.                                                                                         |
| **Pod / Billing Pod / Spend Profile** | The billing mechanism attached to a workspace. A billing pod or spend profile is required before running anything that incurs cloud compute costs. See the [Verily Workbench Guide](workbench/index.md). |
| **Resources tab**                     | The Workbench tab where curated data, metadata, documentation, and linked workspace resources can be browsed, previewed, or downloaded. See [Resources](workbench/resources.md).                         |
| **Apps**                              | Cloud compute environments launched inside a workspace, such as JupyterLab, RStudio, or Visual Studio Code. See [Apps](workbench/apps.md).                                                               |
| **Curated data**                      | Processed or organized data derived from raw data, made available for analysis through Workbench resources.                                                                                              |
| **Raw data**                          | Original sequencing or instrument-generated files, such as FASTQs. Stored separately in Requester Pays buckets.                                                                         |

## GitHub & Contribution

| Term                             | Definition                                                                                                                                                   |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Learning Lab**                 | This documentation and tutorials repository: `asap-crn-learning-lab`.                                                                                        |
| **Fork**                         | Your own copy of a repository. Forking is recommended when you plan to modify notebooks, documentation, or code. See [Working with GitHub](github/index.md). |
| **Reuse / Link without forking** | Connecting the upstream repository directly, usually for exploring or running existing content without contributing changes back.                            |
| **Pull Request (PR)**            | A proposed set of changes submitted back to the upstream repository for review. See [Working with GitHub](github/index.md).                                  |

## Pipeline & Bioinformatics

| Term                      | Definition                                                                                                                                                                                   |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **scRNA-seq / snRNA-seq** | Single-cell RNA sequencing and single-nucleus RNA sequencing, the data types processed by the CRN single-cell pipeline.                                                                      |
| **AnnData / H5AD**        | The Python data object and file format used to store expression matrices, cell metadata, gene metadata, embeddings, and analysis results together.                                           |
| **CellRanger**            | A tool used to process raw sequencing reads into gene-by-cell count matrices.                                                                                                                |
| **CellBender**            | A tool used to remove technical background signal, such as ambient RNA contamination, from count matrices.                                                                                   |
| **Doublet score**         | A continuous QC metric, calculated with Scrublet, that estimates the likelihood that a barcode represents more than one cell or nucleus.                                                     |
| **MapMyCells**            | A reference-mapping tool used for first-pass cell type annotation in the pipeline.                                                                                                           |
| **scVI**                  | A probabilistic modeling tool used to generate an integrated latent representation of the data. It is commonly used to reduce batch-associated variation while preserving biological signal. |
| **scANVI**                | A semi-supervised label-transfer method used to extend high-confidence cell type labels to the rest of the dataset.                                                                          |
| **Harmony**               | A batch-correction and integration method that may be included for comparison alongside scVI/scANVI workflows.                                                                               |
| **Leiden clustering**     | A clustering algorithm used to group cells or nuclei based on neighborhood structure. The pipeline may run Leiden clustering at multiple resolutions.                                        |
| **UMAP**                  | A visualization method that projects high-dimensional data into two dimensions. UMAPs are useful visual summaries, but they should not be treated as proof of biological separation.         |
| **scib-metrics**          | A benchmarking toolkit used to evaluate integration performance, including the balance between batch correction and biological conservation.                                                 |

See the [scRNA-seq Pipeline Guide](pipeline/index.md) and [Outputs & File Structure](pipeline/outputs.md) for how these terms fit together.

## Versioning

CRN Cloud uses multiple versioning schemes because different parts of the ecosystem change at different times. Always specify which version type you mean.

### Dataset Version

Tracks the content of one specific dataset.

* A dataset may begin as version `0.1` before release.
* At initial release, it is typically bumped to `v1.0`.
* Metadata-only updates usually receive a minor version bump, such as `v1.1`.
* New samples or changes to the underlying data usually receive a major version bump.

### Collection Version

Tracks a grouped set of related datasets, such as:

* `pmdbs-sc-rnaseq`
* `pmdbs-bulk-rnaseq`
* `mouse-sc-rnaseq`

As datasets are added or updated within a collection, the collection version increments.

Collections may also produce synthetic cohort datasets, created by aggregating datasets in the collection into a single meta-dataset. These cohort datasets are associated with a collection version and have their own DOI.

### CRN Cloud Release

A dated, platform-wide snapshot of CRN Cloud. A CRN Cloud release bundles together specific dataset versions, collection versions, documentation, and supported resources at a point in time.

Example:

```text
v5.0.0
```

### CDE Schema Version

**CDE** stands for Common Data Elements. The CDE Schema defines the standardized metadata fields and tables used to describe CRN Cloud datasets.

A CDE Schema Version changes when metadata fields, tables, or definitions are added or revised. This can happen independently of changes to any individual dataset.

A dataset’s metadata may be reformatted to match a newer schema while preserving provenance.

### Pipeline Version

Tracks the version of the processing pipeline itself.

Pipeline versions change when the workflow code, tools, parameters, or structure changes. Pipeline versions are independent of dataset versions, collection versions, and CRN Cloud release versions.

Example:

```text
v4.0.0
```

### DOI

A **Digital Object Identifier** is a persistent, citable identifier.

In CRN Cloud, DOIs may be associated with datasets, collections, synthetic cohort datasets, and platform releases, depending on the object being cited. When citing data, include the DOI along with the relevant dataset, collection, or release version so others can identify the exact resource used.

### Data Dictionary

The reference document that defines every metadata field and table in the current CDE Schema. The data dictionary helps users understand what each metadata field means and how values should be interpreted.
