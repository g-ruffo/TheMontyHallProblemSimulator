
import random

class Doors:
    def __init__(self):
        self.winning_door_number = random.randint(0, 2)
        self.closed_doors = self.create_closed_doors()
        self.open_doors = self.create_open_doors()
        self.remaining_doors = list(range(0, 3))
        self.user_guess = None
        self.user_switched = None
        self.did_win = None
        self.system_game = False
        self.system_should_switch = None
    def start_manual_game(self):
        self.show_doors_closed(True)

    def start_automatic_game(self, should_switch):
        self.system_game = True
        self.system_should_switch = should_switch
        self.show_doors_closed(True)

    def create_closed_doors(self):
        doors = []
        for door_number in range(0, 3):
            door = self.CLOSEDDOOR.format(self.DOORNUMBERS[door_number])
            doors.append(door)
        return doors

    def create_open_doors(self):
        doors = []
        for door_number in range(0, 3):
            if door_number == self.winning_door_number:
                doors.append(self.WINNERDOOR)
            else:
                doors.append(self.LOSERDOOR)
        return doors

    def show_doors_closed(self, isclosed):
        doors = self.closed_doors if isclosed else self.open_doors
        doors_split = [door.split('\n') for door in doors]
        for lines in zip(*doors_split):
            print("        ".join(lines))
        if self.user_guess is None:
            self.guess_door_number()
        elif self.user_switched is None and isclosed:
            self.offer_to_switch()
        elif not isclosed:
            self.show_winner()

    def guess_door_number(self):
        while self.user_guess is None:
            print("Guess Which Door the Prize is Behind! \nEnter the door number:")
            if self.system_game:
                value = random.randint(0, 2)
            else:
                value = input()
            try:
                number = int(value)
                if 1 <= number <= 3:
                    self.user_guess = number - 1
                    print("You Guessed Door Number {}".format(str(number)))
                    self.open_hint_door()
                    break
                else:
                    print("You need to enter 1, 2, or 3!")
            except ValueError:
                print("Please enter a valid number!")
                continue

    def offer_to_switch(self):
        while self.user_switched is None:
            guess_string = self.user_guess + 1
            remaining_door = self.remaining_doors[0]
            print("Would You Like to Switch Your Choice From {} to {}\nEnter Y to switch or N to keep:".format(guess_string, remaining_door + 1))
            if self.system_game:
                response = "y" if self.system_should_switch else "n"
            else:
                response = input()
            try:
                if response.lower() == "y":
                    self.user_switched = True
                    self.user_guess = remaining_door
                    self.show_doors_closed(False)
                    break
                elif response.lower() == "n":
                    self.user_switched = False
                    self.show_doors_closed(False)
                else:
                    print("You entered an invalid value. Please try again.")
                    continue
            except Exception as e:
                print("There was an error in your input:" + str(e))
                continue

    def show_winner(self):
        self.did_win = self.winning_door_number == self.user_guess
        winning_string = str(self.winning_door_number + 1)
        if self.did_win:
            print("Congratulations, Door number {} was the correct answer. \nEnjoy your new car!".format(winning_string))
        else:
            print("Ooooo I am sorry, Door number {} was the correct answer. \nHere's a Goat!".format(winning_string))

    def open_hint_door(self):
        self.remaining_doors.remove(self.user_guess)
        reveal = self.first_non_matching(self.winning_door_number)
        self.remaining_doors.remove(reveal)
        self.closed_doors[reveal] = self.LOSERDOOR
        print("Now because I am such a nice guy, I will give you a hint.\nI will open one of the other doors and then give you the opportunity to switch.")
        self.show_doors_closed(True)

    def first_non_matching(self, winner):
        for door in self.remaining_doors:
            if door != winner:
                return door

    DOORNUMBERS = ["1️⃣", "2️⃣", "3️⃣"]
    CLOSEDDOOR = """
🟫🟫🟫🟫🟫🟫
🟫         🟫
🟫   {}    🟫
🟫         🟫
🟫 🟤      🟫
🟫         🟫
🟫         🟫
🟫         🟫
🟫🟫🟫🟫🟫🟫"""

    LOSERDOOR = """
🟥🟥🟥🟥🟥🟥
🟥        🟥
🟥   ❌   🟥
🟥        🟥
🟥        🟥
🟥   🐐   🟥
🟥        🟥
🟥        🟥
🟥🟥🟥🟥🟥🟥"""
    WINNERDOOR = """
🟩🟩🟩🟩🟩🟩
🟩        🟩
🟩   💰   🟩
🟩        🟩
🟩        🟩
🟩   🏎️   🟩
🟩        🟩
🟩        🟩
🟩🟩🟩🟩🟩🟩"""
