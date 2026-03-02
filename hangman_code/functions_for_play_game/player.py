class Player:

    def __init__(
        self,
        player_name : str | None = None,
        current_score : int | None = None,
        cumulative_score : int | None = None,
        number_of_games_played: int | None = None,
        number_of_games_won : int | None = None,
                 ) -> None:

                self.player_name = player_name
                self.current_score = current_score
                self.cumulative_score = cumulative_score
                self.number_of_games_played = number_of_games_played
                self.number_of_games_won = number_of_games_won

