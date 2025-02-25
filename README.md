# Tic-Tac-Toe Game with an AI Player

This is a tic-tac-toe game where a human player can play against the computer, and the computer should be able to either win or tie the game every single time.

## Overview
The tic-tac-toe game is strategic and sequential, and since there is no chance involved and the players make decisions one after the other, it is not too hard to 
map out all of the possible moves for both players in the game.

Since a game of tic-tac-toe ends when a player positions 3 of their symbols one after another horizontally, vertically, or diagonally, and both players take turns to make a move, 
the smallest number of possible moves to win a game is 5 (3 moves for the winner, and 2 moves for the loser). The largest number of possible moves for a game to end is 9, 
since that means that all of the cells in a board have been filled out. So a game can end in 5, 6, 7, 8, or 9 moves.

if we want to calculate the total board configurations for a game that is won in 5 moves, we have to keep in mind that there are 8 possible ways to place 3 symbols ("X" or "O") 
one after the other: 3 ways to put them in a row, 3 ways to put them in a column, and 2 ways to put them diagonally. Since the order in which the symbols are placed matters, 
there are 8 ∗ 3! = 48 ways in which the winner can place its 3 symbols one after the other on the board. On the other hand, the loser of the game can place its 2 symbols 
on the remaining 6 cells, and since the order in this case also matters, we can calculate that there are $_6P_2$ = 30 ways for the loser to place its symbols on the board. 

We can use a similar logic to calculate the number of possible board configurations for games that end in 6, 7, 8, or 9 moves, and the number that we get at the end should be 255,168 total configurations.

When building a tic-tac-toe game, we could try to code all of these possible configurations and try to figure out the best path for a player to follow, but since the number of total 
board configurations is so great, it would be extremely hard to do this, so I am using the minimax algorithm here.

In the code, "X" represents the maximizing player, while "O" represents the minimizing player, in this case the computer. The function minimax calls itself recursively 
again and again until it reaches an end-of-the-game state (which in my code is represented by a depth of 0), and as it keeps generating new possible states, 
it assigns a score to each state as described above. A win for the maximizing player is assigned a score of +10, a win for the minimizing player is assigned a score of −10, 
while a draw is assigned a score of 0.

## How to run the game?

Simply run the python file and a new window should immediately show up with 9 white squares representing each of the squares where you can put a symbol in to play the game. You can
click on any of these squares to place an "X". The game will end either in a draw or in a win for one of the players, but since the computer is programmed to try to win or draw the game,
it should always end either in a draw or a win for the computer.
