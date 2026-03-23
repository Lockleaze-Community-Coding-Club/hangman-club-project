
## ALSO NEEDS TO GET THE LIST OF USED WORDS FROM PERSISTENCE

#from persistence import Persistence

import random

#By JF:


def parse_words(words_file):
        words_list = []
        with open(words_file) as f:
                for x in f:
                        formatted_word = x.strip().lower()
                        words_list.append(formatted_word)
        return words_list


def choose_word(available_words_list):
        number_of_words_in_list = len(available_words_list)
        chosen_word_position = random.randint(1, number_of_words_in_list) - 1
        chosen_word = available_words_list[chosen_word_position]

        available_words_list.remove(chosen_word)

        return (chosen_word, available_words_list)


#Examples of how to use the above:
# In main program:

# initial_words_list = parse_words("C:/Users/john_/Documents/Coding/My Python/Hangman/hangman_words_files/words.txt")
# print(initial_words_list)

# unused_words_list = initial_words_list

# while len(unused_words_list)>0:

#     From_choose_word = choose_word(unused_words_list)
#     word_to_guess = From_choose_word[0]
#     unused_words_list = From_choose_word[1]

#     print(word_to_guess)
#     print("- is the chosen word.  The remaining unused words are:")
#     print(unused_words_list)

# print("End of session, as all words used.")