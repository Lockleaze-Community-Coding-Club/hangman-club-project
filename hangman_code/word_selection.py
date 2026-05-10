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
                chosen_word = chosen_word.strip().lower()


                chosen_word = [char for char in chosen_word]

                return (chosen_word, available_words_list)


#By others: - ....now maybe not required.  OR TBC:

 
 




