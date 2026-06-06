import pytest
from hangman_code.game import Game

def test_can_create_game_object():
    a = Game()
    assert 1==1

def test_can_initiate_game_with_integer_score():
    game = Game(score=10)
    assert game.score == 10

def test_cannot_initiate_game_with_text_score():
    with pytest.raises(ValueError, match="score must be an integer") as exc_info:
        Game(score="TEXT") 
    print(exc_info.value)

def test_initiate_game_with_none_gives_default_score():
    test_game = Game(score=None)
    assert test_game.score == 0
    assert isinstance (test_game.score, int)