import pytest
from hangman_code.game import Game

@pytest.fixture

def factory_data():
    
    def create_game():
        game = Game()
        return game
    return create_game

def test_get_word_returns_formatted_list(factory_data):
       game = factory_data()
       result = game.get_word()
       assert isinstance(result,list)
       assert result is not None
       res = any(x.isspace()for x in result)
       assert res is False

def test_set_word_returns_formatted_list(factory_data):
       game = factory_data()
       old_word = list(game.word)
       result = game.set_word(["L","a","z","y"])       
       assert isinstance(result,list)
       assert result is not old_word
       assert result is not None
       assert not any(
        c.isspace()
        for letter in result
        for c in letter
                )
       assert any(
       c.islower()
       for letter in result
       for c in letter
               )
       with pytest.raises(TypeError):
                game.set_word(30)

def test_get_game_id_returns_int(factory_data):
       game = factory_data()
       result = game.get_game_id()
       assert isinstance(result,int)
       assert result >= 0
     
def test_set_game_id_returns_int(factory_data):
        game = factory_data()
        old_id = game.game_id
        result = game.set_game_id(30)
        assert isinstance(result,int)
        assert result > 0
        assert result != old_id
        with pytest.raises(TypeError):
                game.set_game_id("thirty")  

def test_get_current_score_returns_int(factory_data):
       game = factory_data()
       result = game.get_current_score()
       assert isinstance(result,int)
       assert result >= 0

def test_set_current_score_returns_int(factory_data):
        game = factory_data()
        old_score = game.current_score
        result = game.set_current_score(10)
        assert isinstance(result,int)
        assert result > 0
        assert result != old_score
        with pytest.raises(TypeError):
                game.set_current_score("thirty")

def test_get_player_name_returns_formatted_str(factory_data):
       game = factory_data()
       result = game.get_player_name()
       assert isinstance(result,str)
       assert result is not None
       assert result[0].isupper()
       res = any(char.isspace()for char in result)
       assert res is False

def test_set_player_name_returns_formatted_str(factory_data):
        game = factory_data()
        old_player_name = game.player_name
        result = game.set_player_name(" harry123")
        assert isinstance(result,str)
        assert result != old_player_name
        assert result[0].isupper()
        res = any(char.isspace()for char in result)
        assert res is False
        with pytest.raises(TypeError):
                game.set_player_name(30)
        
def test_set_player_name_eradicates_swearword_entries(factory_data):
        game = factory_data()
        with pytest.raises(ValueError):
                game.set_player_name(" harry123cunt")
 
def test_get_template_returns_formatted_str(factory_data):
       game = factory_data()
       result = game.get_template()
       assert isinstance(result,str)
       assert result is not None
       res = any(char.isspace()for char in result)
       assert res is False
       assert ".html" in result

def test_set_template_returns_formatted_str(factory_data):
        game = factory_data()
        result = game.set_template("fake")
        assert isinstance(result,str)
        with pytest.raises(TypeError):
                game.set_template(123)
        res = any(char.isspace()for char in result)
        assert res is False
        assert ".html" in result

def test_get_message_returns_formatted_str(factory_data):
       game = factory_data()
       result = game.get_message()
       assert isinstance(result,str)
       assert result is not None

def test_set_message_returns_formatted_str(factory_data):
        game = factory_data()
        old_message = game.message
        result = game.set_message(" fake message")
        assert isinstance(result,str)
        assert result != old_message
        assert result[0].isspace() == False
        assert result[0].isupper()
        with pytest.raises(TypeError):
                game.set_message(30)

def test_get_used_letters_returns_formatted_list(factory_data):
       game = factory_data()
       result = game.get_used_letters()
       assert isinstance(result,list)
       assert result is not None
       res = any(x.isspace()for x in result)
       assert res is False


def test_set_used_letters_returns_formatted_list(factory_data):
       game = factory_data()
       old_used_letters = list(game.used_letters)
       result = game.set_used_letters(" kz")       
       assert isinstance(result,list)
       assert result != old_used_letters
       assert result is not None
       assert not any(
        c.isspace()
        for letter in result
        for c in letter
                )
       assert any(
        c.isupper()
        for letter in result
        for c in letter
                )
       with pytest.raises(TypeError):
                game.set_used_letters(30)
       assert not any(
        len(letter) > 1
        for letter in result
                )
       
def test_get_game_status_returns_Enum(factory_data):
       game = factory_data()     
       result = game.get_game_status()
       assert isinstance(result, Game.Game_status)
       assert result is not None

def test_set_game_status_returns_Enum(factory_data):
       game = factory_data()
       previous_result = Game.Game_status.IN_PLAY       
       result = game.set_game_status(Game.Game_status.WON)
       assert isinstance(result, Game.Game_status)
       assert result != previous_result
       with pytest.raises(TypeError):
                game.set_game_status(30)

def test_set_game_status_accepts_integers(factory_data):
       game = factory_data()
       previous_result = Game.Game_status.IN_PLAY       
       result = game.set_game_status(2)
       assert isinstance(result, Game.Game_status)
       assert result != previous_result


def test_get_accepted_letters_returns_formatted_list(factory_data):
       game = factory_data()
       result = game.get_accepted_letters()
       assert isinstance(result,list)
       assert result is not None
       res = any(x.isspace()for x in result)
       assert res is False

def test_set_accepted_letters_returns_formatted_list(factory_data):
       game = factory_data()
       old_accepted_letters = list(game.accepted_letters)
       result = game.set_accepted_letters(" kz")       
       assert isinstance(result,list)
       assert result != old_accepted_letters
       assert result is not None
       assert not any(
        c.isspace()
        for letter in result
        for c in letter
                )
       assert any(
        c.isupper()
        for letter in result
        for c in letter
                )
       with pytest.raises(TypeError):
                game.set_accepted_letters(30)
       assert not any(
        len(letter) > 1
        for letter in result
                )

def test_get_attempts_remaining_returns_int(factory_data):
       game = factory_data()
       result = game.get_attempts_remaining()
       assert isinstance(result,int)
       assert result >= 0
       assert result is not None

def test_set_attempts_remaining_returns_int(factory_data):
        game = factory_data()
        old_attempts_remaining = game.attempts_remaining
        result = game.set_attempts_remaining(-1)
        assert isinstance(result,int)
        assert result >= 0
        assert result != old_attempts_remaining
        with pytest.raises(TypeError):
                game.set_attempts_remaining("thirty")

def test_get_word_progress_returns_formatted_list(factory_data):
       game = factory_data()
       result = game.get_word_progress()
       assert isinstance(result,list)
       assert result is not None
       res = any(x.isspace()for x in result)
       assert res is False

def test_set_word_progress_validates_input_list(factory_data):
       game = factory_data()
       with pytest.raises(TypeError):
                game.set_word_progress(["",2,"z","y"])
       with pytest.raises(TypeError):
                game.set_word_progress(["","aa","z","y"])
       
def test_set_word_progress_returns_formatted_list(factory_data):
       game = factory_data()
       old_word_progress = list(game.word_progress)
       result = game.set_word_progress(["","","z","y"])       
       assert isinstance(result,list)
       assert result != old_word_progress
       assert result is not None
       assert not any(
        c.isspace()
        for letter in result
        for c in letter
                )
       assert any(
       c.isupper()
       for letter in result
       for c in letter
               )




