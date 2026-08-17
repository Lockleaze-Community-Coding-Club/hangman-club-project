from enum import IntEnum
"Defines the class self that holds details of the game and "
"provides game specific functions"


class Game:

        class Game_choice(IntEnum): 
                NEW_GAME = 1
                EXIT_GAME = 4

        class Game_status(IntEnum): # RP: I have made a note of this 
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
                player_name: str | None = "Enter_name",
                template = "index.html",
                message: str = "initial message",
                used_letters: list[str] | None = None,
                game_status: Game_status| None = None,
                accepted_letters: list[str] | None = None,
                attempts_remaining: int = 8,
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
                else: 
                        self.game_status = game_status
                self.accepted_letters = [] if accepted_letters is None else accepted_letters
                self.attempts_remaining = attempts_remaining
                self.word_progress = [""] if word_progress is None else word_progress

# FOR EVERY SINGLE ATTRIBUTE, THERE IS A GET AND A SET

        def get_word(self):
                return self.word
        
        def set_word(self,chosen_word):
                # This function takes an input of a list and returns a list
                if isinstance(chosen_word, list):
                        self.word = chosen_word
                        return self.word
                else:
                        raise TypeError

        def get_game_id(self):
                return self.game_id

        def set_game_id(self, new_id):
                if isinstance(new_id, int):
                        self.game_id = new_id
                        return self.game_id
                else:
                        raise TypeError
        
        def get_current_score(self):
                return self.current_score

        def set_current_score(self,current_score):
                if isinstance(current_score, int):
                        self.current_score = current_score
                        return self.current_score
                else:
                        raise TypeError
                
        def get_player_name(self):
                return self.player_name
        
        def set_player_name(self, player_name):
                swearlist = ["fuck", "wank", "shit", "cunt"]
                if isinstance(player_name, str):
                        if any ([x in player_name for x in swearlist]):
                                raise ValueError()
                        self.player_name = player_name
                        return self.player_name.strip().capitalize()                
                else:
                        raise TypeError

        def get_template(self):
                return self.template
        
        def set_template(self, template_name):
                if isinstance(template_name, str):
                        if ".html" in template_name:
                                self.template = template_name
                                return self.template.strip()
                        else:
                                self.template = template_name.__add__(".html")
                                return self.template.strip() 
                else:
                        raise TypeError
 
        def get_message(self):
                return self.message

        def set_message(self,message):
                if isinstance(message, str):
                        self.message = message
                        return self.message.strip().capitalize()
                else:
                        raise TypeError

        def get_used_letters(self):
                return self.used_letters       
        
        def set_used_letters(self,letter):
                if isinstance(letter, str):
                        self.used_letters.append(letter.strip()
                                                 .capitalize()[:1])
                        return self.used_letters
                else:
                        raise TypeError
        
        def get_game_status(self):
                return self.game_status
                
        def set_game_status(self, game_status):
                try:
                        self.game_status = Game.Game_status(game_status)
                        return self.game_status
                except ValueError:
                    raise TypeError(f"{game_status!r} is not a valid Game_status")
        
        def get_accepted_letters(self):
                return self.accepted_letters

        def set_accepted_letters(self,letter):
                if isinstance(letter, str):
                        self.accepted_letters.append(letter.strip()
                                                 .capitalize()[:1])
                        return self.accepted_letters
                else:
                        raise TypeError
        
        def get_attempts_remaining(self):
                return self.attempts_remaining

        def set_attempts_remaining(self,attempts_remaining):
                if isinstance(attempts_remaining, int):
                        if attempts_remaining >= 0:
                                self.attempts_remaining = attempts_remaining
                                return self.attempts_remaining
                        else:
                                return 0
                else:
                        raise TypeError

        def get_word_progress(self):
                return self.word_progress
        
        def set_word_progress(self,word_progress):
                # This function takes an input of a list and returns a list
                if isinstance(word_progress, list):
                        word_progress_list = []
                        for character in word_progress:
                                if isinstance(character,int):
                                        raise TypeError
                                if len(character) > 1:
                                        raise TypeError
                                word_progress_list.append(character.strip()
                                                          .capitalize())
                        self.word_progress = word_progress_list
                        return self.word_progress
                else:
                        raise TypeError





