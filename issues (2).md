# 📝 Hangman Project Issues and Task Breakdown

Use this list to raise and track GitHub Issues. Each issue should meet the Definition of Done below.

## 🗂️ Project Setup

### 🔧 Create a Git repository and add a README
**Definition of Done:**
- [ ] Code is written in a clear, readable, and consistent style
- [ ] Follows Python conventions (PEP8 or as agreed by the group)
- [ ] Includes meaningful comments or docstrings where appropriate
- [ ] Feature or fix fulfills the ticket's description and acceptance criteria
- [ ] Has been tested manually and/or with automated tests (if relevant)
- [ ] 100% unit test coverage added or updated
- [ ] Handles common edge cases and invalid inputs gracefully
- [ ] Changes are committed with a clear, descriptive message
- [ ] Code is pushed to a dedicated feature branch
- [ ] A pull request (PR) is created for review before merging into main
- [ ] PR includes a short summary of the change and screenshots (if applicable)
- [ ] README or inline docs updated if the change affects how to use or run the program
- [ ] New functions or modules include docstrings (at least 1–2 lines explaining what it does)
- [ ] At least one other person has reviewed and approved the pull request
- [ ] All review comments have been addressed or discussed
- [ ] The branch has been tested after merging to ensure no breakages

---

### 🔧 Add `.gitignore` file for Python
**Definition of Done:**
- [ ] Code is written in a clear, readable, and consistent style
- [ ] Follows Python conventions (PEP8 or as agreed by the group)
- [ ] Includes meaningful comments or docstrings where appropriate
- [ ] Feature or fix fulfills the ticket's description and acceptance criteria
- [ ] Has been tested manually and/or with automated tests (if relevant)
- [ ] 100% unit test coverage added or updated
- [ ] Handles common edge cases and invalid inputs gracefully
- [ ] Changes are committed with a clear, descriptive message
- [ ] Code is pushed to a dedicated feature branch
- [ ] A pull request (PR) is created for review before merging into main
- [ ] PR includes a short summary of the change and screenshots (if applicable)
- [ ] README or inline docs updated if the change affects how to use or run the program
- [ ] New functions or modules include docstrings (at least 1–2 lines explaining what it does)
- [ ] At least one other person has reviewed and approved the pull request
- [ ] All review comments have been addressed or discussed
- [ ] The branch has been tested after merging to ensure no breakages

---

### 🔧 Create folder structure (e.g., `/src`, `/tests`, etc.)
**Definition of Done:**
- [ ] Code is written in a clear, readable, and consistent style
- [ ] Follows Python conventions (PEP8 or as agreed by the group)
- [ ] Includes meaningful comments or docstrings where appropriate
- [ ] Feature or fix fulfills the ticket's description and acceptance criteria
- [ ] Has been tested manually and/or with automated tests (if relevant)
- [ ] 100% unit test coverage added or updated
- [ ] Handles common edge cases and invalid inputs gracefully
- [ ] Changes are committed with a clear, descriptive message
- [ ] Code is pushed to a dedicated feature branch
- [ ] A pull request (PR) is created for review before merging into main
- [ ] PR includes a short summary of the change and screenshots (if applicable)
- [ ] README or inline docs updated if the change affects how to use or run the program
- [ ] New functions or modules include docstrings (at least 1–2 lines explaining what it does)
- [ ] At least one other person has reviewed and approved the pull request
- [ ] All review comments have been addressed or discussed
- [ ] The branch has been tested after merging to ensure no breakages

---
## 🧠 Core Game Logic

### 🔧 Write a main function which calls the other functions in the correct order to play the game 
-- Use placeholder (empty) functions to build this based on the inputs and outputs of each module

