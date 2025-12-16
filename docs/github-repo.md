# Forking, Reusing, and Contributing to the Learning Lab

This page explains how teams can reuse the ASAP-CRN Learning Lab in their own projects, connect GitHub repositories to Verily Workbench workspaces, and contribute improvements back to the shared resources.

## Step 1: Fork the Repository on Github 
Forking creates your team’s own copy of the repository so you can customize notebooks, docs, and workflows without affecting the upstream Learning Lab.

1. Go to the Learning Lab repo on GitHub: 
    👉 https://github.com/ASAP-CRN/asap-crn-learning-lab 
2. Click **Fork** (top right)
    ![Fork Repo](images/screenshots/Github_Fork.png)
3. Choose your organization or personal account as Owner of the forked repo. 
4. Click **Create fork**

    !!! note For more information on forking a github repository, please see [Github Docs](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo)

✅ Best for: teams making edits, adding notebooks, or maintaining internal variants.

---
## Option B: Reuse without forking (minimal changes)
If you do not need to modify the Learning Lab, you can reuse it by:
- Cloning it locally, or
- Connecting it directly in Verily Workbench and using it as read-only reference

✅ Best for: teams that want the notebooks as a starting point but will keep their work elsewhere.

## 2. Link GitHub Repositories to Verily Workbench Workspaces

Verily Workbench can automatically clone linked GitHub repositories into your cloud apps so you can manage and run source code inside JupyterLab or other environments.

### Add a repository to your workspace
1. Open your workspace in Verily Workbench.
2. Go to the Apps tab.
3. Select + Add Repository.
4. Fill in:
    - Name: a short identifier (for example learning-lab)
    - Repository URL: your fork URL or the upstream repository URL
5. Click Add repository to confirm.

Once added, the repository will be automatically cloned into your app environment when the app starts.

!!! note If your workspace was duplicated from the Learning Lab template, the repo may already be connected. If you do not see it, follow the steps above.

--- 
### Where the repo appears inside your app
After launching **JupyterLab** (or another app), your repositories typically show up under a directory like:
- `/repos/<repo-name>/...`
From there you can open notebooks, edit files, and run code.

!!! Note: If you do not see /repos/, restart your app or confirm the repository is linked in the Apps → Repositories section.