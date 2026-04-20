from hangman_code.functions_for_play_game.game_status_function import (
    Current_game_status,
    is_won,
    is_lost,
)

from hangman_code.functions_for_play_game.make_guess import (
    Make_guess,
    remaining_attempts_function,
    update_score_function,
)

from hangman_code.game import (
    set_message,
    set_game_status,
    set_word_progress,
    get_attempts_remaining,
    set_attempts_remaining,
    get_current_score,
    set_current_score,
    set_accepted_letters,
    set_used_letters,
)


def play_game(game, letter: str):
       
        results = Make_guess(letter, game["word"], game["word_progress"])        
        #This will update the status of the game object e.g.
        # Is Won, Is Lost, In Play                        
        attempts_remaining = remaining_attempts_function(get_attempts_remaining(game))
        current_game_status = Current_game_status(results.get("word_progress"))
        set_game_status(game,current_game_status)

        if current_game_status == 1: #"In Play via enum"
        # update the message to the player on the results within game object
                message = results.get("message")
                set_message(game,message)
                #update the word progress within the game object
                word_progress = results.get("word_progress")
                set_word_progress(game,word_progress)
                #update remaining attempts within the game object
                set_attempts_remaining(game,attempts_remaining)
                #update the score        
                current_score=update_score_function(get_current_score(game))
                set_current_score(game,current_score)
                if results.get("letter_found")==True:
                        #update accepted letters
                        set_accepted_letters(game,letter)
                elif results.get("letter_found")==False:
                        #or update used letters
                        set_used_letters(game,letter)                              
                return game
        #This will re-set the screen to allow the user 
        # to set up a new guess

        elif current_game_status == 2: # "Is Won" in Enum
                result = is_won(game)
                return result
                # offer a new game to player

        elif current_game_status == 3: #"Is Lost" in Enum
                result = is_lost(game)
                return result
                #offer a new game to player