**Definition of Done:**
- [ ] Code is written in a clear, readable, and consistent style
- [ ] Follows Python conventions (PEP8 or as agreed by the group)
- [ ] Includes meaningful comments or docstrings where appropriate
- [ ] Feature or fix fulfills the ticket's description and acceptance criteria
- [ ] Has been tested manually and/or with automated tests (if relevant)
- [ ] 100% unit test coverage added or updated
- [ ] Handles common edge cases and invalid inputs gracefully
- [ ] Changes are committed with a clear, descriptive message
- [ ] Code is pushed to a dedicated feature branch
- [ ] A pull request (PR) is created for review before merging into main
- [ ] PR includes a short summary of the change and screenshots (if applicable)
- [ ] README or inline docs updated if the change affects how to use or run the program
- [ ] New functions or modules include docstrings (at least 1–2 lines explaining what it does)
- [ ] At least one other person has reviewed and approved the pull request
- [ ] All review comments have been addressed or discussed
- [ ] The branch has been tested after merging to ensure no breakages


### 🔧 Implement word selection from a list

-- select_word.py (file already created but incomplete. to do)
-- Create function or functions that 
-- contains a [list] of words or phrases that are part of the game # this can be automated later the list will become a parameter (input)
-- selects a word from the list (randomly) 
-- returns two lists of characters
1 - the chosen word as a list (ready for input to input validation for guesses)
2 - a masked version of the chosen word withthe correct number of letters replaced by '_' except for ' ' 

eg ['apple','pear','bannana', 'gainsborough square']

if the second element in the list is chosen the return 
['pear', '____']
if the fourth is chosen
return 
['gainsborough square'],['____________ ______']



**Definition of Done:**
- [ ] Code is written in a clear, readable, and consistent style
- [ ] Follows Python conventions (PEP8 or as agreed by the group)
- [ ] Includes meaningful comments or docstrings where appropriate
- [ ] Feature or fix fulfills the ticket's description and acceptance criteria
- [ ] Has been tested manually and/or with automated tests (if relevant)
- [ ] 100% unit test coverage added or updated
- [ ] Handles common edge cases and invalid inputs gracefully
- [ ] Changes are committed with a clear, descriptive message
- [ ] Code is pushed to a dedicated feature branch
- [ ] A pull request (PR) is created for review before merging into main
- [ ] PR includes a short summary of the change and screenshots (if applicable)
- [ ] README or inline docs updated if the change affects how to use or run the program
- [ ] New functions or modules include docstrings (at least 1–2 lines explaining what it does)
- [ ] At least one other person has reviewed and approved the pull request
- [ ] All review comments have been addressed or discussed
- [ ] The branch has been tested after merging to ensure no breakages

---

### 🔧 Implement function to display current game state
**Definition of Done:**
- [ ] Code is written in a clear, readable, and consistent style
- [ ] Follows Python conventions (PEP8 or as agreed by the group)
- [ ] Includes meaningful comments or docstrings where appropriate
- [ ] Feature or fix fulfills the ticket's description and acceptance criteria
- [ ] Has been tested manually and/or with automated tests (if relevant)
- [ ] 100% unit test coverage added or updated
- [ ] Handles common edge cases and invalid inputs gracefully
- [ ] Changes are committed with a clear, descriptive message
- [ ] Code is pushed to a dedicated feature branch
- [ ] A pull request (PR) is created for review before merging into main
- [ ] PR includes a short summary of the change and screenshots (if applicable)
- [ ] README or inline docs updated if the change affects how to use or run the program
- [ ] New functions or modules include docstrings (at least 1–2 lines explaining what it does)
- [ ] At least one other person has reviewed and approved the pull request
- [ ] All review comments have been addressed or discussed
- [ ] The branch has been tested after merging to ensure no breakages

---

### 🔧 Implement input validation for guesses
Create a function with two inputs
- An ordered [list] of characters that are the current word being guessed
- A single letter, the current guess
one output:
- a list of positions in the current word that contain the current guess

eg 
word: 'apple'
guess: 'p'
output [1,2] # note a is 0 in python



