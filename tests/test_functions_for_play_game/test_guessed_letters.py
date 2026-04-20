import pytest
from hangman_code.functions_for_play_game.guessed_letters import used_letters_function
def test_used_letters_function():
    letter_list = ["X", "C", "L"]
    new_text = "U"
    result = used_letters_function(letter_list, new_text)
       #This will make a list of used letters
    assert result == ["x", "c", "l","u"] 
       #if condition returns true then nothing happens, if false then assertion error is raised
    print (result)
    return None

