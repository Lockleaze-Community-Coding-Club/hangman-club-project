"Loads, filters, and sanitises words "
"for new games"
"Purpose: Load and sanitise word lists and "
"provide get_random_word()."
"Relationship to main.py => recieves a request for a "
"new word and returns a random work"

#from persistence import Persistence

class Word_selection():
    
    def parse_words(words_file):
        with open(words_file, "r") as words_file:
            lines = words_file.readlines()
            print(lines)

    def choose_word():
        return None
    
    #def load_words():
        #return "none"
    
    def sanitize_word(word):
        return None
    
    def filter_words(words, min_length=4, max_length=10):
        return None

    def get_random_word():
        return None 
 
 




