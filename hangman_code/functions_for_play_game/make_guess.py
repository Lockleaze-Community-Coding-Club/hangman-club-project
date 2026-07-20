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
#This function will update the number of remaining attempts left
def remaining_attempts_function(attempts_remaining, letter_found):
       if letter_found:
              return attempts_remaining
       else:
              if attempts_remaining>0:
                      attempts_remaining=attempts_remaining-1
                      return attempts_remaining
              else:
                      attempts_remaining = ValueError
                      return attempts_remaining
              
def update_score_function(current_score, attempts_remaining):
       #This function will update the score
       return current_score