# Connecting GitHub to Verily Workbench

## Why it matters

Verily Workbench is where you run analyses; GitHub is where the CRN's pipeline code, tutorials, and notebooks actually live. Connecting a GitHub repo to a workspace is what bridges the two — it's the link between the CRN Cloud's "Resources & Documentation" pillar and its "Data Utilization: Analysis & Sharing" pillar.

Concretely, once a repo is connected to your workspace, it's **automatically cloned into every app** (JupyterLab, RStudio, etc.) you launch from that workspace. That means:

- No manually downloading or uploading scripts between your laptop and the cloud
- Your notebooks stay in sync with the latest version of the pipeline/tutorial code
- Your analysis, the code that produced it, and its version history all live together — which is what makes the work reproducible and shareable with the rest of the team

## How to connect a repo

1. Open your workspace and go to the **Apps** tab.
2. Click **+ Add Repository** within the Git repositories section.
3. Enter a **Name** for the repo (e.g., `asap-crn-learning-lab`).
4. Enter the **Repository URL** (e.g., `https://github.com/ASAP-CRN/asap-crn-learning-lab`).
5. Click **Add Repository**.

Once added, the repo will be cloned automatically into any app you create in that workspace going forward. 

Repositories are typically available under:
 `$HOME/repos`

For example, the Learning Lab repository may appear at:
`$HOME/repos/asap-crn-learning-lab/`

## Important note about existing apps

Adding a repository to a workspace does not automatically add it to apps that were already created.

If you added the repository after creating your app, either create a new app or clone the repository manually from inside the existing app.

From a terminal inside the app, you can use:
`wb git clone --resource=<YOUR_GITHUB_RESOURCE_NAME>`
or clone directly from GitHub:
`git clone <REPO_URI>`

## Fork it, or link it directly?

- **Link the repo directly** if you just want to run or lightly explore existing notebooks.
- **Fork it first**, then connect your fork's URL, if you plan to modify code or contribute changes back.

For more in-depth information refer to [Working with GitHub](github-repo.md) 