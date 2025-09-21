# Virtual Machine Setup Guide

This guide explains how to set up a virtual machine (VM) with all required software to run the Hangman Project CI/CD pipeline.

---

## 1. Choose a Virtualization Tool
Recommended options:

- **VMware Workstation Pro** (free for personal use - this will require creation of a Broadcom account- select version 17.6.4 - to be able to click "I agree to the Terms and Conditions and download the software, you will need to click on the Terms and Conditions hyperlink)

Download and install one on your host computer.

---

  ## 2. Create a New VM
- Download Ubuntu ISO (https://ubuntu.com/download/desktop).
1. Open **VMware Workstation / Player**.
2. Click **Create a New Virtual Machine**.
3. Select **Typical (recommended)** and click **Next**.
4. Choose **Installer disc image file (ISO)** and browse to your downloaded Ubuntu ISO.
5. Click **Next**.

---

## 3. Configure the VM

| Setting | Recommended Value |
|---------|-----------------|
| Guest OS | Linux → Ubuntu 64-bit |
| Name | Ubuntu VM (any descriptive name) |
| Memory (RAM) | 2048 MB (2 GB) or more |
| Processors | 2 CPUs |
| Hard Disk | 20 GB or more, pre-allocated or dynamically allocated |
| CD/DVD (SATA) | Attach Ubuntu ISO, check **Connect at power on** |
| Network Adapter | NAT (default) |

---


## 3. Boot from the ISO

1. Start the VM.
2. If it does not boot automatically from the ISO:
   - Press **Esc**, **F2**, or **F12** at VM startup to access the boot menu.
   - Select the **CD/DVD drive** to boot first.

---
## 4. Install Ubuntu

1. When the Ubuntu menu appears, select **"Try Ubuntu"** or **"Install Ubuntu"**.
2. Follow the installer wizard:
   - Select language, keyboard layout, and time zone.
   - Partition your virtual disk (default option is fine).
   - Create a username and password.
3. Complete the installation.

---

## 5. After Installation

1. Remove the ISO from the virtual drive to boot from the virtual disk:
   - VM Settings → CD/DVD (SATA) → Disconnect.
2. Restart the VM; it should now boot directly into Ubuntu.

---

## ✅ Tips to Avoid Kernel/Boot Errors

- Use the **desktop ISO** for VirtualBox/VMware, not the server ISO, unless required.
- Ensure **at least 2 GB RAM**.
- Verify the ISO checksum to ensure it’s not corrupted.
- Enable virtualization extensions in your host BIOS/UEFI if available.

---

## 6. Install Required Software
Once Ubuntu is running, open a terminal by pressing Ctrl + Alt + T and install:

# Ubuntu VM Setup Guide for Hangman Club Project

This guide walks you through setting up a development environment for the Hangman Club Project on an Ubuntu VM.

---

## 1. Open Terminal

Press **Ctrl + Alt + T** to open the terminal.

---

## 2. Update System Packages

```bash
sudo apt update -y && sudo apt upgrade -y

---

3. Install Required System Software

python3, python3-pip, python3-venv → Python and virtual environment support

git → Version control

curl → Needed for downloading GitHub CLI key

build-essential → Development tools (gcc, make, etc.)

```bash
sudo apt install -y python3 python3-pip python3-venv git curl build-essential

---


4. Install GitHub CLI (gh)

```bash
# Ensure curl is installed
type -p curl >/dev/null || sudo apt install -y curl

# Download and register GitHub CLI GPG key
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
sudo chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg

# Add GitHub CLI repository
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null

# Update package lists and install
sudo apt update -y
sudo apt install -y gh

---

5. Set Up Python Development Environment

⚠️ All Python development tools are installed inside the virtual environment, avoiding conflicts with system Python.

```bash
# 0. Install the virtual environment software
sudo apt update
[sudo] password for your-name
   # Enter your ubunto password. When you type the password, nothing will appear on the screen (not even asterisks). This is normal - just type it carefully and press enter.
sudo apt install python3-venv -y
   # Verify the installation
python3 -m venv --help
   # If it prints usage instructions instead of an error, python3-venv is installed correctly

# 1. Create a virtual environment
python3 -m venv devenv

# 2. Activate the virtual environment
source devenv/bin/activate

# 3. Upgrade pip inside the virtual environment
pip install --upgrade pip

# 4. Install Python development tools
pip install pytest pytest-xdist flake8 black isort


# 5. Verify installations
pytest --version
flake8 --version
black --version
isort --version

---
## 6. Update GitHub from your laptop local repo

On your laptop, push your local changes to GitHub:

```bash

cd /path/to/local/repo
git add .
git commit -m "Save Changes"
git push origin master
```
---

## 7. Set up Git in your Ubuntu VM with SSH Keys
   ## 📘 Documentation :

  - [Git Setup in Ubuntu VM with SSH Keys](</docs/git_ssh_vm_setup_guide>)

After this, the VM sees the same files as your laptop
Then you can activate your virtual environment in the VM (source devenv/bin/activate) and work inside it.

---

## 8. Verify Installation
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

Notes

To deactivate the virtual environment when done:
```bash
deactivate```

To reactivate later:
```bash
source devenv/bin/activate```

---

## 9. Next Steps
- Configure CI/CD in `.github/workflows/`.
- Test the pipeline by using the CI_CD_Testing_Hangman_Project.md guide

---

✅ You are now ready to contribute to the Hangman Project with full CI/CD support!

