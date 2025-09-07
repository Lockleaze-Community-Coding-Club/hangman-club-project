
from select_word import select_word

word_selected = select_word()
winner = True

if winner:
    print('You are correct todays word was: ', word_selected)
else:
    print('Loser')


# To run the hangman project from bash use this command:
# python code/lockleaze_hangman.py

# it will look like this
# Rick@LAPTOP-IK2NAICQ MINGW64 
# /c/Lockleaze Hangman/hangman-club-project (master)
# $ python code/lockleaze_hangman.py
# empt string -- this needs to contain the word 
# chosen and the masked version to display on the screen