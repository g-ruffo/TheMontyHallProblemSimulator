import os
from Game import Game

def main_menu():
    # Main menu infinite loop
    while True:
        print("\nMain Menu:")
        print("1. Create new game")
        print("2. Load existing game")
        print("3. Exit")

        # Get the user's menu choice
        choice = input("Enter your choice: ")

        # Depending on the choice, perform the selected menu action
        if choice == "1":
            game = Game()  # Create a new game
            game.setup_game()  # Set up the game
            game_menu(game)  # Enter the game menu with the new game
        elif choice == "2":
            load_game_menu()  # Load an existing game
        elif choice == "3":
            print("Exiting the application...")  # Exit the application
            break
        else:
            print("Invalid choice. Please try again.")  # If the input was not valid, ask again

def load_game_menu():
    # Get the path of the saved games directory
    saved_games_dir = os.path.join(os.getcwd(), "saved_games")

    try:
        # Get the list of all saved games
        saved_games = os.listdir(saved_games_dir)
    except FileNotFoundError:
        # If the directory does not exist, print a message and return to the previous menu
        print("No saved games found.")
        return

    if not saved_games:
        # If there are no saved games, print a message and return to the previous menu
        print("No saved games found.")
        return

    # Print the list of all saved games
    for i, saved_game in enumerate(saved_games, start=1):
        print(f"{i}. {saved_game}")

    # Get the user's choice of which game to load
    while True:
        choice = input("Enter the number of the game you want to load, or B to go back: ")
        if choice.lower() == "b":
            # If the user wants to go back, break the loop
            break

        try:
            # Try to convert the choice to an integer and load the chosen game
            choice = int(choice)
            game_filename = saved_games[choice - 1]  # Subtract 1 because list indices start at 0, but our printed list starts at 1
            game = Game.load_from_file(os.path.join(saved_games_dir, game_filename))  # Load the game
            game_menu(game)  # Enter the game menu with the loaded game
            break
        except (ValueError, IndexError):
            # If the choice was not a valid integer or was out of the range of the saved games list, print an error message and ask again
            print("Invalid choice. Please try again.")

def game_menu(game):
    # Game menu infinite loop
    while True:
        print("\nGame Menu:")
        print("1. Save game")
        print("2. Close game and load a new one")
        print("3. Close game and create a new one")
        print("4. Calculate win average")
        print("5. Clear game")
        print("6. Play again")
        print("7. Back to main menu")

        # Get the user's menu choice
        choice = input("Enter your choice: ")

        # Depending on the choice, perform the selected game action
        if choice == "1":
            game.save_to_file()  # Save the game state to a file
        elif choice == "2":
            load_game_menu()  # Load a new game
            break  # Break the game menu loop and go back to the main menu
        elif choice == "3":
            game = Game()  # Create a new game
            game.setup_game()  # Set up the new game
        elif choice == "4":
            game.calculate_win_average()  # Calculate and display the win average
        elif choice == "5":
            game.clear_game()  # Clear the current game state
        elif choice == "6":
            game.setup_game()  # Set up the game again to play
        elif choice == "7":
            print("Returning to main menu...")  # Go back to the main menu
            break  # Break the game menu loop and go back to the main menu
        else:
            print("Invalid choice. Please try again.")  # If the input was not valid, ask again


if __name__ == "__main__":
    main_menu()  # Start the main menu


