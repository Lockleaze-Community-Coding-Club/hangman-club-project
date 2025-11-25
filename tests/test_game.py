import pytest
#from re import fullmatch
from hangman_code.game import Game

def test_make_guess():
        """Test to check that the user has inputted a letter 
        correctly and that
        the same letter guess cannot be repeated"""
        test_letter = ["E", "z", "e", 1, 10000,"!", "aa", "Be", "E"]
        test_result =[]
        expected = ["E","Z", "E", ValueError, ValueError, ValueError, 
                    ValueError, ValueError, ValueError]
        for x in test_letter:
            result = Game.make_guess(x)
            test_result.append(result)
        msg = (
            f"Expected {expected}, \n"
            f"but got {result}"
        )
        assert test_result == expected, msg

def test_display_word():
        """Test to check that the word and the blanks are 
        correctly outputted for display to the player"""
        test_words = ["apple", "ra__i_", "Lockleaze_is_great", 
                      "I like wine", "Oopsie123", "1__A__3"]
        test_result = []
        expected = ["APPLE",
                    "RA__I_", 
                    ValueError, 
                    ValueError, 
                    ValueError, 
                    ValueError]
        for x in test_words:
            result = Game.display_word(x)
            test_result.append(result)
        msg = (
            f"Expected {expected}, \n"
            f"but got {result}"
        )
        assert test_result == expected, msg

def test_remaining_attempts():
        test_attempts = [11,10,1,0,-1]
        test_result = []
        expected = [10,9,0,-1,-2]
        for x in test_attempts:
                result = Game.remaining_attempts(x)
                test_result.append(result)
        msg = (f"Expected {expected}\n"
               f"but got {result}")
        assert test_result == expected, msg

def test_to_dict_basic_structure():
        game = Game(word = "lockleaze")
        data = game.to_dict()

        # Ensure correct keys
        assert set(data.keys()) == {
                "word", 
                "guessed_letters",
                "attempts_left", 
                "wrong_guesses"}

def test_to_dict_values_are_correct():
        game = Game(word="community", guessed_letters={"p", "x"}, 
                        attempts_left=5)
        data = game.to_dict()

        assert data["word"] == "community"
        assert set(data["guessed_letters"]) == {"p", "x"}  
        # converted from set → list
        assert data["attempts_left"] == 5

def test_to_dict_returns_json_safe_types():
        game = Game(word="club", guessed_letters={"p", "y"})
        data = game.to_dict()

        # Word must be a string
        assert isinstance(data["word"], str)

        # guessed_letters must be a list 
        # (because JSON can't store sets)
        assert isinstance(data["guessed_letters"], list)

        # attempts_left must be an int
        assert isinstance(data["attempts_left"], int)

def test_to_dict_does_not_expose_internal_state():
        game = Game(word="guinness")
        data = game.to_dict()

        # Ensure no private/internal attributes leak
        for key in data.keys():
                assert not key.startswith("_")

def test_from_dict_basic_structure():
        """Test the reconstruction of the game"""
        data = {
                "word": "lockleaze",
                "guessed_letters": ["l", "e"],
                "attempts_left": 7,
                "wrong_guesses": ["x"]
        }

        game = Game.from_dict(data)

        assert isinstance(game, Game)
        assert game.word == "lockleaze"
        assert game.guessed_letters == {"l", "e"}  # list → set
        assert game.attempts_left == 7
        assert game.wrong_guesses == {"x"}         # list → set

def test_from_dict_values_are_correct():
        """Test that the values are reconstructed correctly"""
        data = {
                "word": "community",
                "guessed_letters": ["p", "x"],
                "attempts_left": 5,
                "wrong_guesses": []
        }

        game = Game.from_dict(data)

        assert game.word == "community"
        assert game.guessed_letters == {"p", "x"}
        assert game.attempts_left == 5

def test_from_dict_missing_keys_raises_error():
        """Do a test to check for missing keys"""
        data = {"word": "python"}  
        # missing guessed_letters, attempts_left, wrong_guesses

        with pytest.raises(KeyError):
                Game.from_dict(data)

def test_from_dict_wrong_types_raise_error():
        """Do a check that the data is in the right
        format and raises an error if not"""
        data = {
                "word": 123,                         # should be str
                "guessed_letters": "not a list",     # should be list
                "attempts_left": "five",             # should be int
                "wrong_guesses": {}
        }

        with pytest.raises(TypeError):
                Game.from_dict(data)

def test_from_dict_none_raises_error():
        """Check what happens if a null value is returned"""
        with pytest.raises(TypeError):
                Game.from_dict(None)

def test_from_dict_rejects_empty_word():
        """Cannot play hangman with an empty word"""
        data = {
                "word": "",
                "guessed_letters": [],
                "attempts_left": 6,
                "wrong_guesses": []
        }

        with pytest.raises(ValueError):
                Game.from_dict(data)

def test_from_dict_invalid_guessed_letters():
        """Check that an error is raised if invalid values are entered"""
        data = {
                "word": "python",
                "guessed_letters": [1, 2, 3],
                "attempts_left": 5,
                "wrong_guesses": []
        }

        with pytest.raises(ValueError):
                Game.from_dict(data)

def test_from_dict_negative_attempts_rejected():
        """Check that the number of remaining attempts cannot be negative"""
        data = {
                "word": "python",
                "guessed_letters": [],
                "attempts_left": -1,
                "wrong_guesses": []
        }
        with pytest.raises(ValueError):
                Game.from_dict(data)

def test_from_dict_ignores_unknown_keys():
        """Check that unknown extra keys are ignored"""
        data = {
                "word": "python",
                "guessed_letters": [],
                "attempts_left": 5,
                "wrong_guesses": [],
                "cheat_mode": True
        }

        game = Game.from_dict(data)
        assert not hasattr(game, "cheat_mode")