**Definition of Done:**
- [ ] Code is written in a clear, readable, and consistent style
- [ ] Follows Python conventions (PEP8 or as agreed by the group)
- [ ] Includes meaningful comments or docstrings where appropriate
- [ ] Feature or fix fulfills the ticket's description and acceptance criteria
- [ ] Has been tested manually and/or with automated tests (if relevant)
- [ ] 100% unit test coverage added or updated
- [ ] Handles common edge cases and invalid inputs gracefully
- [ ] Changes are committed with a clear, descriptive message
- [ ] Code is pushed to a dedicated feature branch
- [ ] A pull request (PR) is created for review before merging into main
- [ ] PR includes a short summary of the change and screenshots (if applicable)
- [ ] README or inline docs updated if the change affects how to use or run the program
- [ ] New functions or modules include docstrings (at least 1–2 lines explaining what it does)
- [ ] At least one other person has reviewed and approved the pull request
- [ ] All review comments have been addressed or discussed
- [ ] The branch has been tested after merging to ensure no breakages

---

### 🔧 Add function to track incorrect guesses and update lives
**Definition of Done:**
- [ ] Code is written in a clear, readable, and consistent style
- [ ] Follows Python conventions (PEP8 or as agreed by the group)
- [ ] Includes meaningful comments or docstrings where appropriate
- [ ] Feature or fix fulfills the ticket's description and acceptance criteria
- [ ] Has been tested manually and/or with automated tests (if relevant)
- [ ] 100% unit test coverage added or updated
- [ ] Handles common edge cases and invalid inputs gracefully
- [ ] Changes are committed with a clear, descriptive message
- [ ] Code is pushed to a dedicated feature branch
- [ ] A pull request (PR) is created for review before merging into main
- [ ] PR includes a short summary of the change and screenshots (if applicable)
- [ ] README or inline docs updated if the change affects how to use or run the program
- [ ] New functions or modules include docstrings (at least 1–2 lines explaining what it does)
- [ ] At least one other person has reviewed and approved the pull request
- [ ] All review comments have been addressed or discussed
- [ ] The branch has been tested after merging to ensure no breakages

---

### 🔧 Detect game win/loss and show message
**Definition of Done:**
- [ ] Code is written in a clear, readable, and consistent style
- [ ] Follows Python conventions (PEP8 or as agreed by the group)
- [ ] Includes meaningful comments or docstrings where appropriate
- [ ] Feature or fix fulfills the ticket's description and acceptance criteria
- [ ] Has been tested manually and/or with automated tests (if relevant)
- [ ] 100% unit test coverage added or updated
- [ ] Handles common edge cases and invalid inputs gracefully
- [ ] Changes are committed with a clear, descriptive message
- [ ] Code is pushed to a dedicated feature branch
- [ ] A pull request (PR) is created for review before merging into main
- [ ] PR includes a short summary of the change and screenshots (if applicable)
- [ ] README or inline docs updated if the change affects how to use or run the program
- [ ] New functions or modules include docstrings (at least 1–2 lines explaining what it does)
- [ ] At least one other person has reviewed and approved the pull request
- [ ] All review comments have been addressed or discussed
- [ ] The branch has been tested after merging to ensure no breakages

---
## 🎮 User Interaction & Interface

### 🔧 Add ASCII art for hangman
**Definition of Done:**
- [ ] Code is written in a clear, readable, and consistent style
- [ ] Follows Python conventions (PEP8 or as agreed by the group)
- [ ] Includes meaningful comments or docstrings where appropriate
- [ ] Feature or fix fulfills the ticket's description and acceptance criteria
- [ ] Has been tested manually and/or with automated tests (if relevant)
- [ ] 100% unit test coverage added or updated
- [ ] Handles common edge cases and invalid inputs gracefully
- [ ] Changes are committed with a clear, descriptive message
- [ ] Code is pushed to a dedicated feature branch
- [ ] A pull request (PR) is created for review before merging into main
- [ ] PR includes a short summary of the change and screenshots (if applicable)
- [ ] README or inline docs updated if the change affects how to use or run the program
- [ ] New functions or modules include docstrings (at least 1–2 lines explaining what it does)
- [ ] At least one other person has reviewed and approved the pull request
- [ ] All review comments have been addressed or discussed
- [ ] The branch has been tested after merging to ensure no breakages

---

