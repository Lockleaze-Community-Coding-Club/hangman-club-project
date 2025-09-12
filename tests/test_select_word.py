import sys
sys.path.append ('./code/')
from select_word import select_word

def test_select_word_returns_tupel():
    type_returned_by_select_word = type(select_word())
    test_tuple = (1,1)
    type_of_test_tupel = type (test_tuple)
    assert type_returned_by_select_word == type_of_test_tupel

def test_select_word_returns_strings():  
    word_selected = select_word()
    first_element = word_selected[0]
    second_element = word_selected[1]
    test_string = 'test'
    type_of_test_string = type (test_string)
    assert type (first_element) == type_of_test_string
    assert type (second_element) == type_of_test_string
    
def test_word_same_length_as_template():
    word_selected = select_word()
    assert len (result[0]) == len(result[1])



