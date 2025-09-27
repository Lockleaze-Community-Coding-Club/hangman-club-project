#This is a test to test the word_selection function
import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), \
                             "../code"))
)

from word_selection import word_selection


def test_format_string():
    """Check that the actual return \
        value is a string at runtime."""
    result = word_selection("green")
    assert isinstance(result, str)
    """Expected word_selection() to return a string"""


def test_return_annotation_is_str():
    """Check that the function is annotated to return a string."""
    assert type (word_selection('hello')) == \
        type('example of a string')
    """Expected word_selection() return type annotation to be str"""

def test_length():
     """Check that the function will return a certain length."""
     assert len (word_selection('hello')) > 0
     assert len (word_selection('hello')) < 47

def test_no_space():
    from re import fullmatch
    """Check that there is only one word supplied \
        and there are no spaces"""
    assert fullmatch(r"[A-Za-z]+", word_selection('hello')), \
          f"String contains non-letter characters: "