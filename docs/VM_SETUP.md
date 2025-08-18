# Virtual Machine Setup Guide

This guide explains how to set up a virtual machine (VM) with all required software to run the Hangman Project CI/CD pipeline.

---

## 1. Choose a Virtualization Tool
Recommended options:
- **VirtualBox** (free, open source)
- **VMware Workstation Player** (free for personal use)

Download and install one on your host computer.

---

## 2. Create a New VM
- Allocate at least **2 CPUs** and **4GB RAM**.
- Assign at least **20GB disk space**.
- Choose an operating system:
  - Ubuntu Linux (recommended for CI/CD pipelines)

---

## 3. Install the OS
- Download Ubuntu ISO (https://ubuntu.com/download/desktop).
- Attach the ISO to your VM and install Ubuntu inside it.
- Follow installation prompts, create a username/password.

---

## 4. Install Required Software
Once Ubuntu is running, open a terminal and install:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3 python3-pip git
```

Optional but recommended:
```bash
sudo apt install -y curl build-essential
```

---

## 5. Install CI/CD Tools
- **GitHub CLI** (for repo and issues):
  ```bash
  type -p curl >/dev/null || sudo apt install curl -y
  curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
  sudo chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg
  echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
  sudo apt update
  sudo apt install gh -y
  ```

- **Pytest** (for automated testing):
  ```bash
  pip install pytest
  ```

- **Flake8** (for linting):
  ```bash
  pip install flake8
  ```

---

## 6. Clone the Project Repository
```bash
git clone https://github.com/<your-username>/hangman-club-project.git
cd hangman-club-project
```

---

## 7. Verify Installation
Run:
```bash
python3 --version
pip --version
git --version
pytest --version
gh --version
```

All should return version numbers.

---

## 8. Next Steps
- Configure CI/CD in `.github/workflows/`.
- Test the pipeline by committing and pushing code.

---

✅ You are now ready to contribute to the Hangman Project with full CI/CD support!
