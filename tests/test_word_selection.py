#This is a test to test the word_selection function
import pytest
from re import fullmatch
from hangman_code.word_selection import word_selection

def test_input_error():
    """Check that an error is raised if words.txt does not exist."""
    with pytest.raises(FileNotFoundError):
        word_selection.parse_words("notfound.txt")
    #Issue 28

def test_parse_words():
    """Check that the words.txt file is parsed as a list of words."""
    result = word_selection.parse_words("test_words.txt")
    expected = ["animal", "banana", "carrot", "donkey"]
    assert result == expected, f"Expected {expected}, but got {result}"
    # Issue 28

def test_choose_word():
    """Check that a single word is chosen from the list"""
    fake_list = ["red","yellow","pink","green"]
    result = word_selection.choose_word(fake_list)
    assert result in fake_list, f"Expected one of {fake_list}, but got {result}"
    #Issue 29

def test_choose_word2():
    """Check that an error is returned if the list contains no words"""
    fake_list = []  
    with pytest.raises(ValueError):
         word_selection.choose_word(fake_list)
    #Issue 29

def test_word_selection_randomness():
    results = {word_selection() for _ in range(100)}
    # Expect that more than one unique word was selected
    assert len(results) > 1, f"Word selection not random enough: {results}"
    #Issue 29


def test_format_string():
    """Check that the actual return \
        value is a string at runtime."""
    result = word_selection("green")
    assert isinstance(result, str)
    """Expected word_selection() to return a string"""

def test_length():
     assert len (word_selection('hello')) > 0
     assert len (word_selection('hello')) < 47

def test_no_space():
    """Check that there is only one word supplied and there are no spaces"""
    result = word_selection('hello')
    assert fullmatch(r"[A-Za-z]+", result), f"Invalid string: {result}"