### 🔧 Make a simple command-line interface
**Definition of Done:**
- [ ] Code is written in a clear, readable, and consistent style
- [ ] Follows Python conventions (PEP8 or as agreed by the group)
- [ ] Includes meaningful comments or docstrings where appropriate
- [ ] Feature or fix fulfills the ticket's description and acceptance criteria
- [ ] Has been tested manually and/or with automated tests (if relevant)
- [ ] 100% unit test coverage added or updated
- [ ] Handles common edge cases and invalid inputs gracefully
- [ ] Changes are committed with a clear, descriptive message
- [ ] Code is pushed to a dedicated feature branch
- [ ] A pull request (PR) is created for review before merging into main
- [ ] PR includes a short summary of the change and screenshots (if applicable)
- [ ] README or inline docs updated if the change affects how to use or run the program
- [ ] New functions or modules include docstrings (at least 1–2 lines explaining what it does)
- [ ] At least one other person has reviewed and approved the pull request
- [ ] All review comments have been addressed or discussed
- [ ] The branch has been tested after merging to ensure no breakages

---
## 🧪 Testing & Validation

### 🔧 Write tests for word selection function
**Definition of Done:**
- [ ] Code is written in a clear, readable, and consistent style
- [ ] Follows Python conventions (PEP8 or as agreed by the group)
- [ ] Includes meaningful comments or docstrings where appropriate
- [ ] Feature or fix fulfills the ticket's description and acceptance criteria
- [ ] Has been tested manually and/or with automated tests (if relevant)
- [ ] 100% unit test coverage added or updated
- [ ] Handles common edge cases and invalid inputs gracefully
- [ ] Changes are committed with a clear, descriptive message
- [ ] Code is pushed to a dedicated feature branch
- [ ] A pull request (PR) is created for review before merging into main
- [ ] PR includes a short summary of the change and screenshots (if applicable)
- [ ] README or inline docs updated if the change affects how to use or run the program
- [ ] New functions or modules include docstrings (at least 1–2 lines explaining what it does)
- [ ] At least one other person has reviewed and approved the pull request
- [ ] All review comments have been addressed or discussed
- [ ] The branch has been tested after merging to ensure no breakages

---

### 🔧 Write tests for display function
**Definition of Done:**
- [ ] Code is written in a clear, readable, and consistent style
- [ ] Follows Python conventions (PEP8 or as agreed by the group)
- [ ] Includes meaningful comments or docstrings where appropriate
- [ ] Feature or fix fulfills the ticket's description and acceptance criteria
- [ ] Has been tested manually and/or with automated tests (if relevant)
- [ ] 100% unit test coverage added or updated
- [ ] Handles common edge cases and invalid inputs gracefully
- [ ] Changes are committed with a clear, descriptive message
- [ ] Code is pushed to a dedicated feature branch
- [ ] A pull request (PR) is created for review before merging into main
- [ ] PR includes a short summary of the change and screenshots (if applicable)
- [ ] README or inline docs updated if the change affects how to use or run the program
- [ ] New functions or modules include docstrings (at least 1–2 lines explaining what it does)
- [ ] At least one other person has reviewed and approved the pull request
- [ ] All review comments have been addressed or discussed
- [ ] The branch has been tested after merging to ensure no breakages

---
## 💡 Stretch Goals

### 🔧 Load word list from external file
**Definition of Done:**
- [ ] Code is written in a clear, readable, and consistent style
- [ ] Follows Python conventions (PEP8 or as agreed by the group)
- [ ] Includes meaningful comments or docstrings where appropriate
- [ ] Feature or fix fulfills the ticket's description and acceptance criteria
- [ ] Has been tested manually and/or with automated tests (if relevant)
- [ ] 100% unit test coverage added or updated
- [ ] Handles common edge cases and invalid inputs gracefully
- [ ] Changes are committed with a clear, descriptive message
- [ ] Code is pushed to a dedicated feature branch
- [ ] A pull request (PR) is created for review before merging into main
- [ ] PR includes a short summary of the change and screenshots (if applicable)
- [ ] README or inline docs updated if the change affects how to use or run the program
- [ ] New functions or modules include docstrings (at least 1–2 lines explaining what it does)
- [ ] At least one other person has reviewed and approved the pull request
- [ ] All review comments have been addressed or discussed
- [ ] The branch has been tested after merging to ensure no breakages

