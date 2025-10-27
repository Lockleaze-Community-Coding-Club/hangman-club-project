# 🎮 Hangman Web App – Architecture Overview

## 🧠 Purpose
This document describes the architecture of the **Hangman Web Application**, designed for the community Python coding club. It uses a **Flask** web framework and a **JSON file** for persistence. The goal is to illustrate good design, modularity, and testing practices for beginner to intermediate learners.

---

## 🧩 C4 Model Overview

### Level 1: Context
The Hangman application allows users to play the classic word-guessing game in their browser. It interacts with a lightweight persistence layer that stores game state between sessions.

**Primary Actors:**
- **User** — interacts with the game through a web interface.
- **Flask Web App** — handles user input and renders HTML.
- **Persistence Store (JSON)** — saves and loads game data.

---

### Level 2: Containers

| Container | Technology | Purpose |
|------------|-------------|----------|
| **Flask Web App** | Python, Flask | Main application. Handles routing, templates, and business logic. |
| **Persistence Store** | JSON file | Provides durable storage for game sessions and player data. |

---

### Level 3: Components

| Component | Description |
|------------|--------------|
| `app.py` | Application entry point. Initializes Flask, configures routes, and registers blueprints. |
| `routes.py` | Defines the HTTP endpoints (`/`, `/guess`, `/new_game`, `/admin`). Handles user input and communicates with game logic. |
| `game.py` | Core game logic, including starting new games, processing guesses, and determining win/loss. |
| `word_selection.py` | Loads word lists, filters and sanitizes words for fairness. |
| `persistence.py` | Reads/writes game data to JSON. Provides functions for saving, loading, and deleting game states. |
| `templates/` | HTML templates rendered by Flask using Jinja2 (`index.html`, `game.html`). |
| `static/` | Contains CSS, images, and optional JavaScript. |
| `tests/` | Unit and integration tests using pytest. Includes tests for game logic, persistence, and Flask routes. |

---

## 🔄 Component Relationships

```text
app.py → routes.py → game.py → persistence.py → JSON file
                         ↘ word_selection.py
app.py → templates/, static/
tests/ → app.py, routes.py
```

| From | To | Purpose |
|------|----|----------|
| `app.py` | `routes.py` | Registers routes and creates the Flask app. |
| `app.py` | `templates/` | Provides UI rendering. |
| `app.py` | `static/` | Serves static files. |
| `routes.py` | `game.py` | Connects HTTP endpoints to game logic. |
| `game.py` | `word_selection.py` | Retrieves valid words for the game. |
| `game.py` | `persistence.py` | Saves and restores game state. |
| `routes.py` | `persistence.py` | Interacts with JSON data for admin functions. |
| `tests/` | `app.py` | Uses Flask’s test client for integration tests. |

---

## ⚙️ Persistence Strategy

**Technology:** JSON file (e.g., `data/games.json`)

**Advantages:**
- Simple for beginners to read/write.
- No setup required beyond Python’s standard library.
- Easy to upgrade to SQLite later.

**Persistence functions (in `persistence.py`):**
```python
save_game_state(game_id, data)
load_game_state(game_id)
delete_game_state(game_id)
list_saved_games()
```

---

## 🧩 Function Breakdown by Container

| Container | Functions / Responsibilities |
|------------|------------------------------|
| **app.py** | Initialize Flask app; configure routes; set up persistence path; run server. |
| **routes.py** | Define endpoints; manage user sessions; handle form submissions; render templates. |
| **game.py** | `start_game()`, `make_guess()`, `is_won()`, `is_lost()`, `remaining_attempts()`. |
| **word_selection.py** | `load_words()`, `filter_words()`, `sanitize_word()`. |
| **persistence.py** | `save_game_state()`, `load_game_state()`, `delete_game_state()`, `list_games()`. |
| **templates/** | `index.html`, `game.html` — front-end display logic using Jinja2. |
| **static/** | `style.css`, optional JS enhancements. |
| **tests/** | Unit + integration tests (`pytest`, `Flask test client`). |

---

## 🧪 Testing & Quality
- **Framework:** `pytest`
- **Test coverage:** 100% (target)
- **Testing layers:**
  - *Unit tests* for game logic and persistence.
  - *Integration tests* for routes and templates.
- **Continuous Integration:** GitHub Actions (pytest + flake8 linting)

---

## 🏁 Future Improvements
- Replace JSON with SQLite for multi-user persistence.
- Add user authentication.
- Introduce async requests for real-time game state updates.
- Extend test automation to include UI testing.

---

## 📘 Summary
This architecture separates concerns between the web interface, core game logic, and persistence layer, while remaining lightweight and fully Python-based.  
It is ideal for teaching maintainable design and prepares learners for more advanced concepts like databases, APIs, and CI/CD.
