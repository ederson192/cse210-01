def main ():
    #Main function that includes all functions 
    
    board = create_board() 
   
    global current_player
    current_player = "X" #X is always the first player
    
    while not (winner(board) or tie(board)): #In case there is not a winner or a tie, it repeats
        display_board(board)
        play(current_player,board)
        flip_player() 
   
    
    print("Good game. Thanks for playing!") 
    
    
def create_board():
    #Funcition that creates the board
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"] 
    return board

def display_board(board): 
    #Function to display the board
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()
    
def play (player, board):
    #Function that allows the user to choose position
   position = int(input(f"{player}'s turn to choose a square (1-9): "))
   board[position-1] = player
  

def winner(board):
    #Function to check if there's a winner
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def tie (board):
    #Function to check if there's a tie  (I literally used help here)
   for i in range(9):
       if board[i] != "x" and board[i] != "o":
            return False
   return True
    
def flip_player():
    #Function to change players
  global current_player
  # If the current player was X, make it O
  if current_player == "X":
    current_player = "O"
  # Or if the current player was O, make it X
  elif current_player == "O":
    current_player = "X"
  
  
if __name__ == "__main__": #Call main function to start the game 
    main()