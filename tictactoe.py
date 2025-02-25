import tkinter as tk
from tkinter import messagebox

# creates an empty window where the board will be displayed
display = tk.Tk()
display.title("Tic Tac Toe")

# Initialize variables
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
human = "X"
computer = "O"
# the human player makes the first move
current_player = human

def new_game():
    global board, current_player

    # Clear the board
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    # Destroy the message label if it exists
    existing_message_label = display.grid_slaves(row=5, column=1)
    if existing_message_label:
        existing_message_label[0].destroy()

    for i in range(3):
        for j in range(3):
            # create the button that represents a cell in the board
            cellbutton = tk.Button(display, 
                                   text="", # initially each cell will be empty
                                   font=("Arial", 60), # font and font size
                                   height=3, width=6, # height and width of each cell
                                   # the function to be called when the button is clicked
                                   # this means that when a cell is clicked, we call the handle_click function
                                   command=lambda row=i, col=j: handle_click(row, col)) # lambda passes i and j as arguments to handle_click
            # the cells will be put in a grid
            cellbutton.grid(row=i, column=j, sticky="nsew")
            # display a button below the board to restart the game
            replay_button = tk.Button(display, 
                          text="Restart",
                          font=("Arial", 30),
                          command=new_game)
            replay_button.grid(row=4, column=1)
    
    # Reset the current player to human
    current_player = human



# call the function to actually create the board
new_game()

def handle_click(row, col):
    global current_player

    # Check if the game is still ongoing
    if evaluateBoard() == 0:
        # check if the cell is empty
        if board[row][col] == 0:
            # if the current player is human, then place the human symbol "X" on cell
            if current_player == human:
                board[row][col] = human
                # gets the button the player is trying to click on
                button1 = display.grid_slaves(row=row, column=col)[0]
                # actually places the right symbol on the cell
                button1.config(text=board[row][col])
                # switch the player to computer
                current_player = computer

            # after a move, check if the game is over (this means either a win or tie)
            check_gameover()

            # If the game is still ongoing and it's the computer's turn, make its move
            if current_player == computer and evaluateBoard() == 0:
                move = findBestMove()
                # get the row index for the best move
                r = move[0]
                # get the col index for the best move
                c = move[1]
                board[r][c] = computer
                # gets the button the player is trying to click on
                button2 = display.grid_slaves(row=r, column=c)[0]
                # actually places the right symbol on the cell
                button2.config(text=board[r][c])
                # switch the player back to human
                current_player = human



# checks if the game is over and displays the appropriate message
def check_gameover():
    winner = None
    score = evaluateBoard()

    # If maximizer/human has won the game return evaluated score  
    if (score == 10) :  
        winner = human 
  
    # If minimizer/computer has won the game return score
    if (score == -10) : 
        winner = computer 
  
    # If there are no more moves and no winner then  
    # it is a tie  
    if (anyEmptyCells(board) == False) : 
        winner = "tie"

    if winner is not None:
        if winner == "tie":
            message = "IT'S A TIE!"
        else:
            message = f"Player {winner} wins!"

        # Create a new label for the message
        message_label = tk.Label(display, text=message, font=("Arial", 14))
        message_label.grid(row=5, column=1) 

# assign a score of 10 is the maximizer has won the game,
# a score of -10 if the minimizer has won
# and 0 if none of them have won
def evaluateBoard():
    # checking rows for a win
    for i in range(3):
        # check if the three elements in a row are the same
        if board[i][0] == board[i][1] == board[i][2]:
            # check if the winner is human
            if board[i][0] == human:
                # since the winner is the maximizer, return 10
                return 10
            # check if the winner is computer
            elif board[i][0] == computer:
                # return -10 since the winner is the minimizer
                return -10
    
    # checking columns for a win
    for j in range(3):
        # check if the three elements in a column are the same
        if board[0][j] == board[1][j] == board[2][j]:
            # check if the winner is human
            if board[0][j] == human:
                # since the winner is the maximizer, return 10
                return 10
            # check if the winner is computer
            elif board[0][j] == computer:
                # return -10 since the winner is the minimizer
                return -10

    # checking diagonal for a win
    if board[0][0] == board[1][1] == board[2][2]:
        # check if the winner is human
            if board[0][0] == human:
                # since the winner is the maximizer, return 10
                return 10
            # check if the winner is computer
            elif board[0][0] == computer:
                # return -10 since the winner is the minimizer
                return -10
    # checking antidiagonal for a win
    if board[2][0] == board[1][1] == board[0][2]:
        # check if the winner is human
            if board[2][0] == human:
                # since the winner is the maximizer, return 10
                return 10
            # check if the winner is computer
            elif board[2][0] == computer:
                # return -10 since the winner is the minimizer
                return -10
            
    # if none of them have won the game yet, return 0
    return 0

# the minimax function
def minimax(depth, isMax):
    score = evaluateBoard()


    if score == 10:
        return score - depth  # Adjust the score based on depth
    if score == -10:
        return score + depth  # Adjust the score based on depth
    if not anyEmptyCells(board):
        return 0

    # If this maximizer's move 
    if isMax:
        best = -1000
        bestMove = (-1, -1)

        # go through each cell
        for i in range(3):
            for j in range(3):
                # check if the cell is empty
                if board[i][j] == 0:
                    # if empty, place "X" for the maximizer
                    board[i][j] = human
                    # recursively call teh function for the new depth
                    moveVal = minimax(depth + 1, not isMax)
                    # undo the move
                    board[i][j] = 0
                    
                    # update best move
                    if moveVal > best:
                        bestMove = (i, j)
                        best = moveVal
        # only return best move when we are done
        return bestMove if depth == 0 else best

    # for the minimizer
    else:
        best = 1000
        bestMove = (-1, -1)

        # go through each cell
        for i in range(3):
            for j in range(3):
                # check if cell is empty
                if board[i][j] == 0:
                    # if empty, place "O" for the minimizer
                    board[i][j] = computer
                    # recursively call the function for new depth
                    moveVal = minimax(depth + 1, not isMax)
                    # undo the move
                    board[i][j] = 0

                    #update best move
                    if moveVal < best:
                        bestMove = (i, j)
                        best = moveVal

        # only return best move when we are done
        return bestMove if depth == 0 else best

# find the best possible move for a player
def findBestMove():
    return minimax(0, False)

# check if there are any empty cells left
def anyEmptyCells(b):
    # go through each cell in the board
    for i in range(3):
        for j in range(3):
            # check if the cell is empty
            if b[i][j] == 0:
                # if you find an empty cell, return true
                return True
    # if there are no empty cells, return false
    return False



display.mainloop()