

import random

class Doors:
    def __init__(self):
        self.winningDoorNumber = random.randint(0, 3)
        self.startingDoors = self.createInitialDoors()

    def createInitialDoors(self):
        doors = []
        for doorNumber in range(0, 3):
            door = self.CLOSEDDOOR.format(self.DOORNUMBERS[doorNumber])
            doors.append(door)
        return doors

    def showStartingDoors(self):
        doors_split = [door.split('\n') for door in self.startingDoors]
        for lines in zip(*doors_split):
            print("        ".join(lines))


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


