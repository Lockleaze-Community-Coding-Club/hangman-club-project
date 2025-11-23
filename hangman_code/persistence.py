"Stores words lists and , stores previous game "
"and cumulative scores, even after the game is closed"
"Relationship to word_selection - provides the"
" word list on request to word_selection"
"Relationship to routes - provides the cumulative score"

class Persistence():

    def _init_(self):
        return None

    def persistence():
        return None

    def previous_scores():
        return None
    
    def cumulative_score():
        return None
    
    def load_game_state(game_id, path='data/games.json'):
        return None

#Purpose: Durable storage for word lists, saved games 
# and optional scores. Implemented as JSON files under /data/.
#- save_game_state(game_id, data, path='data/games.json')
#- delete_game_state(game_id, path='data/games.json')
#- list_saved_games(path='data/games.json')
#- load_word_list(path='data/words.json')
