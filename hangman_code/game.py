"Defines the class Game that holds details of the game and provides game specific functions"

from enum import Enum
class Game:

        class load_game(Enum): 
                NEW_GAME = 1
                RESUME_GAME = 2
                FACTORY_RESET = 3
                EXIT_GAME = 4

        def __init__(
                self,
                word: list[str] | None = None,
                game_id: int | None = None,
                current_score: int = 0,
                template = "index",
                message: str = "initial message",
                used_letters: list[str] | None = None,
                game_started: bool = True,
                current_game_status: list[str] | None = None,
                accepted_letters: list[str] | None = None,
                guess_result: list[str] | None = None,
                attempts_remaining: int = 10,
                guessed_word: list[str] | None = None,
                words_guessed: list[str] | None = None,
                start_game_selection: load_game = load_game.NEW_GAME,
                game_closed: bool = False,
                    ) -> None:
        
                self.word = [""] if word is None else word
                self.game_id = id(self) if game_id is None else game_id
                self.current_score = current_score
                self.template = template
                self.message = message
                self.used_letters = [] if used_letters is None else used_letters
                self.game_started = game_started
                self.current_game_status = [] if current_game_status is None else current_game_status
                self.accepted_letters = [] if accepted_letters is None else accepted_letters
                self.guess_result = [""] if guess_result is None else guess_result
                self.attempts_remaining = attempts_remaining
                self.guessed_word = [""] if guessed_word is None else guessed_word
                self.words_guessed = [""] if words_guessed is None else words_guessed
                self.start_game_selection = start_game_selection
                self.game_closed = game_closed
