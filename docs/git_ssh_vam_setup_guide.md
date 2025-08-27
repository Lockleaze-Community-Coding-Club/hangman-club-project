# SSH Connection Setup from VM to GitHub

This guide explains the steps to securely connect your Ubuntu VM to GitHub using SSH, including the first-time authentication prompt, along with a visual checklist.

---

## Steps to Connect

### 1. Generate an SSH Key (if not already done)
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```
- Press Enter to accept default location.
- Optionally set a passphrase.

### 2. Add the Public Key to GitHub
```bash
cat ~/.ssh/id_ed25519.pub
```
- Copy the output.
- Go to GitHub: **Settings → SSH and GPG keys → New SSH key**.
- Paste the key and save.

### 3. Test SSH Connection
```bash
ssh -T git@github.com
```
- First time you see:
```
The authenticity of host 'github.com (IP)' can't be established.
ED25519 key fingerprint is SHA256:<fingerprint>.
Are you sure you want to continue connecting (yes/no/[fingerprint])?
```
- **Type `yes`** and press Enter.
- Git adds GitHub’s key to `~/.ssh/known_hosts`.

### 4. Confirmation
You should see:
```
Hi <username>! You've successfully authenticated, but GitHub does not provide shell access.
```
- Now your VM is authenticated with GitHub.
- You can clone/push repositories using SSH without a password.

### 5. Clone Repository via SSH
```bash
git clone git@github.com:<your-username>/<repo-name>.git
```

### 6. Optional: Configure Git user
```bash
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
```

---

## Visual Checklist

```text
Step 1: Generate SSH Key on VM
    │
    ▼
Step 2: Copy Public Key and Add to GitHub
    │
    ▼
Step 3: Test SSH Connection
    │
    ▼
Step 4: First-time prompt
    └─> Type 'yes' to add GitHub to known_hosts
    │
    ▼
Step 5: Confirmation message
    │
    ▼
Step 6: Clone repositories and work in VM
```

---

This ensures a secure SSH connection between your VM and GitHub, enabling seamless git operations without needing a password every time.

