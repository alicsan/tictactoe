#-----------------BASIC TIC TAC TOE GAME -----------------------
#Things we are going to need in order to build our  game:

#-> A board
#-> Display Board
#-> Play Game
#-> Check win
#-> Check tie
#-> Flip player
#-> Check rows
#-> Check columns
#-> Check diagonals
#-> Handle Turn



#----------- Global Variables ----------

#gameboard
board = ['-','-','-',
        '-','-','-',
        '-','-','-',]
#if game is still going
game_still_going = True

winner = None

#whose turn is it, it will flip between X and O
current_player = "X"

#-----------  ----------


def display_board():
    #painting the board
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def handle_turn():
    
    #define the variable
    global current_player
    
    print(current_player +"'s turn.")

    #input prints what's inside and collects the data(?) equals to scanner in java but easier
    position = input('Choose a position from one to nine: ')
    
    valid = False
    #we create a loop to check that the position entered is correct
    #also we check that the position choosen hasn't been taken
    while not valid:

        while position not in ['1','2','3','4','5','6','7','8','9']:
            position = input('Choose a position from one to nine: ')

        #we cast it to int and rest one in order to match the position inside the list
        position = int(position)-1

        #checking that the position is empty and painting it
        if board[position] == "-":
            valid = True
            board[position]=current_player
        else:
            print("You can't go there. Try again.")


        #we assign the x into the position we have previously selected
           
    display_board()



def flip_player():

    #defining variables
    global current_player

    #flippling players
    if current_player == "X":
       current_player = "O"
       
    elif current_player == "O":
        current_player = "X"

def check_rows():

    #set up global variables
    global game_still_going

    #checking row values
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    
    #exit game 
    if row_1 or row_2 or row_3:
        game_still_going = False
    
    #return winner   
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]    


def check_columns():
   
    #set up global variables
    global game_still_going
   
    #checking row values
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
   
    #exit game
    if column_1 or column_2 or column_3:
        game_still_going = False
   
    #return winner   
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2] 


def check_diagonals():
   
    #set up global variables
    global game_still_going
   
    #checking row values
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
   
    #exit game
    if diagonal_1 or diagonal_2:
        game_still_going = False
   
    #return winner   
    if diagonal_1:
        return board[4]
    elif diagonal_2:
        return board[4]
 


def check_win():
 
    #access global variable
    global winner
    
    #calling checking methods
    row_winner=check_rows()

    column_winner=check_columns()

    diagonal_winner=check_diagonals()

    if row_winner:
        #there was a win
        winner = row_winner
    elif column_winner:
        #there was a win
        winner = column_winner
    elif diagonal_winner:
        #there was a win
        winner = diagonal_winner
    else:
        #there was no win
        winner = None


def check_tie():
   #define variable
    global game_still_going
   
    if "-" not in board:
        game_still_going=False
   
    check_rows()
    check_columns()
    check_diagonals()


def check_game_over():
    check_win()
    check_tie()



def play_game():
    
    #display initial board
    display_board()

    while game_still_going:
        
        handle_turn()
        check_game_over()
        flip_player()    

    #the game has ended
    if winner == "X" or winner == "O":
        print("Congratulations: "+winner+".")
    
    elif winner == None:
        print("Tie.")    

play_game()