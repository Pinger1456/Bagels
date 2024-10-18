# Bagels - Deductive Logic Game

## Overview
**Bagels** is a deductive logic game in which the player has to guess a secret number based on clues provided after each guess. The game doesn't allow repeated digits in the secret number, and the clues you receive guide you towards the correct answer. The game is inspired by the version created by Al Sweigart, which demonstrates basic principles of game design using Python.

## How the Game Works
- The computer randomly generates a secret number with no repeated digits.
- After each guess, the game provides clues:
  - **Fermi** means one digit is correct and in the correct position.
  - **Pico** means one digit is correct but in the wrong position.
  - **Bagels** means no digit is correct.
- The player has to guess the number using these clues.
- The game continues until the player guesses the correct number or runs out of guesses.

## Clues
- **Fermi**: One digit is correct and in the correct position.
- **Pico**: One digit is correct but in the wrong position.
- **Bagels**: No digits are correct.

## Example
If the secret number is `248` and the player's guess is `843`, the clues will be:
- **Fermi Pico**:
  - **Fermi** for the digit `4` (correct position and digit).
  - **Pico** for the digit `8` (correct digit but wrong position).

## How to Run the Game

### Requirements
- **Python 3.x** is required to run the game.
- No additional dependencies are required.

### Installation and Execution

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Pinger1456/Bagels.git
Navigate to the project directory:



cd Bagels
Run the game:

bash
Копировать код
python game.py
Game Instructions
After starting the game, you will be prompted to guess a number based on the number of digits chosen by the game.
After each guess, you'll receive clues (Fermi, Pico, or Bagels).
Continue guessing until you correctly identify the secret number or run out of allowed guesses.
Example Output
vbnet
Копировать код
Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com

I am thinking of a 3-digit number with no repeated digits.
Try to guess what it is.
Here are some clues:
  When I say:    That means:
  Pico         One digit is correct but in the wrong position.
  Fermi        One digit is correct and in the right position.
  Bagels       No digit is correct.

You have 10 guesses to get it.

Guess #1: 
> 123
Fermi
Guess #2: 
> 256
Bagels
Guess #3: 
> 429
Fermi Pico
...
Project Structure
game.py - Main script that runs the game logic.
config.py - Stores the configuration for the game, such as the number of digits in the secret number and the number of guesses allowed.
.env - Environment file where the number of digits and guesses can be set.
Features
The game allows players to choose the number of digits in the secret number.
Customizable number of guesses via the .env file.
Simple text-based interface with interactive gameplay.
Gives feedback after every guess to help guide the player.
Future Enhancements
Add difficulty levels (e.g., different numbers of digits for easy, medium, and hard modes).
Implement a graphical interface (GUI) for improved user experience.
Add multiplayer mode where players take turns guessing each other's numbers.
Keep track of high scores and fastest guesses.
License
This project is licensed under the MIT License. See the LICENSE file for details.
