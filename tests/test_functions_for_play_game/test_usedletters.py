import pytest
from hangman_code.functions_for_play_game.guessed_letters import used_letters_function

def test_used_letters_function():
    used_letters = ["X", "C", "L"]
    letter = "U"
    result = used_letters_function(used_letters, letter)
       #This will make a list of used letters
    assert result == ["x", "c", "l","u"] 
       #if condition returns true then nothing happens, 
       # if false then assertion error is raised

