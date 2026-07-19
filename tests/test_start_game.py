import pytest
#from hangman_code.game import Game
from hangman_code.game import Game
from hangman_code.start_game import load_game




@pytest.fixture
def factory_data():
    
    def create_persistance():
        return {
                "player_name": "Ronald",
                "word": ["D", "O", "G"],
                "game_id": 42,
                "current_score": 52,
                "template": "Resume",
                "message": "The only way is up",
                "used_letters": ["A","B","C"],
                "game_status": 1,
                "accepted_letters": ["O", "G"],
                "word_progress": ["_", "O", "G"],
                "attempts_remaining": 2,
                "start_game_selection": 2
                }
    return create_persistance

def test_load_game_returns_a_game_object ():
    #given a player name
    player_name = "fred"
    result= load_game(player_name)
    assert result != None
    assert type(result) == Game

def test_load_game_returns_expected_game_attribute ():
    player_name = "Fred"
    result = load_game(player_name)
    assert "Fred" == result.player_name

def test_load_game_returns_game_status ():
# Check for any game status' which are IN_PLAY(1)
    player_name = "Fred"
    result = load_game(player_name)
    assert result.game_status in [Game.Game_status.NEW_GAME,
                                  Game.Game_status.IN_PLAY,
                                  Game.Game_status.WON,
                                  Game.Game_status.LOST]

def test_load_game_searches_game_status_in_persistance (factory_data, mocker):
# Check for any game status' which are IN_PLAY(1)
    player_name = "Fred"
    persistence = factory_data()

    mocker.patch(
        "hangman_code.start_game.read_and_find",
        return_value={
            "letter_found": False,
            "word_progress": ["_", "O", "G"],
            "message": "Bad luck you lemon!"
        },
        )
    result = load_game(player_name)
    assert result.game_status in [Game.Game_status.NEW_GAME,
                                  Game.Game_status.IN_PLAY,
                                  Game.Game_status.WON,
                                  Game.Game_status.LOST]
    print(Game.Game_status)
