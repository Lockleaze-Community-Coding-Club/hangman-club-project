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
    expected = ["animal", "banana", "carrot"]
    assert result == expected, f"Expected {expected}, but got {result}"
    # Issue 28

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
