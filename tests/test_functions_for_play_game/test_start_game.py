import pytest
from hangman_code.functions_for_play_game.start_game import new_game, load_game
from hangman_code.functions_for_play_game.start_game import resume_game
from hangman_code.game import Game

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

def test_new_game ():

    #word = choose_word()
    # This shall call on the word_selection class to get a word
    #  and pass this into the game Class constructor
    # The output shall be returned to the user as an HTTP/HTTPS 
    # format via the convertor send_request function
    # The get_render function in templates will need to be called
    assert 1 == 2


def test_resume_game ():
    # This shall call on the from_dict function and pass data from 
    # persistance into the Game Class as the arguments
    # The output shall be returned to the user as an HTTP/HTTPS 
    # format via the convertor send_request function
    # It should flash up an error message to the user if there 
    # is no game to resume
    assert 1 == 2


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
