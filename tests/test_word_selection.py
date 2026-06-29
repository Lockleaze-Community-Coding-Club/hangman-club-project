#This is a test to test the word_selection function
import pytest
from hangman_code.word_selection import choose_word
from hangman_code.word_selection import parse_words
#from hangman_code.functions_for_play_game.data_handling import to_dict

@pytest.fixture
def listofwords():
    expected = {
        "Apple",
        "Banana",
        "CARROT",
        "SticK",
        "Banana",
        "orange",
        "1sha",
        "Banana",
        "Dog",
        "Cat",
        "Thisisaverylongwordnotrecognisable",
        "a",
        "it",
        "shit"
        }
    return expected

def test_input_error():
    """Check that an error is raised if words.txt does not exist."""
    with pytest.raises(FileNotFoundError):
        parse_words("words.txt")

def test_parse_words_returns_list_of_words():
    """Check that the words.txt file is parsed as a list of words."""
    result = parse_words("tests/test_words.txt")
    expected = ["animal", "banana", "carrot", "donkey"]
    assert result == expected, f"Expected {expected}, but got {result}"

def test_single_word_chosen():
    fake_list = ["red", "yellow", "pink", "green"]

    chosen_word, remaining = choose_word(fake_list.copy())

    assert len(remaining) == 3


def test_choose_word_error_returned_if_no_words_in_list():
    """Check that an error is returned if the list contains no words"""
    fake_list = []  
    with pytest.raises(ValueError):
         choose_word(fake_list)


def test_word_is_removed():
    words = ["red", "yellow", "pink", "green"]

    word, remaining = choose_word(words.copy())

    assert word not in remaining
    assert len(remaining) == 3

def test_format_returned_is_tuple():
    """Check that the actual return \
        value is a list at runtime."""
    result = choose_word(["green","red"])
    assert isinstance(result, tuple)
    """Expected word_selection() to return a tuple"""

def test_word_length_is_reasonable():
    words = parse_words("tests/test_words.txt")

    assert len(words) > 0
    assert all(len(word) < 47 for word in words)


from re import fullmatch

def test_no_white_space_returned():
    """Check that chosen word has no whitespace"""

    chosen_word, remaining = choose_word(["hello", "Dog"])

    word_as_string = "".join(chosen_word)

    assert fullmatch(r"[A-Za-z]+", word_as_string), f"Invalid string: {word_as_string}"
    assert " " not in word_as_string

def test_choose_word_returns_lowercase_letters():
    words = ["DOG"]

    chosen_word, remaining = choose_word(words)

    assert all(c.islower() for c in chosen_word)
