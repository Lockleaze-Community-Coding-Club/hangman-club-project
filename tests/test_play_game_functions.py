import pytest
from hangman_code.play_game_functions import play_game
from hangman_code.game import Game

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

def test_play_game_returns_a_Game_object(factory_data):
    data = factory_data()
    letter = "E"
    result = play_game(data, letter)
    assert isinstance(result, Game)
    
def test_play_game_continues_if_attempts_remaining_greaterthanzero(mocker,
                                                                   factory_data
                                                                   ):
        data = factory_data()

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
        original_attempts_remaining = Game.get_attempts_remaining(data)

        original_used_letters = Game.get_used_letters(data)
        
        result = play_game(data, letter)

        assert Game.get_attempts_remaining(result) == original_attempts_remaining -1
        assert Game.get_message(result)!="The only way is up"
        assert Game.get_current_score(result)!=52
        assert Game.get_game_status(result)==1
        assert Game.get_word_progress(result)==["_","O","G"]
        assert Game.get_used_letters(result)==original_used_letters

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