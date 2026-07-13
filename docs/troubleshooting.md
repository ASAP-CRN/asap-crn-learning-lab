# Troubleshooting Guide

This guide covers common issues encountered when using the ASAP CRN Learning Lab and Verily Workbench, along with recommended steps to resolve them. Start with the section that best matches the issue you’re seeing.

---
# Verily Workbench
## 1. App Fails to Launch on First Attempt

**Symptom**  
When clicking your App name or the “Launch” icon, the new tab/window opens but remains blank or shows an error.

**Why this happens**
This can occur during initial app startup while the environment is still provisioning.

**What to Try**

1. Close the blank/error window.  
2. Relaunch the App from the Verily Workbench interface.

**If the issue persists**

- Wait 1–2 minutes and try launching again.
- Refresh the Workbench page before retrying.
- If the problem continues after multiple attempts, consider restarting the app or workspace.
---

## 2. App Is Slow, Unresponsive, or Throwing Repeated Errors (JupyterLab)

**Symptom**  
JupyterLab becomes sluggish, repeatedly shows errors, or stops responding.

**Why this happens**
This can occur due to resource constraints, long-running processes, or accumulated kernel state during extended sessions.

**What to Try**

1. Restart the kernel from within JupyterLab (“Kernel” → “Restart Kernel”).  
2. Reload the browser tab.  
3. Save your work and restart the App from the Verily Workbench **Workspace** page.  

**If the issue persists**

   - Shut down the current App instance.  
   - Start a new App session from the Workspace page.
---

If your issue is not listed here, feel free to open an issue on GitHub or contact the CRN Cloud team for support at <cloud@parkinsonsroadmap.org>.
