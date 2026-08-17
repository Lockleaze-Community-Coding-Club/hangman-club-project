import pytest
import json
from hangman_code.game import Game
from hangman_code.functions_for_play_game.data_handling import turn_game_into_data
from hangman_code.functions_for_play_game.data_handling import turn_dict_into_game
from hangman_code.functions_for_play_game.data_handling import to_dict
from hangman_code.functions_for_play_game.data_handling import from_dict
from hangman_code.functions_for_play_game.data_handling import read_and_find


@pytest.fixture
def factory_data():
    
    def create_game():
        newgame = Game()
        newgame.set_player_name("Ronald")
        newgame.set_word(["D", "O", "G"])
        newgame.set_game_id(42)
        newgame.set_current_score(52)
        newgame.set_template("Resume")
        newgame.set_message("The only way is up")
        newgame.set_used_letters("A")
        newgame.set_used_letters("B")
        newgame.set_used_letters("C")
        newgame.set_accepted_letters("O")
        newgame.set_accepted_letters("G")        
        newgame.set_word_progress(["_","O","G"])
        newgame.set_attempts_remaining(2)
        
        return newgame 

    return create_game

@pytest.fixture
def temp_path(tmp_path):
    def create_file():
        file_path = tmp_path / "test.json"
        return file_path
    return create_file 

@pytest.fixture
def from_dict_fake_data():
    def create_dict():
        expected = {
                "player_name": "Ronald",
                "word": ["D", "O", "G"],
                "game_id": 42,
                "current_score": 52,
                "template": "Resume",
                "message": "The only way is up",
                "used_letters": ["A", "B", "C"],
                "game_status": 1,
                "accepted_letters": ["O", "G"],
                "attempts_remaining": 2,
                "word_progress": ["_","O","G"],

                }
        return expected
    return create_dict

@pytest.fixture
def temp_path_2(tmp_path):
    def create_file():
        file_path = tmp_path / "test2.json"
        return file_path
    return create_file

@pytest.fixture
def from_dict_fake_data_b():
    def create_dict():
        expected = {
                "player_name": "Ronald",
                "word": ["D", "O", "G"],
                "game_id": 42,
                "current_score": 52,
                "template": "Resume",
                "message": "The only way is up",
                "used_letters": ["A", "B", "C"],
                "game_status": 1,
                "accepted_letters": ["O", "G"],
                # missing attempts_remaining
                "word_progress": ["_","O","G"],

                }
        return expected
    return create_dict

def test_turn_game_object_into_dict_sunny_day(factory_data):
    input_data = factory_data()
    print(type(input_data))
    result = turn_game_into_data(input_data)
    assert type(result) is dict

def test_turn_game_object_into_dict_None_returns_error():
    input_data = None
    with pytest.raises(ValueError):
            turn_game_into_data(input_data)

def test_turn_game_object_into_dict_not_game_returns_error():
    input_data = 1
    with pytest.raises(ValueError):
            turn_game_into_data(input_data)

def test_turn_dict_object_into_Game_sunny_day(from_dict_fake_data):
    input_data = from_dict_fake_data()
    print(type(input_data))
    result = turn_dict_into_game(input_data)
    assert type(result) is Game

def test_turn_dict_object_into_Game_None_returns_error():
    input_data = None
    with pytest.raises(ValueError):
            turn_dict_into_game(input_data)

def test_turn_dict_into_Game_not_dict_returns_error():
    input_data = 1
    with pytest.raises(ValueError):
            turn_game_into_data(input_data)

def test_turn_dict_into_Game_returns_error_if_keys_are_missing(from_dict_fake_data_b):
# Number of attempts remaining has been deleted
    fake_game = from_dict_fake_data_b()
    with pytest.raises(ValueError):
        turn_game_into_data(fake_game)


def test_to_dict_raises_error_if_directory_missing(factory_data):
    location = "missing_dir/file.json"
    data = factory_data()

    with pytest.raises(FileNotFoundError):
        to_dict(data, location)

def test_to_dict_fails_when_file_unwritable(factory_data, temp_path):
    input_data = factory_data()
    file_path = temp_path()
    file_path.touch()
    file_path.chmod(0o400)  # read-only

    with pytest.raises(PermissionError):
        to_dict(input_data, file_path)

def test_to_dict_basic_functionality(temp_path, factory_data):
    input_data = factory_data()
    file_path = temp_path()
    to_dict(input_data, file_path)
    with open(file_path) as f:
        data = json.load(f)
    print(type(data))
    assert isinstance(data,dict)

