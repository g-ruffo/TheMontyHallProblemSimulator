# Monty Hall Problem Simulator
This Python program serves as an interactive simulation of the Monty Hall problem, a well-known probability puzzle. The user can play the game manually, or the game can be set to run automatically a specified number of times, collecting data on the outcomes for analysis.

## Project Description
The Monty Hall problem is a counter-intuitive statistics puzzle:

- There are 3 doors, behind which are two goats and a car.
- You pick a door (call it door A). You’re hoping for the car, of course.
- Monty Hall, the game show host, examines the other doors (B & C) and always opens one of them with a goat (call it door B). If both doors B and C have goats behind them, he chooses one randomly.
- Here's the game changer: After Monty Hall opens door B with a goat, he'll ask you if you want to stick with your initial choice (door A) or switch to the unopened door C.
- So, is it to your advantage to switch your choice of doors?

This program offers an opportunity to test this probability puzzle in real time, either by playing the game manually or by setting the game to run automatically a specific number of times.

## Features
- Interactive command-line interface for playing the game manually.
- Automated mode for running the game a specified number of times, with the option to always switch doors or always keep the initial choice.
- Summary of wins and losses, with a calculated win percentage.
- Save game data to a file for further analysis.
- Load game data from a file to continue an analysis.

## Setup & Installation
1. Ensure that Python 3.x is installed on your system.

2. Clone this repository.
     
  ```python
git clone [https://github.com/your-repo/monty-hall-problem.git](https://github.com/g-ruffo/TheMontyHallProblemSimulator.git)
```
3. Navigate to the cloned repository.
     
```python
cd TheMontyHallProblemSimulator
```
  4. Run the program.
   ```python
python game.py
```

## Usage
Once the program is running, follow the prompts in the command line to play the game or to set up an automatic run of the game. The program will provide a summary of wins and losses, along with a win percentage, upon the completion of the games.

## Developed By
Grayson Ruffo

      Copyright 2023 Grayson Ruffo

