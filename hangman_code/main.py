# main program
from word_selection import Word_selection
from game import Game
from templates import Template

"Purpose: Define HTTP endpoints and orchestrate interactions between the Game logic, Persistence, and Templates."

# The user selects to either to start a new game or continue with the existing
# Choice of either new_game or resume_game
# CLicking either of these will start the game
# An object of class Game shall be retrieved to do this

def new_game ():
    # This shall call on the word_selection class to get a word and pass this into the game Class constructor
    # The output shall be returned to the user as an HTTP/HTTPS format via the convertor send_request function
    # The get_render function in templates will need to be called
    return None

# or 

def resume_game ():
    return None
    # This shall call on the from_dict function and pass data from persistance into the Game Class as the arguments
    # The output shall be returned to the user as an HTTP/HTTPS format via the convertor send_request function
    # It should flash up an error message to the user if there is no game to resume
    
# The user then enters the play game cycle and the first task is to make a guess:

attempts_remaining = 10

while attempts_remaining > 0:
    
    def play_game():
            # user makes a guess
        def guess ():
            # guess calling on make_guess from game, get_render from templates and then send_request from convertor
            return None
                # calculate result
            # Work out if game is won using Game.is_itwon
                # If not store information using Game.to_dict:
                    # Store used letters (to_dict)
                    # Store used word guesses (to_dict)
                    # Store games status e.g. mid-game 
                    # reduce number of attempts remaining
                    # Render and display to the user
                # If so :
                    # Break and go to is_won in main
                            
def is_won():
    # store game status / history (to dict)
    # include a running total of how many games have been played
    # include a cumulative total of how many games have been won
    # display the "you have won" screen
    return None


def is_lost():
    return None



# These 3 functions below are what chatGPT suggested to do with the flask app. I think they are needed to configure the new game
def index ():
    return None

def admin ():
    return None

"Relationship to app.py - Registered in Flask app"

def send_registration():
    return None









