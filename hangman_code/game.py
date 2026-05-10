"Defines the class Game that holds details of the game and provides game specific functions"

from enum import Enum
class Game:

        class load_game(Enum): 
                NEW_GAME = 1
                RESUME_GAME = 2
                FACTORY_RESET = 3
                EXIT_GAME = 4

        class Game_status(Enum): # RP: I have made a note of this 
        # in game_status_function
                NEW_GAME = 0
                IN_PLAY = 1
                WON = 2
                LOST = 3

        def __init__(
                self,
                word: list[str] | None = None,
                game_id: int | None = None,
                current_score: int = 0,
                player_name: str | None = None,
                template = "index",
                message: str = "initial message",
                used_letters: list[str] | None = None,
                game_status: Game_status| None = None,
                accepted_letters: list[str] | None = None,
                attempts_remaining: int = 10,
                word_progress: list[str] | None = None,
                    ) -> None:
        
                self.word = [""] if word is None else word
                self.game_id = id(self) if game_id is None else game_id
                self.current_score = current_score
                self.player_name = player_name
                self.template = template
                self.message = message
                self.used_letters = [] if used_letters is None else used_letters
                self.game_status = [] if game_status is None else game_status
                self.accepted_letters = [] if accepted_letters is None else accepted_letters
                self.attempts_remaining = attempts_remaining
                self.word_progress = [""] if word_progress is None else word_progress

### FOR ECERY SINGLE ATTRIBUTE, MAKE A GET AND A SET

def get_game_status(game):
        return game["current_game_status"]

def set_game_status(game, game_status):
        game["game_status"] = game_status

def get_player_name(game):
        return game["player_name"]
    
def set_player_name(game, player_name):
        game["player_name"] = player_name

def get_message(game):
        return game["message"]

def set_message(game,message):
        game["message"]=message

def set_word_progress(game,word_progress):
        game["word_progress"]=word_progress

def get_attempts_remaining(game):
        return game["attempts_remaining"]

def set_attempts_remaining(game,attempts_remaining):
        game["attempts_remaining"]=attempts_remaining

def get_current_score(game):
        return game["current_score"]

def set_current_score(game,current_score):
        game["cuurent_score"]=current_score

def set_accepted_letters(game,letter):
        game["accepted_letters"]=game["accepted_letters"].append(letter)

def set_used_letters(game,letter):
        game["used_letters"]=game["used_letters"].append(letter)