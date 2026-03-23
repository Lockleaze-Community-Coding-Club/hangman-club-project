#from hangman_code.word_selection import choose_word
#from hangman_code.game import Game
#from hangman_code.functions_for_play_game.data_handling import from_dict
#from enum import Enum


def new_game (Game_status, player_name):

## IF THERE NO GAME WITH STATUS IN PLAY (IN PERSISTANCE) THEN START A NEW GAME
# IF THERE IS A GAME IN PERSISTANCE WITH STATUS IN PLAY THEN RESUME THE GAME
# To resume the game call def resume_game => to be written belo
## NEEDS TO TAKE PLAYERS_NAME AS A PARAMETER FROM THE INDEX HTML
#-----------------------------------------------------------------------

#NEW GAME MUST MUTATE GUESSED_WORD INTO A LIST OF THE SAME LENGTH AS WORD
#E.G IF WORD IS "DOG", "GUESSED WORD MUST BECOME ["_","_","_"]

#-----------------------------------------------------------------------

    # Will also need to consider how this interacts with player
    # get word from word selection
    # Mutate guessed word into a list
    # get game object and data from data_handling.initialise_game_and_data
    # Consider that this enum class exists in game.py in the function design

     #class Game_status(Enum): 
        #NEW_GAME = 0
        #IN_PLAY = 1
        #WON = 2
        #LOST = 3
    # You will need to make a new object of game
    # You will need to get hold of all of the other persistence data (such
    # as cumululative score etc) via data_handling
    game_object = {Game_status : 0} # placeholder result until game_object is initialised properly
    return game_object

# or 

def resume_game (Game_status):
    
    # Consider that this enum class exists in game.py in the function design
     # You will need to create a object from Game
     # use data from from_dict for this

     #class Game_status(Enum): 
        #NEW_GAME = 0
        #IN_PLAY = 1
        #WON = 2
        #LOST = 3

        # Return the game object
    game_object = {Game_status : 1} # placeholder until game_object is initialised properly
    return game_object

def Start_game(current_game, letter):
    test = current_game["used_letters"].append(letter)  # modifies in place
    print(test)
    return current_game
