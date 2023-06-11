# Mike's Battleship Game

## Introduction
Mike's Battleship Game is a Python console-based application that recreates the classic game of Battleship. The game allows players to strategically place their battleships on a grid and engage in a battle against the computer. It provides an entertaining and engaging experience for users to test their tactical skills and luck.

## Mockups of game
![Mockup of starting page](https://github.com/MikesCodingCreations/Portfolio3/blob/main/assets/main_page1.png)
![Mockup of menu screen page](https://github.com/MikesCodingCreations/Portfolio3/blob/main/assets/menu_screen1.png)
![Mockup of player board / game start page](https://github.com/MikesCodingCreations/Portfolio3/blob/main/assets/player_gameboard1.png)

## Game Rules
1. The game board is a square grid where you and the computer place battleships
2. The goal is to sink all of the opponent's battleships before they sink yours
3. Each battleship occupies multiple adjacent cells either horizontally (H) or vertically (V)
4. Players take turns attacking the opponent's board by guessing positions
5. If a player's attack hits a battleship, it is a hit
6. Otherwise, it is a miss
7. The game continues until all of one player's battleships are sunk
8. The player who sinks all opponent battleships first wins the game

## Installation
1. Ensure you have Python 3.x installed on your system
2. Clone this repository or download the ZIP file and extract it to your desired location
3. Alternatively, you may access the game via the deployed link on Heroku/Github

## Usage
1. Open a terminal or command prompt
2. Navigate to the directory where the game files are located
3. Run the following command to start the game:
   ```shell
   python run.py

## Testing 

* Link works / Can reach deployed site
- Expetected: 
  - The game should open via the deployed Heroku link
- Tested by:
  - Clicking on the deployed link: https://mikes-battleship-game.herokuapp.com/
- Works? Yes
- Any known issues? No

* Run Program starts the python game/app
- Expetected: 
  - The game should run / the welcome message and menu options are displayed
- Tested by:
  - Clicking on the 'run program' button. Reviewing all necessary content is showing
- Works? Yes
- Any known issues? No

* Each menu option works
- Expetected: 
  - Each of the three menu options work
  - Option 1: selecting this should display the menu/rules
  - Option 2: selecting this should start the game
  - Option 3: selecting this should allow you to quit the game
- Tested by:
  - Selecting each of the options 1, 2 and 3. The menu displays, the game starts and the game quits
- Works? Yes
- Any known issues? No

* User is able to chose their board size from 4 - 10
- Expetected: 
  - User should be able to chose the size of their board from 4x4 upto 10x10
- Tested by:
  - Selected each option, 4x4, 5x5 etc up to 10x10
- Works? Yes
- Any known issues? No

* Chose how many ships are being placed/used in the game
- Expetected: 
  - User should be able to chose upto 10 ships to place on the board
- Tested by:
  - Chosing where each ship goes on the board. Tried placing less ships, does not work. Tried placing more ships also does not work. Right number of ships can be placed when selected.
- Works? Yes
- Any known issues? No

* User has the positbility of loosing or winning
- Expetected: 
  - User should be able to play a game of their chosing (board/ship size) and have the posibility of winning or losing depending on their choices
- Tested by:
  - Tried on a small (4x4) and large (10x10) board
  - User is able to successfully play a game and either win or loose depending on their choices
- Works? Yes
- Any known issues? No

* Restart/Quit game
- Expetected: 
  - User should be able quit the game and start a new one.
- Tested by:
  - Q is typed and the game is quit.
- Works? Yes
- Any known issues? No

## Bugs
Identified Bugs
- N/A
  - No bugs found.
Solved: N/A

### Unfixed Bugs
N/A - All known bugs were fixed.

### Validator Testing 

- PEP 8 Validator
  - No significant bugs or errors found.

## Deployment
- The site was deployed to Heroku via my GitHub link.

# The live link can be found here:
https://mikes-battleship-game.herokuapp.com/

## Contributing
Contributions to Mike's Battleship Game are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request on the GitHub repository.

## License 
Feel free to customize and add more sections as needed to suit your specific requirements.