---

### 🔧 Add difficulty levels (easy/medium/hard)
**Definition of Done:**
- [ ] Code is written in a clear, readable, and consistent style
- [ ] Follows Python conventions (PEP8 or as agreed by the group)
- [ ] Includes meaningful comments or docstrings where appropriate
- [ ] Feature or fix fulfills the ticket's description and acceptance criteria
- [ ] Has been tested manually and/or with automated tests (if relevant)
- [ ] 100% unit test coverage added or updated
- [ ] Handles common edge cases and invalid inputs gracefully
- [ ] Changes are committed with a clear, descriptive message
- [ ] Code is pushed to a dedicated feature branch
- [ ] A pull request (PR) is created for review before merging into main
- [ ] PR includes a short summary of the change and screenshots (if applicable)
- [ ] README or inline docs updated if the change affects how to use or run the program
- [ ] New functions or modules include docstrings (at least 1–2 lines explaining what it does)
- [ ] At least one other person has reviewed and approved the pull request
- [ ] All review comments have been addressed or discussed
- [ ] The branch has been tested after merging to ensure no breakages

---

### 🔧 Add multiplayer or 2-player mode
**Definition of Done:**
- [ ] Code is written in a clear, readable, and consistent style
- [ ] Follows Python conventions (PEP8 or as agreed by the group)
- [ ] Includes meaningful comments or docstrings where appropriate
- [ ] Feature or fix fulfills the ticket's description and acceptance criteria
- [ ] Has been tested manually and/or with automated tests (if relevant)
- [ ] 100% unit test coverage added or updated
- [ ] Handles common edge cases and invalid inputs gracefully
- [ ] Changes are committed with a clear, descriptive message
- [ ] Code is pushed to a dedicated feature branch
- [ ] A pull request (PR) is created for review before merging into main
- [ ] PR includes a short summary of the change and screenshots (if applicable)
- [ ] README or inline docs updated if the change affects how to use or run the program
- [ ] New functions or modules include docstrings (at least 1–2 lines explaining what it does)
- [ ] At least one other person has reviewed and approved the pull request
- [ ] All review comments have been addressed or discussed
- [ ] The branch has been tested after merging to ensure no breakages

---

### 🔧 Add GUI using `tkinter`
**Definition of Done:**
- [ ] Code is written in a clear, readable, and consistent style
- [ ] Follows Python conventions (PEP8 or as agreed by the group)
- [ ] Includes meaningful comments or docstrings where appropriate
- [ ] Feature or fix fulfills the ticket's description and acceptance criteria
- [ ] Has been tested manually and/or with automated tests (if relevant)
- [ ] 100% unit test coverage added or updated
- [ ] Handles common edge cases and invalid inputs gracefully
- [ ] Changes are committed with a clear, descriptive message
- [ ] Code is pushed to a dedicated feature branch
- [ ] A pull request (PR) is created for review before merging into main
- [ ] PR includes a short summary of the change and screenshots (if applicable)
- [ ] README or inline docs updated if the change affects how to use or run the program
- [ ] New functions or modules include docstrings (at least 1–2 lines explaining what it does)
- [ ] At least one other person has reviewed and approved the pull request
- [ ] All review comments have been addressed or discussed
- [ ] The branch has been tested after merging to ensure no breakages

---
## 📋 Docs & Collaboration

### 🔧 Document how to run the game
**Definition of Done:**
- [ ] Code is written in a clear, readable, and consistent style
- [ ] Follows Python conventions (PEP8 or as agreed by the group)
- [ ] Includes meaningful comments or docstrings where appropriate
- [ ] Feature or fix fulfills the ticket's description and acceptance criteria
- [ ] Has been tested manually and/or with automated tests (if relevant)
- [ ] 100% unit test coverage added or updated
- [ ] Handles common edge cases and invalid inputs gracefully
- [ ] Changes are committed with a clear, descriptive message
- [ ] Code is pushed to a dedicated feature branch
- [ ] A pull request (PR) is created for review before merging into main
- [ ] PR includes a short summary of the change and screenshots (if applicable)
- [ ] README or inline docs updated if the change affects how to use or run the program
- [ ] New functions or modules include docstrings (at least 1–2 lines explaining what it does)
- [ ] At least one other person has reviewed and approved the pull request
- [ ] All review comments have been addressed or discussed
- [ ] The branch has been tested after merging to ensure no breakages

