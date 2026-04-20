import pytest
from hangman_code.play_game_functions import play_game

@pytest.fixture
def data():
    return {
        "player_name": "Ronald",
        "word": ["D", "O", "G"],
        "game_id": 42,
        "current_score": 52,
        "template": "Resume",
        "message": "The only way is up",
        "used_letters": ["A", "B", "C"],
        "current_game_status": 1,
        "accepted_letters": ["O", "G"],
        "word_progress": ["_", "O", "G"],
        "attempts_remaining": 2,
        "start_game_selection": 2
              }



def test_play_game_returns_a_dict(data):
    letter = "A"
    result = play_game(data, letter)
    assert isinstance(result, dict)
    

