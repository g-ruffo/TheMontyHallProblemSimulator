from typing import List

import Doors


class Game:

    def __int__(self):
        self.completed_games: List[Doors] = []

    def add_result_to_list(self, finished_game):
        self.completed_games.append(finished_game)

    def calculate_win_average(self):
        total_games = len(self.completed_games)
        if total_games == 0:
            print("You do not have any completed games.")
            return
        total_wins = 0

        for game in self.completed_games:
            if game.did_win:
                total_wins += 1
