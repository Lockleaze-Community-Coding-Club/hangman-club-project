#This is a test to test the word_selection function
import pytest
from re import fullmatch
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
    """Check that a single word is chosen from the list"""
    ## choose_words also needs to take in where the persistence file is
    fake_list = ["red","yellow","pink","green"]
    result = choose_word(fake_list)
    assert result in fake_list, f"Expected one of {fake_list} but got {result}"

def test_choose_word_error_returned_if_no_words_in_list():
    """Check that an error is returned if the list contains no words"""
    fake_list = []  
    with pytest.raises(ValueError):
         choose_word(fake_list)

def test_word_selection_non_repitition(listofwords):
    
    results = {choose_word(listofwords) for i in range(100)}
    # Expect that more than one unique word was selected
    msg = f"Word selection not random enough: {results}"
    assert len(results) > 1, msg

def test_format_returned_is_list():
    """Check that the actual return \
        value is a list at runtime."""
    result = choose_word("green")
    assert isinstance(result, list)
    """Expected word_selection() to return a list"""

def test_word_length_is_reasonable():
    words = parse_words("tests/test_words.txt")

    assert len(words) > 0
    assert all(len(word) < 47 for word in words)


def test_no_white_space_returned():
    """Check that there is only one word supplied and there are no spaces"""
    result = choose_word(["hello","Dog"])
    assert fullmatch(r"[A-Za-z]+", result), f"Invalid string: {result}"

def test_choose_word_returns_lowercase_letters():
        word = "DOG"
        expected = ["d","o","g"]
        result = choose_word([word])
        assert result == expected
