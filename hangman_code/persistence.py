"Stores words lists and , stores previous game and cumulative scores, even after the game is closed"
"Relationship to word_selection - provides the word list on request to word_selection"
"Relationship to routes - provides the cumulative score"

def persistence():

    def previous_scores():
        return "none"
    
    def cumulative_score():
        return "none"
    
    return "none"

Purpose: Durable storage for word lists, saved games and optional scores. Implemented as JSON files under /data/.
- save_game_state(game_id, data, path='data/games.json')
- load_game_state(game_id, path='data/games.json')
- delete_game_state(game_id, path='data/games.json')
- list_saved_games(path='data/games.json')
- load_word_list(path='data/words.json')
