#from hangman_code.word_selection import choose_word
#from hangman_code.game import Game
#from hangman_code.functions_for_play_game.data_handling import from_dict
#from enum import Enum


def new_game (game_status, player_name):


    game_object = {game_status : 0} # placeholder result until game_object is initialised properly
    return game_object

# or 

def resume_game (game_status):
    
    # Consider that this enum class exists in game.py in the function design
     # You will need to create a object from Game
     # use data from from_dict for this

     #class Game_status(Enum): 
        #NEW_GAME = 0
        #IN_PLAY = 1
        #WON = 2
        #LOST = 3

        # Return the game object
    game_object = {game_status : 1} # placeholder until game_object is initialised properly
    return game_object


