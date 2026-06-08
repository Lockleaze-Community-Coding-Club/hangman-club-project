import pytest
from hangman_code.play_game_functions import play_game

@pytest.fixture
def factory_data():
    
    def create_game():
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
    return create_game

def test_play_game_returns_a_dict(factory_data):
    data = factory_data()
    letter = "E"
    result = play_game(data, letter)
    assert isinstance(result, dict)
    
def test_play_game_continues_if_attempts_remaining_greaterthanzero(mocker,
                                                                   factory_data
                                                                   ):
        data = factory_data()
        print(data["used_letters"])

        mocker.patch(
        "hangman_code.play_game_functions.make_guess",
        return_value={
            "letter_found": False,
            "word_progress": ["_", "O", "G"],
            "message": "Bad luck you lemon!"
        },
        )

        mocker.patch(
                "hangman_code.play_game_functions.remaining_attempts_function",
                return_value=1,
        )

        mocker.patch(
                "hangman_code.play_game_functions.current_game_status",
                return_value=1,
        )

        mocker.patch(
        "hangman_code.play_game_functions.update_score_function",
        return_value=51,
        )

        letter = "E"
        data = factory_data()
        original_attempts_remaining = data["attempts_remaining"]

        original_used_letters = data["used_letters"]
        print(original_used_letters)
        result = play_game(data, letter)
        print(result["used_letters"])        
        assert result["attempts_remaining"] == original_attempts_remaining -1
        assert result["message"]!="The only way is up"
        assert result["current_score"]!=52
        assert result["game_status"]==3#artificially changed
        assert result["word_progress"]==["_","O","G"]
        assert result["used_letters"]==original_used_letters
        print(original_used_letters)

def test_play_game_finishes_if_game_is_won(mocker,factory_data):
        data = factory_data()
        mocker.patch(
        "hangman_code.play_game_functions.make_guess",
        return_value={
            "letter_found": True,
            "word_progress": ["D", "O", "G"],
            "message": "You won!"
        },
        )

        mocker.patch(
                "hangman_code.play_game_functions.remaining_attempts_function",
                return_value=2,
        )

        mocker.patch(
                "hangman_code.play_game_functions.current_game_status",
                return_value=2,
        )

        mocker.patch(
        "hangman_code.play_game_functions.is_won",
        return_value={"result": "won"},
        )

        letter = "D"
        result = play_game(data, letter)
        assert result == {"result": "won"}

def test_play_game_finishes_if_game_is_lost(mocker, factory_data):
        data = factory_data()
        mocker.patch(
        "hangman_code.play_game_functions.make_guess",

        return_value={
            "letter_found": False,
            "word_progress": ["_", "O", "G"],
            "message": "You Lost!"
        },
        )

        mocker.patch(
                "hangman_code.play_game_functions.remaining_attempts_function",
                return_value=0,
        )

        mocker.patch(
                "hangman_code.play_game_functions.current_game_status",
                return_value=3,
        )

        mocker.patch(
        "hangman_code.play_game_functions.is_lost",
        return_value={"result": "lost"},
        )

        letter = "F"
        result = play_game(data, letter)
        assert result == {"result": "lost"}