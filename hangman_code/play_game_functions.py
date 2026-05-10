from hangman_code.functions_for_play_game.game_status_function import (
    current_game_status,
    is_won,
    is_lost,
)

from hangman_code.functions_for_play_game.make_guess import (
    make_guess,
    remaining_attempts_function,
    update_score_function,
)

from hangman_code.game import (

    get_attempts_remaining,
    get_current_score,

)


def play_game(game, letter: str):
        
        #-----------get results of guess---------------
        results = make_guess(
                letter, 
                game["word"], 
                game["word_progress"]
                )        
        #-----------calculate game status--------------
        # attempts_remaining is an input needed to 
        # calculate the current game status        

        game["attempts_remaining"] = remaining_attempts_function(
                get_attempts_remaining(game),
                results.get("letter_found")
                )
        remaining_attempts = game["attempts_remaining"]
        #Next, update the status of the game object e.g.
        # Is Won, Is Lost, In Play
        game["game_status"] = current_game_status(
                results.get("word_progress"),remaining_attempts)

        game_status = game["game_status"]
        #-------------update message---------------------------
        message = results.get("message")
        game["message"] = message
        #update the word progress within the game object

        #------------update letters and words--------------------
        word_progress = results.get("word_progress")
        game["word_progress"] = word_progress

        if results.get("letter_found"):
                game["accepted_letters"].append(letter)
        else:
                game["used_letters"].append(letter)

        #--------------update the score-------------------------        

        current_score=update_score_function(get_current_score(game))
        game["current_score"] = current_score
        #-------------run game logic-----------------------------
        if game_status == 1: #"In Play

                return game
        #This will re-set the screen to allow the user 
        # to set up a new guess

        elif game_status == 2: # "Is Won" in Enum
                result = is_won(game)
                return result
                # offer a new game to player

        elif game_status == 3: #"Is Lost" in Enum
                result = is_lost(game)
                return result
                #offer a new game to player


