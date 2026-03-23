def Make_guess(letter, word, guessed_word):

        letter_found = False
                
        word_with_guessed_letters = list(guessed_word)
                
        for i,x in enumerate(word):

                if letter == x:
                                
                        word_with_guessed_letters [i] = letter
                        letter_found = True

        if letter_found:
                return {
                "success": True,
                "message": "Good job genius",
                "word_progress": word_with_guessed_letters
                }
        
        else:
                return {
                "success": False,
                "message": "Bad guess you lemon",
                "word_progress": word_with_guessed_letters
                }

## ADD THESE IN AS UPDATES IN MAKE GUESS

def remaining_attempts_function(attempts_remaining):
       #This function will update the number of remaining attempts left
       return attempts_remaining

def update_score_function(current_score):
       #This function will update the score
       return current_score