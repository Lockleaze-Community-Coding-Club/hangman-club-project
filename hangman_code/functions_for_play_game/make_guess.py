def make_guess(letter, word, word_progress):

        letter_found = False
                
        word_with_guessed_letters = list(word_progress)


        if len(word) == len(word_progress):

                
                for i,x in enumerate(word):

                        if letter == x :
                                        
                                word_with_guessed_letters [i] = letter
                                letter_found = True


                if letter_found:
                        return {
                        "message": "Good job genius",
                        "word_progress": word_with_guessed_letters,
                        "letter_found": True
                        }
                
                else:
                        return {
                        "message": "Bad guess you lemon",
                        "word_progress": word_with_guessed_letters,
                        "letter_found": False                
                        }
        else:
                raise ValueError

# ADD THESE IN AS UPDATES IN MAKE GUESS

def remaining_attempts_function(attempts_remaining, letter_found):
       #This function will update the number of remaining attempts left
       return attempts_remaining

def update_score_function(current_score):
       #This function will update the score
       return current_score