# Mike's Battleship Game

[View the live project here.](https://mikes-battleship-game.herokuapp.com)

## Introduction
- Mike's Battleship Game is a Python console-based application that recreates the classic game of Battleship. The game allows players to strategically place their battleships on a grid and engage in a battle against the computer. It provides an entertaining and engaging experience for users to test their tactical skills and luck.

## Technologies Used
- Python
- JavaScript

## Mockups of game
### Starting Page
![Mockup of starting page](https://github.com/MikesCodingCreations/Portfolio3/blob/main/assets/main_page1.png)

### Menu Screen
![Mockup of menu screen page](https://github.com/MikesCodingCreations/Portfolio3/blob/main/assets/menu_screen1.png)

### Game start
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
3. Run the following command to start the gameusing the command: python run.py

## Testing 
- PEP8 validator service was used to validate the Python app to ensure it complies PEP8 style conventions.

### Link works / Can reach deployed site
- Expetected: 
  - The game should open via the deployed Heroku link.
- Tested by:
  - [Visiting the deployed Heroki link](https://mikes-battleship-game.herokuapp.com/)
- Works:
  - Yes, the user can access the app through the link with no issues.
- Any known issues:
  - No. The app runs via the link.

### Run Program starts the python game/app
- Expetected: 
  - The game should run / the welcome message and menu options should be displayed to the user.
- Tested by:
  - Clicking on the 'run program' button when the app opens in browser. Reviewing all necessary content is showing.
- Works:
  - Yes. The 'run program' button executes and the app runs. All necessary content is displayed to the user.
- Any known issues:
  - No. All content is clear and no information is missing.

### Each menu option works
- Expetected:
  - All three menu options are displayed and user can choose either one.
  - Option 1: selecting this should display the menu/rules
  - Option 2: selecting this should start the game
  - Option 3: selecting this should allow the user to quit the game
- Tested by:
  - Selecting each of the options 1, 2 and 3. The menu displays, the game starts and the game quits upon execution of each option.
- Works:
  - Yes, all the above options work for the end user.
- Any known issues:
  - No known issues with this testing.

### User is able to chose their board size from 4 - 9
- Expetected: 
  - User should be able to chose the size of their board from 4x4 up to 9x9
  - User should not be able to choose a board with fewer than 4 or more than 9 spaces.
- Tested by:
  - Selected each option, 4x4, 5x5 etc up to 9x9
  - Trying to enter a null result (i.e., hitting enter when promted to choose board size, not entering a size) or entering a size < 4 or > 9.
- Works:
  - The user is now able to start the game ONLY if the board size is between 4 and 9 grids. 
  - The user is promted with a message to choose an appropriate size board if entering null, <4 or > 9 grid spaces.
- Any known issues:
  - Previously, users were able to start the game by entering <4 or > 9 spaces. However this has now been altered.
  - No knows issues currently. 

### Chose how many ships are being placed/used in the game
- Expetected: 
  - User should be able to chose up to 9 ships to place on the board.
- Tested by:
  - Trying to select > 9 or < 1 ship. This results in a prompt to the user to choose appropriate ships.
- Works:
  - Yes, this piece of testing now works. Users can successfully begin the app when choosing appropriate number of ships.
- Any known issues:
  - Previously users could choose any amount of ships which would not run the app accordingly. The code has now been altered to ensure users cannot continue to begin the game if their chosen ship size is not between 4 and 9

### User has the positbility of loosing or winning
- Expetected: 
  - User should be able to play a game of their chosing (board/ship size) and have the posibility of winning or losing depending on their choices of where they place the ships.
- Tested by:
  - Tried on a small (4x4) and large (9x9) board and all sizes inbetween.
  - User is able to successfully play a game and either win or loose depending on their choices.
- Works:
  - Successfully works depending on choises.
  - User may win or loose VS the computer.
- Any known issues:
  - No current known issues found.

### Restart/Quit game
- Expetected: 
  - User should be able quit the game and start a new one.
- Tested by:
  - Q is typed and the game able to quit.
- Works:
  - Yes. This option is allowed. First on the menu options users may choose option 3 to quite. Then also when the game beging users may choose to type 'Q' to quit.
- Any known issues:
  - No current known issues.


### Further Testing
- The app was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
- Friends & family were asked to review the site and README to point out any bugs and/or user experience issues.
- Feedback from tutor support and Assessment team taken onboard. 

## Bugs
Identified Bugs
- Blank input (i.e., null choice or 0) or too small/large input (i.e. board piece <4 or > 9) causes game to crash / not function propertly. 
- This bug has now been fixed by implmenting a 'get_valid_input' user validation. This code now only allows users to begin the game if they choose the correct grid/ship size (between 4 and 9).

## Unfixed Bugs
- No known, unfixed bugs.
- Currently users can quite the game at 2 stages: (1) At the menu stage and (2) when the first ship is placed/sunk. However, this could be further improved by adding code to allow user to quit the game before a ship is sunk/placed.

## Validator Testing 
- PEP 8 Validator
  - No significant bugs or errors found. Code runs within PEP8 styling conventions.
  - 1 Improvement could be to reduce length size of certain lines.

## Deployment
The site was deployed firstly via GitHub pages then also through Heroku using the following steps:
- GitHub
  1. Login to GitHub and locate the [Repositoy](https://github.com/MikesCodingCreations/Portfolio3)
  2. At the top of the Repository, click on the 'Settings' button.
      - Alternatively click [HERE](https://github.com/MikesCodingCreations/Portfolio3/settings) to access this step.
  3. Scroll down the page and click on the 'GitHub Pages' section which is located on the left hand side.
  4. Change 'None' to 'Master Branch' under the 'source' option.
  5. Allow the page time to refresh.
  6. Scroll all the way down and click on the published site link found in the 'GutHub pages' section.

- Heroku
  1. Navigate to [Heroku.](www.heroku.com)
  2. Login or create an account.
  3. Click the 'New' icon on the right hand side.
  4. Click 'create new app' in the dropdown.
  5. Create a unique app name and change region to Europe. Click on purple 'Create App' icon.
  6. In the 'Deployment method' click 'Connect to GitHub'.
  7. In the 'search for a repository to connect to' section, type in your repo-name and hit search. Hit search then click connect.
  8. Scholl down to the 'manual deploy' and hit 'diploy branch'
  9. After a few moments, you may scroll up and click the 'open app' button which will redirect you to the deployed app link.


## Content
- All content was created by the developer.
- Information on README example found [here.](https://github.com/Code-Institute-Solutions/SampleREADME/blob/master/README.md)
- ASCII Art text how-to found [here.](https://www.devdungeon.com/content/create-ascii-art-text-banners-python)

## Media
- All images are ownder and created by the developer.

## Acknowledgements
- Tutor support at Code Institute for their continued support.

## Contributing
Contributions to Mike's Battleship Game are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request on the GitHub repository.

## License 
Feel free to customize and add more sections as needed to suit your specific requirements.