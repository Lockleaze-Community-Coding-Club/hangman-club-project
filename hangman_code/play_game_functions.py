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

    #get_attempts_remaining,
    #get_current_score,
    Game

)

def play_game(game, letter: str):
        #-----------print type of game ---------------
        print(type(game))

        #-----------get results of guess---------------
        results = make_guess(
                letter,
                Game.get_word(game),
                Game.get_word_progress(game)
                )        
        #-----------calculate game status--------------
        # attempts_remaining is an input needed to 
        # calculate the current game status        
        x = Game.get_attempts_remaining(game)
        y = remaining_attempts_function(x,results.get("letter_found"))
        Game.set_attempts_remaining(game,y)
        remaining_attempts = Game.get_attempts_remaining(game) 


        #Update the status of the game object e.g.
        # Is Won, Is Lost, In Play

        z = current_game_status(
                results.get("word_progress"),remaining_attempts)
        Game.set_game_status(game,z)

        #-------------update message---------------------------
        message = results.get("message")
        Game.set_message(game,message)

        #------------update letters and word progress--------------------
        word_progress = results.get("word_progress")
        Game.set_word_progress(game,word_progress)

        if results.get("letter_found"):
                Game.set_accepted_letters(game,letter)
        # else:
                # Game.set_used_letters(letter)

        #--------------update the score-------------------------        
        a = Game.get_current_score(game)
        current_score=update_score_function(a)
        Game.set_current_score(game,current_score)
        #-------------run game logic-----------------------------
        if game.game_status == 1: #"In Play

                return game
        #This will re-set the screen to allow the user 
        # to set up a new guess

        elif game.game_status == 2: # "Is Won" in Enum
                result = is_won(game)
                return result
                # offer a new game to player

        elif game.game_status == 3: #"Is Lost" in Enum
                result = is_lost(game)
                return result
                #offer a new game to player

