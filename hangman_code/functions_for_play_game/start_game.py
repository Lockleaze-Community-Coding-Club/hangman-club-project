from hangman_code.word_selection import choose_word
from hangman_code.game import Game
from hangman_code.functions_for_play_game.data_handling import from_dict
from enum import Enum


def Start_game_Selection(load_game):
    #User can select either start a new game, resume game, exit game
    # or factory reset. The input to this function is an enum
#class load_game(Enum): 
        #NEW_GAME = 1
        #RESUME_GAME = 2
        #FACTORY_RESET = 3
        #EXIT_GAME = 4


  # there will be some sort of 'if' selection: e.g. a NEW_GAME will call the
  #new_game function


    # To create all of these functions:

    # Write a test in test_start_game_selection - check it fails (Click 
    # on the scientific jar logo on the menu on the left to run the test)
    # This test should be for the most the most basic first step of the 
    #function
    # Then write the function code to pass the test. Check the test passes: 
    # Then write the next test the function has to pass - check the test fails
    # Then write the function code to pass the test
    # So on and so forth

#---------------------------------------------------------------
#THE BELOW IS RUBBISH CODE BEING USED FOR DEBUGGING - DELETE IT ONCE YOU
#HAVE WRITTEN REAL CODE
#--------------------------------------------------------------------------


    if load_game == "1":
        game_object = {
    "game_name" : '', # I haven't used this elsewhere. Is it in app?
    "word" : ["C","A","T"],
    "game_id": 1,
    "current_score": 0,
    "template": None,
    "message": "game message",
    "used_letters": [""],
    "game_started": True,
    "current_game_status": 0,
    "accepted_letters": [],
    "guess_result": [""],
    "attempts_remaining": 10,
    "guessed_word": ["_","_","_"],
    "words_guessed": [""],
    "Start_Game_Selection": "",
    "game_closed": False,
    "cumulative_score": 0,
    "number_of_games_played": 0,
    "number_of_games_won": 0
}
        return game_object

    elif load_game == "2":
        game_object = {
    "game_name" : "Betty", # I haven't used this elsewhere. Is it in app?
    "word" : ["D","O","G"],
    "game_id": 1,
    "current_score": 0,
    "template": None,
    "message": "game message",
    "used_letters": ["D","G"],
    "game_started": True,
    "current_game_status": 1,
    "accepted_letters": [],
    "guess_result": [""],
    "attempts_remaining": 10,
    "guessed_word": ["_","_","_"],
    "words_guessed": [""],
    "Start_Game_Selection": "",
    "game_closed": False,
    "cumulative_score": 600,
    "number_of_games_played": 0,
    "number_of_games_won": 0
}    
        return game_object        

    elif load_game == "3":
        game_object = {
        "game_name" : '', # Should ideally be renamed to player_name
        "word" : ["D","O","G"],
        "game_id": 1,
        "current_score": 0,
        "template": None,
        "message": "game message",
        "used_letters": [""],
        "game_started": True,
        "current_game_status": 0,
        "accepted_letters": [],
        "guess_result": [""],
        "attempts_remaining": 10,
        "guessed_word": [""],
        "words_guessed": [""],
        "Start_Game_Selection": "",
        "game_closed": False,
        "cumulative_score": 0,
        "number_of_games_played": 0,
        "number_of_games_won": 0
        }
        return game_object 
   
    else:
         return None



def new_game (Game_status):
    
#-----------------------------------------------------------------------

#NEW GAME MUST MUTATE GUESSED_WORD INTO A LIST OF THE SAME LENGTH AS WORD
#E.G IF WORD IS "DOG", "GUESSED WORD MUST BECOME ["_","_","_"]

#-----------------------------------------------------------------------


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