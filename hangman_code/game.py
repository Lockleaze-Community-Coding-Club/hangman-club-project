"Purpose: Core game rules and state management. Keep free of Flask imports for easy testing."
"Implements hangman rules and game state management"
"Relationships to routes_py - recieves the selected word from routes and provides feedback on the guess"
"Relationships to routes_py - recieves the selected guess letter from routes and provides feedback on the guess"
"Uses for game operations (start, guess, win/loss)"


- class Game(word, max_attempts=6)
- Game.start_game()
- Game.make_guess(letter)
- Game.display_word()
- Game.is_won()
- Game.is_lost()
- Game.remaining_attempts()
- Game.to_dict()
- Game.from_dict(data)
