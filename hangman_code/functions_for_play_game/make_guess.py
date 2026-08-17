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

              
#This function is only to be called when the game is over
#(The number of attempts unused should be an int.  We could solve this with an input validation.)
def update_score_function(current_score, attempts_remaining):
    match attempts_remaining:
        case 8:
            print("Fluke(?)!")
            new_score = current_score + 100
        case 7:
            new_score = current_score + 1000
        case 6 | 5:
            new_score = current_score + 800
        case 4 | 3:
            new_score = current_score + 500
        case 2:
            new_score = current_score + 100
        case 1:
            new_score = current_score + 5
        case _:
            print("That was close to failure.")
            new_score = current_score + 1
    return new_score