def test_to_dict_stores_correct_data(temp_path, factory_data):
    input_data = factory_data()
    file_path = temp_path()
    to_dict(input_data, file_path)
    with open(file_path) as f:
        data = json.load(f)
    print(type(data))
    print(data)
    data = Game(**data)
    data_test = Game.get_message(data)
    input_data_test = Game.get_message(input_data)
    data_test_two = Game.get_game_id(data)
    input_test_two = Game.get_game_id(input_data)
    assert isinstance(data,Game)
    assert input_data_test == data_test
    assert data_test_two == input_test_two

def test_to_dict_returns_error_if_wrong_data_input(temp_path):
    file_path = temp_path()
    input_data = 3
    with pytest.raises(ValueError):
        to_dict(input_data, file_path)

def test_to_dict_allows_overwrites(temp_path, factory_data):
    file_path = temp_path()
    input_data = factory_data()
    to_dict(input_data, file_path)
    input_data.set_message("Made up test message")
    to_dict(input_data, file_path)
    with open(file_path) as f:
        saved = json.load(f)
    assert saved["message"] == "Made up test message"


def test_to_dict_persists_values_which_are_not_overwritten(temp_path, factory_data):
    file_path = temp_path()
    input_data = factory_data()
    to_dict(input_data, file_path)
    input_data.set_message("Made up test message")
    to_dict(input_data, file_path)
    with open(file_path) as f:
        saved = json.load(f)
    assert saved["game_id"] == 42


def test_read_and_find_returns_false_if_player_name_not_present(temp_path, factory_data):
    file_path = temp_path()
    input_data = factory_data()
    to_dict(input_data, file_path)
    result = read_and_find(file_path, "Fred")
    expected = False
    assert result == expected

def test_read_and_find_returns_true_if_player_name_is_present(temp_path, factory_data):
    file_path = temp_path()
    input_data = factory_data()
    to_dict(input_data, file_path)
    result = read_and_find(file_path, "Ronald")
    expected = True
    assert result == expected

def test_read_and_find_returns_true_if_game_status_is_in_play(temp_path, factory_data):
    file_path = temp_path()
    input_data = factory_data()
    input_data.set_game_status(1)
    to_dict(input_data, file_path)
    result = read_and_find(file_path, "Ronald")
    expected = True
    assert result == expected

def test_read_and_find_returns_false_if_game_status_is_not_in_play(temp_path, factory_data):
    file_path = temp_path()
    input_data = factory_data()
    to_dict(input_data, file_path)
    result = read_and_find(file_path, "Ronald")
    expected = False
    assert result == expected

def test_read_and_find_returns_false_if_game_status_is_in_play_player_name_not_match(temp_path, factory_data):
    file_path = temp_path()
    input_data = factory_data()
    input_data.set_game_status(1)
    to_dict(input_data, file_path)
    result = read_and_find(file_path, "Fred")
    expected = False
    assert result == expected

def test_read_and_find_sunny_day(temp_path, factory_data):
    file_path = temp_path()
    input_data = factory_data()
    input_data.set_game_status(1)
    to_dict(input_data, file_path)
    result = read_and_find(file_path, "Ronald")
    expected = False
    assert result == expected

def test_check_json_file_is_found_for_from_dict():
#Setup test that the expected test json file is present
    result = 1
    try:
        f = open("persistence.json")
    except ValueError:
        result = 2
    assert result == 1
    f.close()

def test_from_dict_basic_functionality(temp_path_2, factory_data):
#Test that data is returned from the persistence file and is correct
    json_file = temp_path_2()
    fake_game = factory_data()
    to_dict(fake_game, json_file)
    result = from_dict(json_file,"Ronald")
    expected = "Ronald"
    assert result.get_player_name() == expected
    expected_id = 42
    assert result.get_game_id() == expected_id

def test_from_dict_returns_error_if_keys_are_missing(temp_path_2, from_dict_fake_data_b):
# Number of attempts remaining has been deleted
    json_file = temp_path_2()
    fake_game = from_dict_fake_data_b()
    with open(json_file, "w") as file:
        json.dump(fake_game, file)
    with pytest.raises(KeyError):
        from_dict(json_file, "Ronald")

def test_from_dict_raises_error_for_empty_file(temp_path):
    file_path = temp_path()
    file_path.touch()  # create empty file

    with pytest.raises(ValueError):
        from_dict(file_path, "Ronald")

def test_from_dict_r(temp_path, factory_data):
    input_data = factory_data()
    file_path = temp_path()
    to_dict(input_data, file_path)
    result = from_dict(file_path, "Ronald")
    assert result.game_id == input_data.game_id

def test_to_dict_from_dict_round_trip(temp_path, factory_data):
    input_data = factory_data()
    file_path = temp_path()
    to_dict(input_data, file_path)
    result = from_dict(file_path, "Ronald")
    assert result.game_id == input_data.game_id




