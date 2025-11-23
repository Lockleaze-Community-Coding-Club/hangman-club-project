# Full Workflow: Using Laptop, VMWare VM, Git, and Python venv

This workflow covers everything from powering up your laptop to working on your project safely using Git and a virtual environment inside a VMWare VM.

---

## 1. Power Up Your Laptop and VM
1. Turn on your laptop.
2. Launch your VMWare VM.
3. Open a terminal inside the VM (or use VS Code with Remote SSH to the VM).

## 2. Navigate to Your Project Directory
```bash
cd /path/to/hangman-club-project
```

## 3. Activate Your Virtual Environment
- Linux / Mac:
```bash
source venv/bin/activate
```
- Windows (PowerShell):
```powershell
.\venv\Scripts\Activate.ps1
```
- Windows (cmd.exe):
```cmd
.\venv\Scripts\activate.bat
```
- Verify that `(venv)` appears in your terminal prompt.

## 4. Git Workflow
### a. Before starting work
```bash
# Fetch latest updates from remote
git fetch origin

# Check your current branch
git branch

# Switch to the branch you want to work on (e.g., dev)
git checkout dev

# Pull the latest changes from remote
git pull origin dev
```

### b. During work
```bash
# Add changes
git add .

# Commit changes
git commit -m "Describe your changes"
```

### c. After finishing work
```bash
# Push commits to the remote repository
git push origin dev
```

### d. Creating a new branch (optional)
```bash
git checkout -b my-feature-branch
# Work, add, commit, then push
git push -u origin my-feature-branch
```

## 5. Install or Update Dependencies
```bash
pip install -r requirements.txt
```
- Do this **inside the activated venv** to ensure dependencies are isolated.

## 6. Running Your Project
```bash
python main.py
# or run tests
pytest
```
- All packages and Python environment come from the active venv.

## 7. Syncing with Your Laptop
- To see changes pushed from VM on your laptop:
```bash
git fetch origin
git checkout dev
git pull origin dev
```

## 8. Deactivating the Virtual Environment
```bash
deactivate
```
- Returns to the VM’s system Python environment.

## ✅ Tips
- Always activate your venv before running scripts or installing packages.
- Always fetch and pull before starting new work to avoid conflicts.
- Use feature branches for new work and merge back into dev/master as needed.
- Keep backups of remote branches if unsure about overwriting commits.
- Your laptop’s Git repo is separate; push/pull between VM and remote, then pull on laptop to sync.

---

