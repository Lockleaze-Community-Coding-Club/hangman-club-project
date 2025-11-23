"Purpose: Core game rules and state management"
"Implements hangman rules and game state management"
"Relationships to main.py - recieves the selected word "
"from main and provides feedback on the guess"
"Relationships to main.py - recieves the selected guess"
" letter from main and provides feedback on the guess"
"Uses for game operations (start, guess, win/loss)"


class Game("word"):

    def _init_(self):
        #this is the constructor
        # should could contain the variables needed like word etc
        #self.word etc
        return None

    def make_guess(letter, word):
        # calls on the recieve request function from convertor.py 
        # to find out the selection from the user
        # returns the updated Game object to main
        return None
        
    def is_itwon():
        # uses the output from make_guess to work out if the game 
        # has been won or not and tells the main programme the status
        return None

    def remaining_attempts(number):
        number -= 1
        return(number)

    def display_word():
        return None
        
    def to_dict(self):
        # this function is to store the game progress into the 
        # persistence file so that it can be resumed later
        """For example, the word, (correctly) guessed_letters, 
        attempts_left, wrong_guesses (letters) and game status is saved"""
        """The keys should be defined"""
        return None

    def from_dict(data):
        # this function is to restore the game progress 
        # from the persistence file if the game is resumed later
        return None
        







