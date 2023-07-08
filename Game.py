import json
import os
from typing import List
from Doors import Doors

class Game:
    # Initialize the Game class with relevant instance variables
    def __init__(self):
        # A list to keep track of completed games, each game is an instance of the Doors class
        self.completed_games: List[Doors] = []
        # Integer variables to store the total number of games and wins
        self.total_games = 0
        self.total_wins = 0
        # Variable to store the win average
        self.win_average = 0
        # Variable to store the filename of the saved game
        self.filename = None
        # Directory to save games
        self.save_dir = "saved_games"  # directory to save games

    # Function to set up the game
    def setup_game(self):
        # This function prompts the user for the number of games they would like to play and whether they would like to play manually or automatically
        # The function will continue to prompt until valid input is received
        # On receipt of valid input, the function will start the relevant game type
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
        # This function prompts the user for their choice to switch doors and guess number in the automatic game
        # On receipt of valid input, the function will start the automatic game with the provided parameters
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
        # This function runs the automatic game the specified number of times
        # Each game result is appended to the completed_games list
        # After all games are completed, the function calculates and prints the win average
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
        # This function runs the manual game the specified number of times
        # Each game result is appended to the completed_games list
        # After all games are completed, the function calculates and prints the win average
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
        # This function adds a completed game to the completed_games list
        self.completed_games.append(finished_game)

    def calculate_win_average(self):
        # This function calculates the win average from completed games and prints the total number of games, number of wins and win average
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
        # This function resets the game state, clearing the completed_games list and resetting the total_games, total_wins and win_average variables
        self.completed_games: List[Doors] = []
        self.total_games = 0
        self.total_wins = 0
        self.win_average = 0

    def save_to_file(self):
        # This function saves the completed games to a file
        # If the filename is not already set, it prompts the user for a filename
        # The function ensures the save directory exists, creates it if not
        # The function then converts the completed games to a list of dictionaries and writes this to a file in the save directory
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
        # This class method loads a game from a file and returns a Game instance
        # The method reads a list of dictionaries from the file and converts this back into a list of Doors instances, adding each one to the game's completed_games list
        # After loading all the games, the function calculates and prints the win average

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

    # This function prints a line break
    def print_line_break(self):
        print("******************")