---

### 🔧 Add a contribution guide
**Definition of Done:**
- [ ] Code is written in a clear, readable, and consistent style
- [ ] Follows Python conventions (PEP8 or as agreed by the group)
- [ ] Includes meaningful comments or docstrings where appropriate
- [ ] Feature or fix fulfills the ticket's description and acceptance criteria
- [ ] Has been tested manually and/or with automated tests (if relevant)
- [ ] 100% unit test coverage added or updated
- [ ] Handles common edge cases and invalid inputs gracefully
- [ ] Changes are committed with a clear, descriptive message
- [ ] Code is pushed to a dedicated feature branch
- [ ] A pull request (PR) is created for review before merging into main
- [ ] PR includes a short summary of the change and screenshots (if applicable)
- [ ] README or inline docs updated if the change affects how to use or run the program
- [ ] New functions or modules include docstrings (at least 1–2 lines explaining what it does)
- [ ] At least one other person has reviewed and approved the pull request
- [ ] All review comments have been addressed or discussed
- [ ] The branch has been tested after merging to ensure no breakages

---

### 🔧 Create example issue template
**Definition of Done:**
- [ ] Code is written in a clear, readable, and consistent style
- [ ] Follows Python conventions (PEP8 or as agreed by the group)
- [ ] Includes meaningful comments or docstrings where appropriate
- [ ] Feature or fix fulfills the ticket's description and acceptance criteria
- [ ] Has been tested manually and/or with automated tests (if relevant)
- [ ] 100% unit test coverage added or updated
- [ ] Handles common edge cases and invalid inputs gracefully
- [ ] Changes are committed with a clear, descriptive message
- [ ] Code is pushed to a dedicated feature branch
- [ ] A pull request (PR) is created for review before merging into main
- [ ] PR includes a short summary of the change and screenshots (if applicable)
- [ ] README or inline docs updated if the change affects how to use or run the program
- [ ] New functions or modules include docstrings (at least 1–2 lines explaining what it does)
- [ ] At least one other person has reviewed and approved the pull request
- [ ] All review comments have been addressed or discussed
- [ ] The branch has been tested after merging to ensure no breakages

---

## 🧱 Software Architecture

### 🧭 Design and Document the Software Architecture

Create a clear plan for the structure of the codebase, including separation of concerns and responsibilities between modules (e.g., game logic, input/output, utilities, etc.). The architecture should support testing, extensibility, and clear readability for contributors.

**Tasks may include:**
- Creating a system diagram or flowchart
- Designing module boundaries and file structure
- Documenting decisions in a dedicated `docs/architecture.md` file
- Proposing structure in a GitHub issue or pull request

**Definition of Done:**
- [ ] Code is written in a clear, readable, and consistent style
- [ ] Follows Python conventions (PEP8 or as agreed by the group)
- [ ] Includes meaningful comments or docstrings where appropriate
- [ ] Feature or fix fulfills the ticket's description and acceptance criteria
- [ ] Has been tested manually and/or with automated tests (if relevant)
- [ ] 100% unit test coverage added or updated (if applicable)
- [ ] Handles common edge cases and invalid inputs gracefully
- [ ] Changes are committed with a clear, descriptive message
- [ ] Code is pushed to a dedicated feature branch
- [ ] A pull request (PR) is created for review before merging into main
- [ ] PR includes a short summary of the change and screenshots (if applicable)
- [ ] README or inline docs updated if the change affects how to use or run the program
- [ ] New functions or modules include docstrings (at least 1–2 lines explaining what it does)
- [ ] At least one other person has reviewed and approved the pull request
- [ ] All review comments have been addressed or discussed
- [ ] The branch has been tested after merging to ensure no breakages
