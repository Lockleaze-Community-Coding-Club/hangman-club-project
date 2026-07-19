import pytest
from hangman_code.game import Game
from hangman_code.start_game import (load_game,
                                     new_game,
                                     save_available_words)

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

@pytest.fixture
def factory_words():
    def create_available_words_list():
        return [
                "Apple",
                "Banana",
                "CARROT",
                "SticK",
                "Banana",
                "orange",
                "isha",
                "Banana",
                "Dog",
                "Cat",
                "Thisisaverylongwordnotrecognisable",
                "a",
                "it",
                "shit"
        ]
    return create_available_words_list

def test_load_game_returns_a_game_object (factory_words):
    #given a player name
    words_list = factory_words()
    player_name = "fred"
    result= load_game(player_name, words_list)
    assert result is not None
    assert type(result) is Game

def test_load_game_returns_expected_game_attribute ():
    player_name = "Fred"
    result = load_game(player_name)
    assert "Fred" is result.player_name

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

def test_new_game_returns_a_game_object (factory_words):
    #given a player name
    player_name = "fred"
    words_list = factory_words()
    result= new_game(player_name, words_list)
    assert result is not None
    assert type(result) is Game

def test_new_game_gets_a_new_word_mock_word_selection (mocker,factory_words):
    words_list = factory_words()
    virgin_game = Game()
    mocker.patch(
        "hangman_code.start_game.choose_word",
        return_value=(
                ["a", "p", "p", "l", "e"],
                ["banana", "orange"]
        )
        )
    previous_word = virgin_game.get_word()
    player_name = "fred"
    result= new_game(player_name,words_list)
    assert result.word is not previous_word

def test_new_game_gets_a_new_word_real_word_selection (factory_words):
    words_list = factory_words()
    virgin_game = Game()
    previous_word = virgin_game.get_word()
    player_name = "fred"
    result= new_game(player_name,words_list)
    assert result.word is not previous_word

def test_new_game_recieves_empty_word_list_and_still_works():
    words_list = []
    virgin_game = Game()
    previous_word = virgin_game.get_word()
    player_name = "fred"
    result= new_game(player_name,words_list)
    assert result.word is not previous_word

def test_new_game_saves_updated_word_list(mocker):

    mocker.patch(
        "hangman_code.start_game.choose_word",
        return_value=(
            ["a", "p", "p", "l", "e"],
            ["banana", "orange"]
        )
    )

    mock_save = mocker.patch(
        "hangman_code.start_game.save_available_words"
    )

    new_game("fred", ["apple", "banana", "orange"])

    mock_save.assert_called_once_with(
        ["banana", "orange"]
    )

def test_new_game_when_choose_word_fails_should_get_error(mocker,
                                                          factory_words):
    words_list = factory_words()
    mocker.patch(
                "hangman_code.start_game.choose_word",
                return_value=[]
        )
    player_name = "fred"
    with pytest.raises(ValueError):
        new_game(player_name,words_list)

def test_save_available_words_calls_to_dict(mocker):

    words = ["apple", "banana", "orange"]

    mock_to_dict = mocker.patch(
        "hangman_code.start_game.to_dict"
    )

    save_available_words(words)

    mock_to_dict.assert_called_once_with(
        words,
        "available_words_list.json"
    )

def test_new_game_save_fails(mocker):

    mocker.patch(
        "hangman_code.start_game.choose_word",
        return_value=(["a"], [])
    )

    mocker.patch(
        "hangman_code.start_game.save_available_words",
        side_effect=OSError("Disk full")
    )

    with pytest.raises(OSError, match="Disk full"):
        new_game("Fred", ["apple"])