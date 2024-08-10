'''
What you will create
Create a TicTacToe game in python, where two users can play together.



tic-tac-toe


Instructions
The game is played on a grid that’s 3 squares by 3 squares.
Players take turns putting their marks (O or X) in empty squares.
The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.
When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.


Hint
To do this project, you basically need to create four functions:

display_board() – To display the Tic Tac Toe board (GUI).
player_input(player) – To get the position from the player.
check_win() – To check whether there is a winner or not.
play() – The main function, which calls all the functions created above.
Note: The 4 functions above are just an example. You can implement many more helper functions or choose a completely different appoach if you want.



Tips : Consider the following:
What functionality will need to accur every turn to make this program work?
After contemplating the question above, think about splitting your code into smaller pieces (functions).
Remember to follow the single responsibility principle! each function should do one thing and do it well!



'''
import random 

# Function to display the current state of the Tic Tac Toe board
def display_board(board_values):
    print(f"""
          |{board_values[0][0]}|{board_values[0][1]}|{board_values[0][2]}|
          |{board_values[1][0]}|{board_values[1][1]}|{board_values[1][2]}|
          |{board_values[2][0]}|{board_values[2][1]}|{board_values[2][2]}|
          """)

# Function to get input from the player
def player_input(board_values):
    while True:  # Loop until valid input is provided
        try:
            pos_str = input('Enter the position of your move in the following format: "0 0" for the upper left, "0 2" for the upper right: ')
            pos_tpl = tuple(map(int, pos_str.split()))  # Convert the input string to a tuple of integers

            # Check if the input contains exactly two numbers
            if len(pos_tpl) != 2:
                raise ValueError("Please enter exactly two numbers separated by a space.")

            # Check if the input numbers are within the valid range (0-2)
            if not (0 <= pos_tpl[0] <= 2) or not (0 <= pos_tpl[1] <= 2):
                raise ValueError("Row and column numbers must be between 0 and 2.")

            # Check if the chosen spot on the board is empty
            if board_values[pos_tpl[0]][pos_tpl[1]] != " ":
                raise ValueError("That spot is already taken. Please choose another one.")

            # Place the player's mark ('O') on the board
            board_values[pos_tpl[0]][pos_tpl[1]] = 'O'
            break 

        except ValueError as ve:
            print(f"Invalid input: {ve}. Please try again.")

        except IndexError:
            print("Invalid position! Make sure to enter numbers within the range 0-2.")
        
        except Exception as e:
            print(f"Unexpected error: {e}. Please try again.")

# Function to check if there is a winner
def check_win(board_values):
    # Check all rows for a win
    for row in board_values:
        if row[0] == row[1] == row[2] != " ":
            return row[0]

    # Check all columns for a win
    for col in range(3):
        if board_values[0][col] == board_values[1][col] == board_values[2][col] != " ":
            return board_values[0][col]

    # Check the diagonals for a win
    if board_values[0][0] == board_values[1][1] == board_values[2][2] != " ":
        return board_values[0][0]
    if board_values[0][2] == board_values[1][1] == board_values[2][0] != " ":
        return board_values[0][2]

    # Return None if there is no winner yet
    return None

# Function to make a random move for the computer ('X')
def PC_moove(board_values):
    # Create a list of all empty spots on the board
    empty_spots = [(i, j) for i in range(3) for j in range(3) if board_values[i][j] == " "]
    
    if not empty_spots:
        return board_values  # If no empty spots are left, return the board as is
    
    # Choose a random empty spot and place an 'X' there
    move = random.choice(empty_spots)
    board_values[move[0]][move[1]] = "X"
    
    return board_values

# Main function to control the game flow
def play():
    # Initialize the board as a 3x3 grid of empty spaces
    board_values = [[" " for _ in range(3)] for _ in range(3)]
    
    # Continue the game until there's a winner or the board is full
    while True:
        print('Computer plays for "X" and you play for "O".')
        
        # Computer makes its move
        PC_moove(board_values)
        display_board(board_values)  # Display the board after the computer's move
        
        # Check if the computer won
        if check_win(board_values):
            print(f'{check_win(board_values)} won! Congratulations.')
            break
        
        # Check if the board is full and it's a tie
        if all(cell != " " for row in board_values for cell in row):
            print('It\'s a tie!')
            break
        
        # Player makes their move
        player_input(board_values)
        
        # Check if the player won
        if check_win(board_values):
            display_board(board_values)
            print(f'{check_win(board_values)} won! Congratulations.')
            break
        
        # Check again if the board is full and it's a tie
        if all(cell != " " for row in board_values for cell in row):
            display_board(board_values)
            print('It\'s a tie!')
            break

# Start the game
play()

