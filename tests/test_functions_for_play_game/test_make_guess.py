import pytest
from hangman_code.functions_for_play_game.make_guess import Make_guess
from hangman_code.functions_for_play_game.make_guess import remaining_attempts_function

def test_make_guess_fills_all_matching_letters():
    """Test to check that a word with two or more of the same letter fills in
      the guessed word multiple times"""
    test_letter = "A"
    test_result = Make_guess(
        test_letter,
        ["A", "B", "A", "C", "U", "S"],
        ["_", "_", "_", "_", "_", "_"],
    )
    assert test_result["success"] is True
    assert test_result["word_progress"] == ["A", "_", "A", "_", "_", "_"]

def test_make_guess_wrong_letter_guess():
    """Test to check that the function behaves as expected when a wrong letter
    is inserted"""
    test_letter = "E"
    test_result = Make_guess(
        test_letter,
        ["A", "B", "A", "C", "U", "S"],
        ["_", "_", "_", "_", "_", "_"],
    )
    assert test_result["success"] is False
    assert test_result["word_progress"] == ["_", "_", "_", "_", "_", "_"]

def test_make_guess_different_list_lengths():
    """Test to check that the function behaves as expected when the game is
    initialised (i.e. the guessed word is converted into a list of the correct
    length)"""
    test_letter = "E"
    with pytest.raises(ValueError):
        Make_guess(
        test_letter,
        ["A", "B", "A", "C", "U", "S"],
        [""])

def test_remaining_attempts():
    test_attempts = [11, 10, 1, 0, -1]
    test_result = [20, 20, 20, 20, 20]
    expected = [10, 9, 0, ValueError, ValueError]
    for i, x in enumerate(test_attempts):
        try:
            result = remaining_attempts_function(x)
        except Exception as e:
            result = type(e)
        test_result[i] = result
    msg = f"Expected {expected}\n" f"but got {test_result}"
    assert test_result == expected, msg

#def test_update_score_function():
       #This function will update the score
       #return None