from json import load, dumps
from hangman_code.game import Game


def turn_game_into_data(object):
       
        if type(object) is Game:
                data_constructor = object
                data = data_constructor.__dict__
                return data
        else:
                raise(ValueError)

def turn_dict_into_game(data: dict) -> "Game":
        """Rebuild a Game instance from a dict (e.g. from session)."""

        if type(data) is dict:
                return Game(
                        word = data["word"],
                        game_id = data["game_id"],
                        current_score = data["current_score"],
                        player_name = data["player_name"],
                        template = data["template"],
                        message = data["message"],
                        used_letters = data["used_letters"],
                        game_status = data["game_status"],
                        accepted_letters = data["accepted_letters"],
                        attempts_remaining = data["attempts_remaining"],
                        word_progress = data["word_progress"]
                        )
        else:
                raise(ValueError)


def from_dict(json_filename, player_name):
        #if json_filename is None:
        #json_filename = config.json_filename
        #This function retrieves the game data from the storage area json
        
        with open(json_filename, 'r') as file:
         
                game = load(file) # this is the dictionary
                game = turn_dict_into_game(game)
                if type(game) is Game:
                        return game
                else:
                        raise(ValueError)

def to_dict(data, json_filename):
        #This function inputs game data to the storage area json
                data = turn_game_into_data(data)
                send_data = dumps(data, indent=4)
                with open(json_filename, "w") as f:
                        f.write(send_data)


def read_and_find(file_path,player_name):

    with open(file_path, "r") as file:
        game = load(file)
        """This is used in start_game to search on player name and see if
        any are still in play"""
    if game["player_name"] == player_name and game["game_status"] == 1:
            result = game["game_id"]
            return result
    else:
            return None