
def current_game_status(word_progress, attempts_remaining):
       #This function will update the status of the game e.g.
       # Is Won, Is Lost, In Play
       #Set it to return 1 for trial purposes. Function needs written.
       # Remember that game_status is an enum
       return 1

def is_won(game):
    #update_data()
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

def is_lost(game):
    #update_data()
    # similar to above in reverse
    return None

def is_closed(load_game,json_filename, data ):
    #This is a function for if the game is exited:
    # A global update of all data shall be required
        #e.g. cumulative data, number of games won etc
    #to_dict(data, json_filename)
    return None


def factory_reset(load_game):
     return None
#This will re-set the game and return all scores to 0


