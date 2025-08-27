# Development Environment and GitHub Actions Guide

This guide explains how your local development environment and GitHub Actions fit together, along with a visual diagram.

---

## Description

### 1. Local Virtual Environment
- The virtual environment (`devenv`) is **local** to your Ubuntu VM.
- It ensures Python packages you install for development **don’t conflict with system Python**.
- Used to write code, run tests, and check formatting with tools like `pytest`, `flake8`, `black`, and `isort`.

### 2. Git and Project Repository
- `git` tracks code changes and allows pushing code to GitHub.
- Your repository (e.g., `hangman-club-project`) lives on GitHub.

### 3. GitHub Actions
- Cloud-based automation for your repository.
- Runs scripts on events like pushing code or opening pull requests.
- Typical uses:
  - Run tests automatically with `pytest`.
  - Check code style with `flake8`, `black`, and `isort`.
  - Deploy code if checks pass.

### 4. Workflow Connection
1. Write code locally in VM inside virtual environment.
2. Push changes to GitHub using `git`.
3. GitHub Actions detects the push and runs workflow in cloud.
   - Sets up temporary Python environment.
   - Installs dependencies.
   - Runs tests and code checks.

**Summary:**
- **VM + virtual environment**: local workspace.
- **GitHub Actions**: automated cloud checks on code pushed to GitHub.

### 5. Syncing Code Between Laptop and VM
- The virtual environment only has access to files **inside the VM**.
- Best practice is to use **GitHub as the central point of synchronization** between laptop and VM:

1. **Laptop Repository**
   - Commit and push changes to GitHub from your laptop.
   - Useful for offline or local edits.

2. **VM Repository**
   - Clone or pull from GitHub to have the latest code inside the VM.
   - Work inside the virtual environment (`devenv`) to run tests and development tools.

3. **GitHub Actions**
   - Automatically runs tests and checks on commits pushed from either laptop or VM.

> ⚠️ Avoid trying to directly sync the laptop folder into the VM without Git — this can cause history conflicts.

**Bottom line:**
- Keep a Git repository on both laptop and VM.
- Use GitHub as the single source of truth.
- Use the VM repository for development in the virtual environment.

---

## Diagram

```text
          +-----------------------+
          |       Laptop          |
          |                       |
          |  Local Git Repository | <--- Push/Pull ---> GitHub Repository
          +-----------------------+
                     ^
                     | Commit & Push
                     v
          +-----------------------+
          |   Local Ubuntu VM     |
          |                       |
          |  +----------------+   |
          |  | Virtual Env    |   |
          |  | (devenv)       |   |
          |  +----------------+   |
          |  Git Repository inside VM
          +-----------------------+
                     |
                     v Push code
          +-----------------------+
          | GitHub Actions (CI/CD)|
          |                       |
          | - Set up Python env   |
          | - Install dependencies|
          | - Run tests & checks  |
          +-----------------------+
```

