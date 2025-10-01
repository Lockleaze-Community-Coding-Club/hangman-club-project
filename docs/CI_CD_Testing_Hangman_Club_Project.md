
# Testing the CI/CD Pipeline for Hangman Club Project

This guide explains how to verify that the CI/CD pipeline works on GitHub for the Hangman Club Project.

---

## 1. Ensure Your Environment is Set Up

Make sure you have completed the setup from the previous guide:

- Python virtual environment activated (`source devenv/bin/activate`)  
- `pytest` installed  
- Git and GitHub CLI installed  
- Project repository cloned

---

---
## 2. Start your Virtual Machine

Start your VM and log into Ubunto
Open a terminal in the VM (Ctrl + Alt + T)
---

## 3. Check Out the Correct Branch

```bash
# Navigate to the project repository
cd hangman-club-project

# Make sure you are on the dev branch
git checkout dev

# Pull the latest changes
git pull origin dev
```
---
## 4. Activate the Virtual Environment
```bash
source devenv/bin/activate
```
---
## 5. Install or Update Dependencies
```bash
pip install -r requirements.txt
```
- Do this **inside the activated venv** to ensure dependencies are isolated.

---

## 6. Run Tests Locally

Verify that tests pass locally:

```bash
# Run all pytest tests
pytest -v

```

- `-v` = verbose output  
- This confirms your tests are working locally before triggering the pipeline  

---

## 7. Make a Test Change (Optional)

To test the pipeline, you can make a small change, e.g., update the README file:

```bash
# Edit the README
nano README.md

# Add a test line, save, and exit
```

---

## 6. Stage and Commit the Change

```bash
# Stage all changes
git add .

# Commit with a descriptive message
git commit -m "Test CI/CD pipeline"
```

---

## 7. Push to GitHub

```bash
git push origin dev
```

- Pushing triggers the **GitHub Actions workflow** automatically if it is set up in `.github/workflows/`.

---

## 8. Monitor the Pipeline on GitHub

1. Open your repository on GitHub:  
   `https://github.com/<your-username>/hangman-club-project`

2. Click on the **Actions** tab.

3. Look for the latest workflow run triggered by your push.

4. Verify that:
   - The workflow starts
   - All jobs run successfully
   - `pytest` tests pass
   - Linting (flake8) and formatting (black, isort) jobs succeed

---

## 9. Troubleshoot Pipeline Failures

- Click on a failed job to see **detailed logs**.  
- Common issues:
  - Virtual environment not activated in workflow
  - Missing dependencies in `requirements.txt`
  - Python version mismatch
- Fix issues locally, commit, and push again to retrigger the workflow.

---

## 10. Optional: Trigger Workflow Manually

If needed, you can trigger GitHub Actions manually:

```bash
# Using GitHub CLI
gh workflow list
gh workflow run <workflow_name.yml> -f ref=dev
```

---

## 11. Clean Up After Testing

- Deactivate virtual environment:

```bash
deactivate
```

- Optional: remove test commits if you only wanted to trigger the workflow:

```bash
git reset --hard HEAD~1
git push origin dev --force
```

---

## Notes

- Ensure your repository has `.github/workflows/ci.yml` or similar workflow file configured.  
- Always test in a **feature branch** for real development, then merge into main once verified.  
- Keep virtual environment isolated for reliable local testing.
