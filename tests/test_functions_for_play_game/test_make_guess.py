import pytest
from hangman_code.functions_for_play_game.make_guess import make_guess
from hangman_code.functions_for_play_game.make_guess import remaining_attempts_function

def test_make_guess_fills_all_matching_letters():
    """Test to check that a word with two or more of the same letter fills in
      the guessed word multiple times"""
    test_letter = "A"
    test_result = make_guess(
        test_letter,
        ["A", "B", "A", "C", "U", "S"],
        ["_", "_", "_", "_", "_", "_"],
    )
    assert test_result["letter_found"] is True
    assert test_result["word_progress"] == ["A", "_", "A", "_", "_", "_"]

def test_make_guess_wrong_letter_guess():
    """Test to check that the function behaves as expected when a wrong letter
    is inserted"""
    test_letter = "E"
    test_result = make_guess(
        test_letter,
        ["A", "B", "A", "C", "U", "S"],
        ["_", "_", "_", "_", "_", "_"],
    )
    assert test_result["letter_found"] is False
    assert test_result["word_progress"] == ["_", "_", "_", "_", "_", "_"]

def test_make_guess_different_list_lengths():
    """Test to check that the function behaves as expected when the game is
    initialised (i.e. the guessed word is converted into a list of the correct
    length)"""
    test_letter = "E"
    with pytest.raises(ValueError):
        make_guess(
        test_letter,
        ["A", "B", "A", "C", "U", "S"],
        [""])

def test_remaining_attempts_letter_not_found():
    attempts_remaining = 8
    letter_found = False
    expected = 7
    result = remaining_attempts_function(attempts_remaining,letter_found)
    msg = f"Expected {expected}\n" f"but got {result}"
    assert result == expected, msg

def test_remaining_attempts_letter_found():
    attempts_remaining = 8
    letter_found = True
    expected = 8
    result = remaining_attempts_function(attempts_remaining,letter_found)
    msg = f"Expected {expected}\n" f"but got {result}"
    assert result == expected, msg

def test_remaining_attempts_is_1_and_letter_not_found():
    attempts_remaining = 1
    letter_found = False
    expected = 0
    result = remaining_attempts_function(attempts_remaining,letter_found)
    msg = f"Expected {expected}\n" f"but got {result}"
    assert result == expected, msg

def test_remaining_attempts_is_0_and_letter_not_found():
    attempts_remaining = 0
    letter_found = False
    expected = ValueError
    result = remaining_attempts_function(attempts_remaining,letter_found)
    msg = f"Expected {expected}\n" f"but got {result}"
    assert result == expected, msg


#def test_update_score_function():
       #This function will update the score
       #return None