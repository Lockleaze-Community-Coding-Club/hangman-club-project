# 🤝 Contributing to the Hangman Python Project

Thank you for your interest in contributing! This guide will help you set up your environment, understand the workflow, and submit improvements or new features.

---

## 📁 Project Structure

```
hangman-project/
├── src/                # Source code for the game
├── tests/              # Unit tests
├── assets/             # ASCII art or word files
├── docs/               # Project documentation (optional)
├── README.md
├── CONTRIBUTING.md
└── .gitignore
```

---

## ⚙️ Getting Started

1. **Fork the repository from the Dev branch** on GitHub.
2. **Clone your fork** to your local machine:
   ```bash
   git clone https://github.com/yourusername/hangman-project.git
   cd hangman-project
   ```
3. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```
4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🌳 Git Workflow

We maintain a **Dev branch** as the main integration branch. All contributors should:

1. **Branch from Dev** for your feature or fix:
   ```bash
   git checkout dev
   git pull origin dev
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and **commit clearly**:
   ```bash
   git add .
   git commit -m "Add feature to handle incorrect guesses"
   ```

3. Push your branch:
   ```bash
   git push origin feature/your-feature-name
   ```

4. **Open a Pull Request (PR) against the Dev branch**:
   - Include a clear description of your changes.
   - Link any relevant Issue.
   - Request a reviewer by adding them in the **Reviewers** section on GitHub.
   - For guidance on writing and reviewing PRs, see [How to Conduct a Great Pull Request Review](docs/How_to_conduct_a_Pull_Request_Review.md).

5. **Review process:**
   - The reviewer(s) will comment, suggest changes, and approve once the PR meets quality standards.

6. **Merging Dev into Master:**
   - Only maintainers merge Dev into Master.
   - Dev should be kept up-to-date with approved feature PRs.
   - Merges into Master happen after all tests pass and code is reviewed.
   - Each merge into Master should create a new release or deployment if applicable.

---

## 🧪 Running Tests

We require **100% unit test coverage** for all features.

```bash
python -m unittest discover tests/
```

---

## ✅ Definition of Done

Each contribution must meet the [Definition of Done checklist](issues.md) including:
- 100% test coverage
- Clear, documented code
- Peer review and feedback
- Updated documentation if applicable

---

## 🧠 Need Help?

Feel free to ask questions by raising a GitHub Issue or commenting in our group chat.

Happy coding! 🎉

