"Defines the class self that holds details of the game and provides game specific functions"

from enum import Enum
class Game:

        class Game_choice(Enum): 
                NEW_GAME = 1
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
                if game_status is None:
                        self.set_game_status(self.Game_status.NEW_GAME)
                self.accepted_letters = [] if accepted_letters is None else accepted_letters
                self.attempts_remaining = attempts_remaining
                self.word_progress = [""] if word_progress is None else word_progress

### FOR ECERY SINGLE ATTRIBUTE, MAKE A GET AND A SET

        def get_game_status(self):
                return self["current_game_status"]

        def set_game_status(self, game_status):

                self.game_status = game_status
                if type(game_status) != Game.Game_status:
                        print("The initial type is", type(game_status),game_status)
                        raise TypeError
                       

        def get_player_name(self):
                return self["player_name"]
        
        def set_player_name(self, player_name):
                self["player_name"] = player_name

        def get_message(self):
                return self["message"]

        def set_message(self,message):
                self["message"]=message

        def set_word_progress(self,word_progress):
                self["word_progress"]=word_progress

        def get_attempts_remaining(self):
                return self["attempts_remaining"]

        def set_attempts_remaining(self,attempts_remaining):
                self["attempts_remaining"]=attempts_remaining

        def get_current_score(self):
                return self["current_score"]

        def set_current_score(self,current_score):
                self["cuurent_score"]=current_score

        def set_accepted_letters(self,letter):
                self["accepted_letters"]=self["accepted_letters"].append(letter)

        def set_used_letters(self,letter):
                self["used_letters"]=self["used_letters"].append(letter)

game_status = Game.Game_status.LOST
my_game = Game(game_status)
# my_game.set_game_status(Game.Game_status.IN_PLAY)
my_game.set_game_status(game_status)
print("my_game object id is",my_game)
print(my_game.game_status)



