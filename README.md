![https://parkinsonsroadmap.org/](https://parkinsonsroadmap.org/wp-content/uploads/2020/10/cropped-ASAP_Logo_FullColor@2x.png) 

# ASAP CRN Learning Lab

A practical workspace for mastering data exploration, curation, and analysis of **ASAP-CRN** datasets within **Verily Workbench**.

> ** New to this workspace? Start with the setup guide on our GitHub Pages:**  
> 👉 https://asap-crn.github.io/asap-crn-learning-lab/

[![Docs](https://img.shields.io/badge/View_Guide-Live-blue)](https://asap-crn.github.io/asap-crn-learning-lab/)

---

## Overview

This repository provides resources to help researchers explore and analyze **ASAP-CRN** datasets on **Verily Workbench**. The ASAP CRN Learning Lab is organized as a progressive but flexible learning path. You can follow it step-by-step from beginner to advanced topics, or jump directly to the sections that best fit your research needs.

**Current focus:** Python  
**Future expansion:** R implementations

---
## Project Structure

### `tutorials/` — General Skill Building
Technique- and UI-focused walkthroughs that teach fundamental skills, independent of any specific dataset.

Each tutorial includes its own lightweight `environment.yml`.

### `case_studies/` — Biological Analysis Modules
Full biological workflows built around real datasets and scientific objectives.

Each case study provides:
- A more complete `environment.yml`  
- A detailed README  
- Domain-specific notebooks 
--- 

## Repository Structure

```plaintext
asap-crn-learning-lab/
│
├── docs/
│   ├── index.md
│   ├── getting-started.md
│   └── images/
├── tutorials/                 # general skill building
│   ├── 00_pilot_workshop_series
│       ├── 01_getting_started.ipynb
│       ├── 02_data_exploration.ipynb
│       └── 03_downstream_analysis.ipynb
│       └── environment.yml # add
├── case_studies/              # analyses with a biological objective
│   ├── 01_SN-celltyping-analysis.ipynb 
│       ├── environment.yml
│       └── README.md
├── mkdocs.yml
├── .github
│   ├── workflows
│   └── build_docs.yml
├── requirements-docs.txt
├── LICENSE                    # MIT License for code
└── README.md                  # You are here
```
---

## Contributing

We welcome and encourage contributions!  
- Found a typo? Submit a pull request.  
- Have a new dataset or tutorial idea? Open an issue.  
---
This project is licensed under the MIT License. See `LICENSE` for details.
