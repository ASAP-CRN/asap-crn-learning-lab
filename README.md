![https://parkinsonsroadmap.org/](https://parkinsonsroadmap.org/wp-content/uploads/2020/10/cropped-ASAP_Logo_FullColor@2x.png) 

# ASAP CRN Learning Lab

Reproducible analysis examples for leveraging ASAP-CRN data to spark new discoveries in Parkinson’s disease.

> **New to the ASAP-CRN Cloud and Learning Lab? Start with the setup guide on our GitHub Pages:**  
> 👉 https://asap-crn.github.io/asap-crn-learning-lab/

[![Docs](https://img.shields.io/badge/View_Guide-Live-blue)](https://asap-crn.github.io/asap-crn-learning-lab/)

---

## Overview

The ASAP-CRN Learning Lab is an ASAP-CRN–maintained resource that enables researchers to leverage CRN Cloud data through reproducible exploratory and meta-analysis examples. Users may engage via workshops, follow a guided learning path, or start directly with the modules and models most relevant to their research.

---

## Data Access Prerequisite

All datasets used in this Learning Lab are accessed through the **[ASAP CRN Cloud](https://cloud.parkinsonsroadmap.org/collections)**, which serves as the authoritative platform for data discovery, access control, and governance across the Collaborative Research Network.

Before running any tutorials or case studies, users must request and receive approval for the relevant **ASAP-CRN data collections** via the CRN Cloud portal. Once approved, datasets can be accessed within supported analysis environments, including Verily Workbench.

For detailed instructions, see the ASAP CRN Cloud User Guide:
👉 https://asap-crn.github.io/asap-crn-learning-lab/

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
│       └── environment.yml
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

We welcome and encourage contributions from the ASAP-CRN community and the broader research ecosystem.

- Found a typo? Submit a pull request.  
- Have a new dataset or tutorial idea? Open an issue.  
---
This project is licensed under the MIT License. See `LICENSE` for details.
