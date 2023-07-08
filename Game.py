from typing import List
from Doors import Doors

class Game:

    def __init__(self):
        self.completed_games: List[Doors] = []
        self.total_games = 0
        self.total_wins = 0
        self.win_average = 0
        self.number_of_plays = 0

    def setup_game(self):
        while self.number_of_plays == 0:
            value = input("How many times would you like to run the game?\nEnter a number greater than 0:")
            try:
                self.number_of_plays = int(value)
                if self.number_of_plays > 0:
                    break
                else:
                    print("You need to enter a number greater than 0!")
            except ValueError:
                print("Please enter a valid number!")
                continue

        waiting_for_response = True

        while waiting_for_response:
            response = input("Would You Like to Play Manually or Run Automatically\nEnter M for manual or A for auto: ")
            try:
                if response.lower() == "m":
                    waiting_for_response = False
                    self.begin_manual_game()
                    break
                elif response.lower() == "a":
                    waiting_for_response = False
                    break
                else:
                    print("You entered an invalid value. Please try again.")
                    continue
            except Exception as e:
                print("There was an error in your input:" + str(e))
                continue

    def setup_automatic_game(self):
        pass
    def begin_automatic_games(self):
        pass
    def begin_manual_game(self):
        for game in range(self.number_of_plays):
            print("Starting Game:{}".format(game + 1))
            new_game = Doors()
            new_game.start_manual_game()
            self.completed_games.append(new_game)
        print("That's It, You Are Done!")
        self.calculate_win_average()

    def add_result_to_list(self, finished_game):
        self.completed_games.append(finished_game)

    def calculate_win_average(self):
        self.total_games = len(self.completed_games)
        if self.total_games == 0:
            print("You do not have any completed games.")
            return

        self.total_wins = 0

        for game in self.completed_games:
            if game.did_win:
                self.total_wins += 1

        self.win_average = self.total_wins / len(self.completed_games)
        print("You Played {} Games and Won {}".format(self.total_games, self.total_wins))
        print("Your Win Average Is: {}".format(self.win_average))
