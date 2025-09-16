# GitHub + Codecov Coverage Setup

This guide explains how to track code coverage and add a coverage badge for your GitHub repository using Codecov.

---

## 1. Sign Up / Log In to Codecov

1. Go to [https://codecov.io](https://codecov.io).
2. Sign up using your GitHub account.

---

## 2. Add Your Repository to Codecov

1. Click **"Add new repository"**.
2. Select your GitHub repository from the list.
3. Configure repository settings:
   - **Public repository:** No token required.
   - **Private repository:** Copy the repository-specific token provided by Codecov.

---

## 3. Set Up GitHub Actions Workflow

Here is an example Python workflow that runs tests, generates coverage, and uploads to Codecov:

```yaml
name: Python CI

on:
  push:
    branches: [ master ]
  pull_request:
    branches: [ master ]

jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.10, 3.11]

    steps:
    - name: Checkout code
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install pytest pytest-cov flake8 codecov pytest-xdist

    - name: Lint with flake8
      run: flake8 .

    - name: Run tests with pytest and generate coverage
      run: |
        pytest -n auto --cov=. --cov-report=xml --cov-report=term --cov-fail-under=80
      env:
        PYTEST_ADDOPTS: "-p no:warnings"

    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v4
      with:
        files: coverage.xml
        fail_ci_if_error: true
        verbose: true
        flags: unittests
```

### Notes:
- `-n auto` enables parallel test execution.
- `--cov-fail-under=80` fails CI if coverage drops below 80%.
- Codecov automatically posts PR comments with color-coded coverage changes.

---

## 4. Add a Coverage Badge to README

1. Go to your repository on Codecov → **Settings → Badge**.
2. Copy the Markdown snippet, e.g.:

```markdown
[![codecov](https://codecov.io/gh/YOUR_USERNAME/YOUR_REPO/branch/master/graph/badge.svg)](https://codecov.io/gh/YOUR_USERNAME/YOUR_REPO)
```

3. Paste it at the top of your `README.md`:

```markdown
# My Project

[![codecov](https://codecov.io/gh/YOUR_USERNAME/YOUR_REPO/branch/master/graph/badge.svg)](https://codecov.io/gh/YOUR_USERNAME/YOUR_REPO)

Description of your project...
```

4. Commit and push. The badge will update automatically after workflow runs.

---

## 5. Optional Enhancements

- **Dependency caching** to speed up CI:

```yaml
- name: Cache pip
  uses: actions/cache@v3
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
```

- **Test multiple Python versions** using the matrix (already included above).
- **PR coverage comments** are handled automatically by Codecov.

---

By following these steps, you will have:
1. Automated tests with coverage in GitHub Actions.
2. PR comments with color-coded coverage changes.
3. A coverage badge in your README showing real-time coverage status.

