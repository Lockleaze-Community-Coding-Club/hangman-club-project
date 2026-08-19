from hangman_code.game import Game
from hangman_code.word_selection import (choose_word,
                                         parse_words)
#from hangman_code.functions_for_play_game.data_handling import from_dict
from hangman_code.functions_for_play_game.data_handling import to_dict
from hangman_code.functions_for_play_game.data_handling import read_and_find


def new_game(player_name, available_words_list):

    try:
        chosen_word, updated_list = choose_word(available_words_list)
    except:
        available_words_list = parse_words("hangman_code/words.txt")
        chosen_word, updated_list = choose_word(available_words_list)

    game = Game(
        player_name=player_name,
        word=chosen_word
    )


def load_game(player_name):
    # Perstistance is checked
    # If an object exists with game_status 2 AND player name matches, 
    # return that object
    # If such an object does not exist, return a new game object
    game = read_and_find(player_name)
    if game is type(Game):
        return game
    else:
        game = new_game(player_name)
        return game




 


def save_available_words(words):
    to_dict(words,"available_words_list.json")

"""def resume_game (game_status):
    
    # Consider that this enum class exists in game.py in the function design
     # You will need to create a object from Game
     # use data from from_dict for this

     #class Game_status(Enum): 
        #NEW_GAME = 0
        #IN_PLAY = 1
        #WON = 2
        #LOST = 3

        # Return the game object
    game_object = {game_status : 1} # placeholder until game_object is 
    initialised properly
    return game_object """


