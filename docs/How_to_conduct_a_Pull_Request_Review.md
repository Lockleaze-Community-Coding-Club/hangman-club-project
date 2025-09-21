# How to Conduct a Great Pull Request Review

This guide walks you step by step on conducting an effective, constructive Pull Request (PR) review using a real PR example: [hangman-club-project PR #17](https://github.com/Lockleaze-Community-Coding-Club/hangman-club-project/pull/17/files).

---

## Step-by-Step Checklist (Overview)
1. **Understand the PR** – read the description, summary, and changed files.
2. **Run the code locally** – check for syntax errors, failing tests, or lint issues.
3. **Review code file by file** – focus on functionality, readability, style, and consistency.
4. **Check imports, dependencies, and project structure**.
5. **Look for blockers** – broken tests, syntax errors, or files that shouldn’t be committed.
6. **Add suggestions for improvements** – small fixes or stylistic improvements.
7. **Provide examples and code snippets** – help the contributor implement your suggestions.
8. **Encourage and explain reasoning** – balance critique with constructive feedback.
9. **Wrap up the review** – summarize key points, next steps, and optional suggestions.

---

## Step 1: Understand the PR
- **Read the description and summary:** Identify what the PR is trying to achieve.
- **Example:** PR #17 adds a top-level runner, a `select_word()` function, tests, and updates documentation.
- **Action:** Note any new features, fixes, or files added.

---

## Step 2: Run the code locally
- **Set up environment:**
```bash
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```
- **Run tests and linting:**
```bash
pytest -q
flake8
```
- **Example from PR #17:** Running pytest revealed that `select_word()` does not return the tuple expected by the tests.

---

## Step 3: Review code file by file
- **Focus areas:** functionality, readability, consistency, PEP8 compliance.
- **Example:**
  - `code/select_word.py` should return `(word, masked)` instead of a single placeholder string.
  - `code/lockleaze_hangman.py` has unindented print statements that will raise `SyntaxError`.

---

## Step 4: Check imports, dependencies, and project structure
- **Ensure imports are correct:** tests should be able to import the module.
- **Example:** `tests/test_select_word.py` imports `from select_word import select_word`, but the module is in `code/`.
- **Fix options:** update import path to `from code.select_word import select_word` or move the module.

---

## Step 5: Look for blockers
- **Identify issues that prevent merging:**
  - Failing tests
  - Syntax or indentation errors
  - Committed binaries or compiled files
- **Example:** `.pyc` files in PR #17 need to be removed and added to `.gitignore`.

---

## Step 6: Add suggestions for improvements
- **Use GitHub comment boxes:** for general suggestions.
- **Use "Add a suggestion" feature:** for actionable one-click fixes.
- **Example:**
```suggestion
# code/select_word.py
import random
from typing import Tuple

_WORDS = ['apple', 'pear', 'banana', 'gainsborough square']

def select_word() -> Tuple[str, str]:
    word = random.choice(_WORDS)
    masked = ''.join('_' if ch != ' ' else ' ' for ch in word)
    return word, masked
```

---

## Step 7: Provide examples and code snippets
- **Why:** Helps the contributor apply your suggestions correctly.
- **Example:** showing the correct indentation and `main()` wrapper in `lockleaze_hangman.py`.

```python
# code/lockleaze_hangman.py
from select_word import select_word

def main():
    word_selected, masked = select_word()
    winner = True

    if winner:
        print("You are correct — today's word was:", word_selected)
    else:
        print("Loser")

if __name__ == '__main__':
    main()
```

---

## Step 8: Encourage and explain reasoning
- **Balance critique with positive feedback:**
  - "Thanks for adding tests — this helps catch errors early."
  - Explain why a change is needed: "select_word() must return a tuple to pass the tests."

---

## Step 9: Wrap up the review
- **Summarize key points:** blockers, minor suggestions, and optional improvements.
- **Provide next steps checklist:**
  - Update `select_word()` to return `(word, masked)`.
  - Fix import paths in tests.
  - Correct indentation in `lockleaze_hangman.py`.
  - Remove `.pyc` files and update `.gitignore`.
  - Remove hidden Unicode characters.
  - Run `pytest` and `flake8` locally before pushing updates.

- **End positively:** encourage further questions or discussion.

---

Following this structure ensures your PR reviews are **clear, actionable, and supportive**, helping maintainers and contributors improve code quality efficiently.

