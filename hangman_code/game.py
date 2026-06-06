"Defines the class Game that holds details of the game and provides game specific functions"

from enum import Enum
class Game:

        class Game_choice(Enum): 
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
                score: int = 0,
                player_name: str | None = None,
                template = "index",
                message: str = "initial message",
                used_letters: list[str] | None = None,
                game_status: Game_status| None = None,
                accepted_letters: list[str] | None = None,
                guess_result: list[str] | None = None,
                attempts_remaining: int = 10,
                guessed_word: list[str] | None = None,
                    ) -> None:
        
                self.word = [""] if word is None else word
                self.game_id = id(self) if game_id is None else game_id
                self.set_score(score)
                self.player_name = player_name
                self.template = template
                self.message = message
                self.used_letters = [] if used_letters is None else used_letters
                self.game_status = [] if game_status is None else game_status
                self.accepted_letters = [] if accepted_letters is None else accepted_letters
                self.guess_result = [""] if guess_result is None else guess_result
                self.attempts_remaining = attempts_remaining
                self.guessed_word = [""] if guessed_word is None else guessed_word

### FOR ECERY SINGLE ATTRIBUTE, MAKE A GET AND A SET


        def set_score(self, score):
                if isinstance(score, int):
                        self.score = score
                elif score == None:
                        self.score = 0
                else:
                        raise ValueError("score must be an integer")
                return    
        
        def set_game_status(game_status):
                game_status = game_status
                #raise ValueError ('error on init')
                return

        def get_player_name(player, player_name):
                return player_name
        
        def set_player_name(player, player_name):
                return  player_name
        
