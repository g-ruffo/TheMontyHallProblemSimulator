import json
import os
from typing import List
from Doors import Doors

class Game:

    def __init__(self):
        self.completed_games: List[Doors] = []
        self.total_games = 0
        self.total_wins = 0
        self.win_average = 0
        self.filename = None
        self.save_dir = "saved_games"  # directory to save games

    def setup_game(self):
        number_of_plays = 0
        while number_of_plays == 0:
            self.print_line_break()
            value = input("How many times would you like to run the game?\nEnter a number greater than 0:")
            try:
                number_of_plays = int(value)
                if number_of_plays > 0:
                    break
                else:
                    print("You need to enter a number greater than 0!")
            except ValueError:
                print("Please enter a valid number!")
                continue

        waiting_for_response = True

        while waiting_for_response:
            self.print_line_break()
            response = input("Would You Like to Play Manually or Run Automatically\nEnter M for manual or A for auto: ")
            try:
                if response.lower() == "m":
                    waiting_for_response = False
                    self.begin_manual_game(number_of_plays)
                    break
                elif response.lower() == "a":
                    waiting_for_response = False
                    self.setup_automatic_game(number_of_plays)
                    break
                else:
                    print("You entered an invalid value. Please try again.")
                    continue
            except Exception as e:
                print("There was an error in your input:" + str(e))
                continue

    def setup_automatic_game(self, number_of_plays):
        should_switch = None
        while should_switch is None:
            self.print_line_break()
            response = input("Would You Like the System to Accept the Offer to Switch its Guess?\nEnter Y to switch or N to refuse: ")
            try:
                if response.lower() == "y":
                    should_switch = True
                    break
                elif response.lower() == "n":
                    should_switch = False
                    break
                else:
                    print("You entered an invalid value. Please try again.")
                    continue
            except Exception as e:
                print("There was an error in your input:" + str(e))
                continue

        waiting_for_response = True

        while waiting_for_response:
            self.print_line_break()
            value = input("Enter a number between 1 and 3 to set the guess for each game,\nor enter R to randomly select a new guess for each game:")
            if value.lower() == "r":
                waiting_for_response = False
                self.begin_automatic_games(number_of_plays, should_switch, None)
            else:
                try:
                    number = int(value)
                    if 1 <= number <= 3:
                        waiting_for_response = False
                        self.begin_automatic_games(number_of_plays, should_switch, number)
                    else:
                        print("You need to enter 1, 2, 3 or R!")
                except ValueError:
                    print("Please enter a valid number!")
                    continue

    def begin_automatic_games(self, number_of_plays, should_switch, guess_number):
        for game in range(number_of_plays):
            self.print_line_break()
            print("Starting Game:{}".format(game + 1))
            self.print_line_break()
            new_game = Doors()
            new_game.start_automatic_game(should_switch, guess_number)
            self.completed_games.append(new_game)
            self.print_line_break()
        print("That's It, You Are Done!")
        self.print_line_break()
        self.calculate_win_average()

    def begin_manual_game(self, number_of_plays):
        for game in range(number_of_plays):
            self.print_line_break()
            print("Starting Game:{}".format(game + 1))
            self.print_line_break()
            new_game = Doors()
            new_game.start_manual_game()
            self.completed_games.append(new_game)
            self.print_line_break()
        self.print_line_break()
        print("That's It, You Are Done!")
        self.print_line_break()
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
        print("Your Win Average Is: %{}".format(self.win_average * 100))

    def clear_game(self):
        self.completed_games: List[Doors] = []
        self.total_games = 0
        self.total_wins = 0
        self.win_average = 0

    def save_to_file(self):
        if self.filename is None:
            while True:
                filename = input("Please enter a filename to save the game results: ").strip()
                if filename:
                    self.filename = filename
                    break
                else:
                    print("Filename cannot be blank. Please try again.")

        # Make sure the directory exists. If not, create it.
        os.makedirs(self.save_dir, exist_ok=True)

        # Create full path for the file
        full_path = os.path.join(self.save_dir, self.filename)

        # Convert game state to a list of dictionaries
        game_data = [vars(game) for game in self.completed_games]

        try:
            # Write the data to a file
            with open(full_path, 'w') as file:
                json.dump(game_data, file)
            print("Game saved successfully in {}".format(full_path))
        except IOError as e:
            print("Unable to save game: {}".format(e))
        except Exception as e:
            print("Unexpected error occurred while saving game: {}".format(e))

    @classmethod
    def load_from_file(cls, filename):
        # Create a new game instance
        game = cls()

        try:
            # Load the data from a file
            with open(filename, 'r') as file:
                game_data = json.load(file)

            # Convert dictionaries back to Doors instances and store them in the game
            for game_dict in game_data:
                door = Doors()
                door.__dict__.update(game_dict)
                game.add_result_to_list(door)

            # Calculate win average based on loaded games
            game.calculate_win_average()
        except IOError as e:
            print("Unable to load game: {}".format(str(e)))
        except ValueError as e:
            print("Invalid game data: {}".format(str(e)))
        except Exception as e:
            print("Unexpected error occurred while loading game: {}".format(str(e)))

        return game

    def print_line_break(self):
        print("******************")
