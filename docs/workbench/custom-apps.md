# Custom Apps

The [Apps](apps.md) page covers the built-in environments Verily Workbench provides out of the box — JupyterLab, RStudio, and VS Code. **Custom apps** let you go further: you define your own environment with a [Dev Container](https://containers.dev/) configuration, so you control the base image, installed tools, startup behavior, and development workflow.

The CRN maintains a set of starter templates you can fork and adapt:

🔗 **[ASAP CRN Workbench App Templates](https://github.com/ASAP-CRN/workbench-app-templates)**

!!! info "Built on Verily's examples"
    The CRN custom app templates are built off of Verily's own Workbench app examples. If you need a starting point beyond the CRN templates, more app examples are available in Verily's repository: [verily-src/workbench-app-devcontainers](https://github.com/verily-src/workbench-app-devcontainers).

!!! note "Prerequisites"
    Building and testing a custom app locally requires [Docker](https://www.docker.com/) and the [Dev Containers CLI](https://github.com/devcontainers/cli) on your own machine. To run the finished app in Workbench you'll also need a workspace and a billing pod — see the [Verily Workbench Guide](index.md).

## Do you need a custom app?

Reach for a built-in app first. Custom apps are aimed at more advanced users who need control over the environment itself — installing larger system-level tools, working from the command line, or tailoring the image beyond what the standard environments allow. Consider a custom app when:

| Use a **built-in app** when... | Use a **custom app** when... |
|---|---|
| You want JupyterLab, RStudio, or VS Code with common packages | You need larger system-level tools, CLIs, or bioinformatics dependencies baked into the image |
| You're running the Learning Lab notebooks or tutorials | You need to control the base OS image or startup behavior |
| You want the fastest path to analysis | You're a command-line-oriented developer who wants a terminal- or IDE-style environment tailored to your workflow |
| A standard environment already covers your needs | You're building a reproducible environment to share across a team or pipeline |

!!! warning "Custom apps can be slow to start"
    Custom apps build their environment on launch, so the first startup can take **10–30 minutes** depending on the image and dependencies. This is expected — plan for it, and avoid deleting the app between short work sessions if you'll need it again soon.

## Available templates

Each template lives in its own folder in the [templates repository](https://github.com/ASAP-CRN/workbench-app-templates). Start from the app-specific `README.md` in that folder for the authoritative setup, customization, and launch instructions.

### Ubuntu (terminal)

A minimal Ubuntu-based app that runs a browser-accessible terminal using `ttyd`. Best for command-line workflows, testing custom package installation, and building a lightweight base for pipeline or analysis development.

### VS Code (IDE)

A browser-accessible VS Code–style environment built with `code-server`. Best for editing notebooks, scripts, and pipeline code in a full IDE. It includes support for a custom Python virtual environment, project-specific packages from `requirements.txt`, and AI-assisted development tools (Gemini Code Assist and Claude Code / Claude API workflows).

!!! tip "Which one?"
    Pick **Ubuntu** for a lightweight command-line environment, or **VS Code** if you want a full editor with extensions and AI-assisted development. The two templates are independent — changes to one don't affect the other.

## The workflow at a glance

The templates are designed to be forked, customized, tested locally, and then registered as a custom app in Workbench.

1. **Fork** the [templates repository](https://github.com/ASAP-CRN/workbench-app-templates) to your own GitHub account.
2. **Pick a template** folder (`ubuntu/` or `vscode/`).
3. **Customize** the files for your environment — most commonly `requirements.txt` (Python packages), the `Dockerfile` (system tools and dependencies), and `.devcontainer.json` (startup and app behavior).
4. **Test locally** with the Dev Containers CLI before launching in the cloud:
    ```bash
    docker network create app-network   # okay if it already exists
    devcontainer up --workspace-folder .
    ```
    Check the template's `README.md` for the correct port and local URL.
5. **Push** your changes to your fork.
6. **Create a custom app** in Verily Workbench that points to your forked repository and the selected template folder.

!!! warning "Test before you launch"
    Building images and resolving dependencies is much faster to debug locally than in Workbench. Confirm the app runs with `devcontainer up` before registering it as a Workbench custom app.

For the full, up-to-date instructions — including the complete list of customizable files and the Workbench registration steps — see the [templates repository README](https://github.com/ASAP-CRN/workbench-app-templates#readme).

## What's next

| If you're trying to... | Go to |
|---|---|
| Connect your forked template repo to a workspace | [GitHub Connection](github.md) |
| Load data into your workspace | [Resources](resources.md) |
| Launch a built-in app instead | [Apps](apps.md) |