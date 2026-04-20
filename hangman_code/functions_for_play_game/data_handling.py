### ADD IN AN ABILITY TO CREATE A GUESSED WORDS LIST FROM PERSISTENCE


from json import load, dumps
from hangman_code.functions_for_play_game.guessed_letters import used_letters_function
#from hangman_code.functions_for_play_game.guessed_letters import guessed_words_function
#from hangman_code.functions_for_play_game.scores_and_attempts_function import remaining_attempts_function
#from hangman_code.functions_for_play_game.scores_and_attempts_function import update_score_function
from hangman_code.game import Game
#from hangman_code.functions_for_play_game.player import Player

def initialise_game_and_data(object):
        data_constructor = object()
        data = data_constructor.__dict__
        return data 

def update_data(key, value, data):
        #This updates the dictionary each time a guess is made
        data.update({key: value})

      
def update_in_play_data(data, letter, 
                       word_progress, message, guess_result,
                       attempts_remaining, 
                       current_score, word_attempt):



        """The updates to the game data shall now be created"""

        used_letters = used_letters_function(letter, data["used_letters"])
        #This will update list of used letters

        #words_guessed = guessed_words_function(word_attempt, data["words_guessed"])
        #This will update the list of previously guessed words

        #attempts_remaining = remaining_attempts_function(attempts_remaining)
        #This will update the number of remaining attempts

        #current_score = update_score_function(current_score)
        #This will update the score value

        data["guessed_word"] = word_progress
        data["message"] = message
        data["guess_result"] = guess_result
        data["used_letters"] = used_letters
        #data["words_guessed"] = words_guessed
        data["attempts_remaining"] = attempts_remaining
        data["current_score"] = current_score

        return data

def global_dictionary_update(data):

        # Update dictionary with updated guess_result
        update_data("word_progress", data.guess_result, data)
        # Update dictionary with used letters
        update_data("used_letters", data.letter, data)
        # Update dictionary with used word guesses
        update_data("guessed_words", data.guessed_word, data)
        # Update dictionary with game status
        update_data("game_status", data.current_game_status, data)
        # Update dictionary with remaining attempts
        update_data("remaining_attempts", data.attempts_remaining, data)
        # Update dictionary with score from last game
        update_data("score_keeping", data.current_score, data)
        # Update dictionary with cumulative score from last game
        update_data("cumulative score", data.cumulative_score, data)
        # Update dictionary with number of games played in total
        update_data("number_games_played", data.number_of_games_played, data)
        # Update dictionary with number of games won in total
        update_data("number_games_won", data.number_of_games_won, data)
        # Update dictionary with index of current game
        update_data("number_games_won", data.game_id, data)


def from_dict(json_filename):
        #if json_filename is None:
        #json_filename = config.json_filename
        #This function retrieves the game data from the storage area json
     
        with open(json_filename, 'r') as file: 
                game = load(file) # this is the dictionary
                #value = data.get(key, None)  # returns None if key missing
                return game

def to_dict(data, json_filename):
        #This function inputs game data to the storage area json

                send_data = dumps(data, indent=4)
                with open(json_filename, "w") as f:
                        f.write(send_data)

def to_dict(self):
        """Serialize the game to plain types (for session / JSON)."""
        return {
            "game_id": self.game_id,
            "game_name": self.get_game_name(),
            "score": self.score,
            "word": self.word,
            "template": self.template,
            "message": self.message,
            "used_letters": self.used_letters,
            "accepted_letters": self.accepted_letters,
            "game_status": self.game_status.value,  # store enum as int
        }

@classmethod
def from_dict(cls, data: dict) -> "Game":
        """Rebuild a Game instance from a dict (e.g. from session)."""
        return cls(
            game_name=data.get("game_name",""),
            word=data["word"],
            game_id=data.get("game_id", 1),
            score=data.get("score", 10),
            template=data.get("template"),
            message=data.get("message"),
            used_letters=data.get("used_letters", []),  # ✅ default to []
            accepted_letters=data.get("accepted_letters", []),
            game_status=Game.Game_status(data.get("game_status", 0)),
        )