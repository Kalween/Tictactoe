Tic Tac Toe Game
This is a simple implementation of the Tic Tac Toe game in Python. The game allows two players to take turns marking spaces on the game board with their respective markers (X and O).

How to Run the Game
Clone the repository to your local machine.
Open a terminal window and navigate to the directory where the repository is located.
Run the following command to start the game:

  python tictactoe.py
  
Game Play
The game board is represented by a 3x3 grid of numbers from 1 to 9.
Players take turns marking spaces on the game board with their respective markers (X and O).
The first player to get three of their markers in a row (horizontally, vertically, or diagonally) wins the game.
If all spaces on the game board are marked and no player has won, the game is a draw.
Code Overview
The code for the Tic Tac Toe game consists of two functions: quest and updateboard.

The quest function allows players to place their markers on the game board by entering a number from 1 to 9.

The updateboard function displays the current state of the game board, showing the positions of the markers.

The game is played in a while loop, which continues until one of the players wins or the game is a draw. The loop alternates between the two players, allowing each player to place their marker on the game board.

The game board is represented as a list of numbers, with each number representing a space on the game board. When a player places their marker on a space, the corresponding number in the list is replaced with the player's marker.
