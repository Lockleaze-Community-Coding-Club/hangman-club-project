
## Tidy up per meeting 16th march

#from word_selection import choose_word
#from game import Game
#from templates import Template

#-----------------------------------------------------------------------------
"""These are the functions used in the main programme"""
#-----------------------------------------------------------------------------

# these functions are all in the functions_for_play_game folder

#-----------------------------------------------------------------------------

from hangman_code.functions_for_play_game.make_guess import Make_guess
from hangman_code.functions_for_play_game.game_status_function import Current_game_status
#from hangman_code.functions_for_play_game.start_game import Start_game
#from hangman_code.functions_for_play_game.game_status_function import setup_new_guess
from hangman_code.functions_for_play_game.game_status_function import is_won
from hangman_code.functions_for_play_game.game_status_function import is_lost
#from hangman_code.functions_for_play_game.game_status_function import is_closed
from hangman_code.functions_for_play_game.data_handling import update_in_play_data
from hangman_code.functions_for_play_game.start_game import new_game
#-----------------------------------------------------------------------------
"""The list of public parameters for playing :
These are needed as user inputs from app"""
#-----------------------------------------------------------------------------

letter = None
player_name = None

#-----------------------------------------------------------------------------
"""Below is the list of private parameters for running main"""
"""Else, the list of parameters for playing the Game is within Game.py"""
#-----------------------------------------------------------------------------

json_filename = "persistence.json"
Game_status = 1
#-----------------------------------------------------------------------------
"""This is the constructor for the dictionary with various the
inputs needed in functions_for_play_game.The initialised data itself is in
game.py"""
#-----------------------------------------------------------------------------

# Now moved into data_handling so that all data and data handling are 
# kept together (Seperation of concerns)

#-----------------------------------------------------------------------------
"""These are the functions used in the main programme"""
#-----------------------------------------------------------------------------

# I have moved these functions into the functions_for_play_game folder

#-----------------------------------------------------------------------------
"""This is the actual game logic / flow / main programme"""
#-----------------------------------------------------------------------------


current_game = new_game(Game_status, player_name)


def play_game(current_game: dict, letter, word_attempt):
       
        game = current_game
        #game = Start_game(current_game, letter)
        # i.e. needs the letter from the user and the game object which is the
        #return from Start_game_selection

        while game["attempts_remaining"] > 0 and not game_closed:


                #try:
                       
                        #Validate_input(letter, game["used_letters"])

                
                #except (TypeError, ValueError):
                        #game["message"] = "Invalid input, try again"
                        #return game


                #else:
                        results = Make_guess(letter, game["word"], game["guessed_word"])
                        #This will update the status of the game e.g.
                                # Is Won, Is Lost, In Play                        
                        current_game_status = Current_game_status(results)
                        #These are the results returned from make guess

                        message = results.get("message")
                        guess_result = results.get("success")
                        word_progress = results.get("word_progress")
                        #This will update the status of the game e.g.
                                # Is Won, Is Lost, In Play


                        if current_game_status == 1: #"In Play via enum"

                                in_play_game = update_in_play_data(
                                 current_game, 
                                 letter, 
                                 word_progress, 
                                 message, 
                                 guess_result, 
                                 current_game["attempts_remaining"], 
                                 current_game["current_score"], 
                                 word_attempt
                                        )
                                
                                return in_play_game
                                #This will re-set the screen to allow the user 
                                # to set up a new guess

                        elif current_game_status == 2: # "Is Won" in Enum
                               is_won()
                               Start_game_Selection(load_game)
                                # if new game, return to play game
                                #this logic should go into the
                                #Start_game_selection function
                                      
                               
                        elif current_game_status == 3: #"Is Lost" in Enum
                                is_lost()
                                Start_game_Selection(load_game)
                                # if new game, return to play game
                                #this logic should go into the
                                #Start_game_selection function

                        #finally:
                                #is_closed(load_game == 4, json_filename, game)
                                
                       #Logic to be worked out
         #The dictionary will now be updated - ready to store in persistence
         # if we wanted to resume the game later"""

