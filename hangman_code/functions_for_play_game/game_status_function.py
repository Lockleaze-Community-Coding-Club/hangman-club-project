from enum import Enum
from hangman_code.functions_for_play_game.data_handling import to_dict
from hangman_code.functions_for_play_game.data_handling import update_data
#from hangman_code.functions_for_play_game.scores_and_attempts_function import remaining_attempts_function
#from hangman_code.functions_for_play_game.scores_and_attempts_function import update_score_function
#from hangman_code.functions_for_play_game.scores_and_attempts_function import update_cunulative_number_of_games_played
#from hangman_code.functions_for_play_game.scores_and_attempts_function import update_cunulative_number_of_games_won
#from hangman_code.functions_for_play_game.scores_and_attempts_function import update_cunulative_score_function
#from hangman_code.functions_for_play_game.player import Player
#--------------------------------------------------------------------------



class Game_status(Enum): # RP: I have made a note of this 
        # in game_status_function
        NEW_GAME = 0
        IN_PLAY = 1
        WON = 2
        LOST = 3

#--------------------------------------------------------------------------

def Current_game_status(results):
       #This function will update the status of the game e.g.
       # Is Won, Is Lost, In Play
       #Set it to return 1 for trial purposes. Function needs written.
       return 1

def is_won():
    update_data()
    # takes an input from game_status
    # store game status / history (to dict)
    # include a running total of how many games have been played
    # include a cumulative total of how many games have been won
    # display the "you have won" screen
    # offer an option to start a new game
    return {
          "message": "You won the game, Would you like to play again?",
          "cumulative score":"",
          "No. of Games Won" : "",
           }

def is_lost():
    update_data()
    # similar to above in reverse
    return None

def is_closed(load_game,json_filename, data ):
    #This is a function for if the game is exited:
    # A global update of all data shall be required
        #e.g. cumulative data, number of games won etc
    to_dict(data, json_filename)
    return None

def setup_new_guess(in_play_data):
     return None
#This will re-set the screen to allow the user to set
                        #up a new guess


def factory_reset(load_game):
     return None
#This will re-set the game and return all scores to 0

#class load_game(Enum): 
        #NEW_GAME = 0
        #RESUME_GAME = 1
        #EXIT_GAME = 2
        #FACTORY_RESET = 3
##########################################################################
#FUNCTIONS BELOW NEED WORK
###########################################################################
def get_game_status(load_game):
        return current_game_status

def set_game_status(game, game_status):
        game_status = game_status
        return

def get_player_name(player, player_name):
        return player_name
    
def set_player_name(player, player_name):
        return  player_name