"Loads, filters, and sanitises words for new games"
"Relationship to routes.py => recieves a request for a new word and returns a random work"

def word_selection(word: str) -> str:
    

    def parse_words():
        return "none"

    def choose_word():
        return "none"

    the_word = word
    return the_word



#print("this is the word : ", word_selection('What'))
None

Purpose: Load and sanitise word lists and provide get_random_word().
- load_words(source='data/words.json')
- sanitize_word(word)
- filter_words(words, min_length=4, max_length=10)
- get_random_word()
