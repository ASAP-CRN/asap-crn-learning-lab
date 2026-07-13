# Resources

The **Resources** tab in Verily Workbench lets you view, organize, and access data and documentation linked to your workspace. Resources may include curated datasets, metadata files, documentation, notebooks, and links to Google Cloud Storage (GCS) locations (ws_files) that can be used in downstram analysis. 

![Resources Tab Overview](../images/screenshots/Verily-ResourcesTab.png){ width="90%" align="center" .shadow}

## Exploring and Navigating Resources

1. From the top navigation bar, click **Resources**.
2. Click **Browse** to open the folder tree and explore available datasets, curated tables, and metadata files.
3. Select any file to open its **details panel**, where you can view size, modification date, and storage location.

## Previewing and Downloading Files

Once you locate a file of interest, you can view or download it without leaving the Resources tab.

In the **details panel**, choose one of the following actions:

- **Preview** — opens a quick viewer for text, CSV, or JSON files.
- **Download** — click the **⋮ (three dots)** menu next to the file name and select **Download** to save it locally.

!!! tip
    To open the file in **Google Cloud Platform (GCP)**, click **Open in GCP** in the upper-right corner above the details panel. This opens the linked Google Cloud Storage bucket in a new browser tab, where you can view the full directory and metadata.

!!! question "Raw data access"
    Raw data files, such as FASTQs, are stored separately from curated analysis-ready outputs and may live in Requester Pays buckets. Accessing these files requires linking your own Google Cloud Billing Account or billing pod to cover applicable data access and egress costs.

    For step-by-step instructions, see the [Accessing Raw Files in Verily Workbench Guide](https://workbench.verily.com/workspaces/asap-crn-learning-lab-ws-v5/resources/7f596d1b-32fb-4277-8263-cc4c2836c0b7/docs/how-to-access-and-analyze-raw-files-in-verily-workbench.html).
