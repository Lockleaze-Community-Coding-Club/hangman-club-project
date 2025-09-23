#This is a test to test the word_selection function
import inspect
import word_selection
import pytest

def test_format_string():
    """Check that the actual return value is a string at runtime."""
    result = word_selection("green")
    assert isinstance(result, str), "Expected word_selection() to return a string"


def test_return_annotation_is_str():
    """Check that the function is annotated to return a string."""
    sig = inspect.signature(word_selection)
    assert sig.return_annotation is str, 
    "Expected word_selection() return type annotation to be str"

def test_length():
     """Check that the function will return a certain length."""
     assert word_selection.length > 0
     assert word_selection.length < 46

def test_no_space():
    """Check that there is only one word supplied and there are no spaces"""
    with pytest.raises(ValueError):
        word_selection("John Doe")