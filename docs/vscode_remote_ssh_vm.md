# Using VS Code with Remote SSH to Access Your VM

This document explains how to use Visual Studio Code on your laptop to work directly on your Virtual Machine (VM) via SSH, including working with a Python virtual environment (venv) and Git.

---

## 1. Install VS Code and Remote SSH Extension
1. Install **VS Code** on your laptop.
2. Open VS Code → go to Extensions → search for **Remote - SSH** → Install.
3. Optionally, install **Python** and **Git** extensions.

---

## 2. Ensure SSH Access to Your VM
1. Make sure your VM has SSH server running. On Linux:
```bash
sudo systemctl status ssh
```
2. Find your VM’s IP address:
```bash
ip addr show   # Linux
```
3. Test SSH access from your laptop:
```bash
ssh username@VM_IP_address
```

---

## 3. Configure VS Code for Remote SSH
1. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac) → type `Remote-SSH: Connect to Host...` → select **Add New SSH Host**.
2. Enter the SSH command:
```bash
ssh username@VM_IP_address
```
3. Save it to your SSH config file (usually `~/.ssh/config`).

---

## 4. Connect to the VM from VS Code
1. Press `Ctrl+Shift+P` → `Remote-SSH: Connect to Host` → select your VM host.
2. VS Code opens a new window connected to the VM.
3. You can now edit files **directly on the VM**.

---

## 5. Using the VM’s Python venv
1. Open the terminal in VS Code (connected to VM).
2. Activate your virtual environment:
```bash
source venv/bin/activate   # Linux/mac
.\venv\Scripts\Activate.ps1   # Windows PowerShell
```
3. VS Code will detect the Python interpreter in the venv for linting, running scripts, and debugging.

---

## 6. Git Operations
- Git commands in the VS Code terminal or Git UI work **inside the VM**.
- Push and pull work as if you were using the VM terminal.

---

## ✅ Tips
- Always activate the venv before running or debugging code.
- All Git operations happen inside the VM; your laptop repo remains separate.
- You can use VS Code terminal for everything (Git, pip installs, Python scripts).
- This setup keeps your development environment isolated and consistent.

