# 🎮 Hangman Web App – Architecture Overview
---
## 🏗️ Diagram
![Architecture Diagram](https://www.plantuml.com/plantuml/png/jLVDSjis4BxhAJQ-H9gHhPcqf_IIr4rYPvJQOycJwOa3aIiHCGYm02X5qycxTx44GSfX7FTG7n8IN7pxiz_-w8tpmlgcKfCNliGAGSbTwNTM72SlfCvLKo2KtjVkzM9XnU5Y9ttPR1g7DZVQe_ONkQaMjH8wW9mxNoYvMLp-UduRZku_BHULS1uj7MMNT4D8ZVQY9jd_0x-gZGvt67_o4aXkYNjKyCjhUA-4Uu3Fk86tTQraBhmq6Wwa3_0h8MYXu1QjamIdSuJfnzNDdx2L2cU4TAqLMGvaJ4KA75qXcwI6lDFfGEW2B2h6TQMitSLaidpxrytzEbk-Ux_Exgu_NAsdiyaaQ35w6foSmnavSaHxHa_tT00rlKgzWokXTvNGG3eeCTB2nfg38y5PSEpyMNyaUBD7AsnU1aXtT1uhs9X65y8UOMjiKlD1LFXyt1KZPRz7f6dPecGxGY57Xg1dC_XdCW7wUmc900wcbwzcV9hEfjkGe4pKDI6C9Yj0yPqMZIGlwkDh48DqRaNkZJroBeX0Mxc3Sx2uewG6hTOq7jrYengihQIa9RZ4dId1PVMHR6ZnGsA6XBbarCRoM_XuQL4GQEGNc-_GEyY7WdCeoII5BYGJI3DQCXNPpiVcWJUm5rQQXXwngbM0PyaGNZ2RBvXxTzQ6xzlaD8ef5RafCB3hw4lJPeA42ZoD8REDivPj6vqpSpccjj5iQgjIcPtCHq8rShiDtT28nQWEZYjRjGpWxDvMcKCulY6-elEM_MufjMlGENGKMa-dGDXYXw4IOSeDB3Al4W-OiUmSfCiEHlF_oZW_OnNreC2Bfg8QXLjhzh90HrwAWd5OCbaT0ftY5GuuG7d8Uagdz5AeONf6WXM-ZaGd8gPmtF3z0R66i92tUGxLB3rMPBHyG3RYO6mnXzhYFX177MF82b3ecLpeyw4hV25pg91JmavnM5ie0dQnf-MbCGx1qhEf-EDOsOJp4VSUQs57FmS5g-umd2mfzY6x8eJIHRfJxsNBMULlK7U9geLrcB73R5nycSwIVqF3UcfIlyjIMXyREYgMKhCq1xIWU9OaIV0c54ggao1O22yohdNAqPoFiy3PnlNix-XSP34t6Scp2-wKmeQGRSOO0PVYankBhRZmeJVu7dOEmqhO2oNf3cPIruq_RHOluLqtyDQflwGEmgsPkcRfApNeFniHoEIyiKIHqvx3aonBJOsYqCFwKdYmg0kqSPJ10JTfc9rsezDk5y8MEeF5uPJjOXkexkY4s-j8sXCMcPEU5pnchtktm_j7gR-8LmFbKqdcVhq80PZtVI2-vyfG8FXb1as8YJUTWpM5nesIiFM5bBKFRCUgzU-j2-E22twrciF75Jilgu3LAjWSEMxtr-DfFDrRlazascEUpA4oUfSHN9N5xo4oupTJrauH1hsLxWvDMj6zauKgUFkU7X8YlV_HMB7fZtWxIPs8UyCUUGHszE1QWA7QYo_Ew5aohoVMkfGEyXGOwVgLpviukMjhSdIC7GH4dhVzSo_5oTWeKT4hLAPe52Ozts9cllsdxUnkk2u-_o9TYzjZMbRkNOZ5rNfzIobdqdQZqpMRIdhNZr2BhgdIPCMlz36rhm2m2F-ipcQiveVTinzdbq8fn-dIU1XEgmYH97_SYLUe2_VuEXnAr13y18j_DyZpA0dzpBv-7jt5ot62BTgnWWMBaE7MLCp7Y0Hvy2V2T_5DpM68TxN-j4nVKl67QmFnLFbtk4KR6EH0SCadpKaQ5b6SgyJzpCNJWljivUDjOT5kIukkLhoP0vVTzUAcBSTPr360UYfFToYA9rMmJpzKChuk9X8p3M2BM6n4_i1G_Gxg3Jyp7OG3CKAq3cTKJyAd3sbbauxBZskUwoFi4pAFVYI5dV84d4BqVRwJCtSy4o9Bc1pSIXvFcuZGqIITixbsZwwZH2JDD4w9BgY9vqzbpLk913NSuPxCoTDeJ7-mg70lj8Umcd2y-aiKtz10IOtGUOxyApkcZWMUPlRFCdYgsPjU_9bwKynEAuZ7LFmTdq8cb4LH70DAx1XZ9TDt6_hwXeniAlKl)

---

## 🧠 Purpose
This document describes the architecture of the **Hangman Web Application**, implemented using **Flask** and structured according to the **C4 Model (up to Level 3)**.  
The system demonstrates separation of concerns between **web handling**, **game logic**, **presentation**, and **file-based persistence**.

---

## 🧩 C4 Model Overview

### Level 1: Context
The Hangman application allows a **Player** to play the game through a web browser.

**Primary Actor**
- **Player** — interacts with the system via HTTP.

---

### Level 2: Containers

| Container | Technology | Purpose |
|---------|-----------|---------|
| **Flask Web Application** | Python, Flask | Handles HTTP requests and responses. |
| **Python Game Code** | Python modules | Implements Hangman game rules and state management. |
| **Templates (UI)** | Jinja2, HTML, CSS | Renders the game in the browser. |
| **JSON File Storage** | JSON | Persists game state, scores, and word usage. |

---

### Level 3: Components

#### Flask Web Application
| Component | Description |
|---------|-------------|
| `app.py` | Creates and configures the Flask app, routes user actions to game logic, and renders templates. |

#### Python Game Code
| Component | Description |
|---------|-------------|
| `play_game_functions.py` | Orchestrates game flow and communicates with Flask. |
| `functions_for_play_game.py` | Provides low-level game logic functions. |
| `game.py` | Defines the game object and state. |
| `word_selection.py` | Loads, sanitises, and selects random words. |

#### User Interface
| Component | Description |
|---------|-------------|
| `templates/` | Jinja2 templates (`index.html`, `play_game.html`, `closed.html`). |
| `static/` | CSS, JavaScript, images. |

#### Persistence
| Component | Description |
|---------|-------------|
| `persistence.json` | Stores saved games, scores, and used words. |

---
## 🔄 Component Relationships

Player -> app.py  
app.py <-> play_game_functions.py  
play_game_functions.py <-> functions_for_play_game.py  
functions_for_play_game.py <-> game.py  
functions_for_play_game.py <-> word_selection.py  
functions_for_play_game.py <-> persistence.json  
app.py -> templates/ -> static/

<table>
  <thead>
    <tr>
      <th>From</th>
      <th>To</th>
      <th>Purpose</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Player</td>
      <td>app.py</td>
      <td>Plays the game via HTTP requests.</td>
    </tr>
    <tr>
      <td>app.py</td>
      <td>play_game_functions.py</td>
      <td>Sends user actions (new game, guesses).</td>
    </tr>
    <tr>
      <td>play_game_functions.py</td>
      <td>app.py</td>
      <td>Returns updated game state for rendering.</td>
    </tr>
    <tr>
      <td>play_game_functions.py</td>
      <td>functions_for_play_game.py</td>
      <td>Delegates detailed game logic.</td>
    </tr>
    <tr>
      <td>functions_for_play_game.py</td>
      <td>game.py</td>
      <td>Creates and updates the game object.</td>
    </tr>
    <tr>
      <td>functions_for_play_game.py</td>
      <td>word_selection.py</td>
      <td>Requests valid random words.</td>
    </tr>
    <tr>
      <td>functions_for_play_game.py</td>
      <td>persistence.json</td>
      <td>Reads/writes game state and scores.</td>
    </tr>
    <tr>
      <td>app.py</td>
      <td>templates/</td>
      <td>Renders UI using Jinja2.</td>
    </tr>
    <tr>
      <td>templates/</td>
      <td>static/</td>
      <td>Loads CSS, JS, and images.</td>
    </tr>
  </tbody>
</table>

## ⚙️ Persistence Strategy

**Technology:** JSON file (`persistence.json`)

**Responsibilities:**
- Store ongoing and completed games
- Track scores and attempts
- Prevent word reuse

**Access Pattern:**
- File I/O performed exclusively by game logic modules
- Flask layer does not access JSON directly

---

## 🧩 Responsibilities by Container

| Container | Responsibilities |
|---------|------------------|
| **Flask Web Application** | Handle HTTP requests, pass user input to game logic, render responses. |
| **Python Game Code** | Enforce rules, manage game state, choose words, validate input, calculate outcomes. |
| **Templates / Static** | Present game state visually in the browser. |
| **JSON Storage** | Persist game data between requests and sessions. |

---

## 🏁 Future Improvements

- Replace JSON file storage with SQLite or PostgreSQL
- Add user accounts and authentication
- Improve concurrency handling for multiple players
- Introduce API endpoints for a SPA or mobile client
