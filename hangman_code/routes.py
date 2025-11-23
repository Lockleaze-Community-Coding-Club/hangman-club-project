"Purpose: Define HTTP endpoints and orchestrate interactions between the Game logic, Persistence, and Templates."

def index ():
    return "none"

def new_game ():
    return "none"

def guess ():
    return "none"

def admin ():
    return "none"

def resume_game ():
    return "none"

"Relationship to user - Recieves HTTP requests from and sends back", "HTTP/HTTPS"

def send_request ():
    return "none"

"Relationship to app.py - Registered in Flask app"

def send_registration():
    return "none"

"Relationship to game_py, start, guess, win/loss"

def play_game():
    return "none"

"Relationship to templates, Renders pages via"

def get_render():
    return "none"

"Relationship to word_selection_py - Gets random word from"

def get_word():
    return "none"

