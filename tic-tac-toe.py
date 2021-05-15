# Tic-Tac-Toe
# Plays the game of tic-tac-toe against a human opponent
   
# global constants
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9

def display_instruct():
    """Display game instructions."""  
    print(
    """
    Welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.  
    This will be a showdown between your human brain and my silicon processor.  

    You will make your move known by entering a number, 0 - 8.  The number 
    will correspond to the board position as illustrated:
    
                    0 | 1 | 2
                    ---------
                    3 | 4 | 5
                    ---------
                    6 | 7 | 8

    Prepare yourself, human.  The ultimate battle is about to begin. \n
    """
    )

def ask_yes_no(question):
    """Ask a yes or no question."""
    # Set the response to None
    response = None
    # While the response is not either 'y' or 'n'
    while response not in ("y", "n"):
        # Input response from keyboard change input to lower case
        response = input(question).lower()
    # return the response
    return response

def ask_number(question, low, high):
    """Ask for a number within a range."""
    # Set the response to None
    response = None
    # While response is not in the number range between low and high
    while response not in range(low, high):
        # Input response from keyboard ensure value is an integer
        response = int(input(question))
    # return the response
    return response

def pieces():
    """Determine if player or computer goes first."""
    # Ask human player if they wish to go first
    go_first = ask_yes_no("Do you require the first move? (y/n): ")
    # If the human player answers y then
    if go_first == "y":
        print("\nThen take the first move.  You will need it.")
        # Set human olayer to 'X'
        human = X
        # Set computer player to 'O'
        computer = O
    else:
        print("\nYour bravery will be your undoing... I will go first.")
        # Set computer player to 'X'
        computer = X
        # Set human player to 'O'
        human = O
    # return the computer and human player pieces
    return computer, human

def new_board():
    """Create new game board."""
    # Set the board to an empty list
    board = []
    # For each square in the board range (0 to 9)
    for square in range(NUM_SQUARES):
        # Add an empty value
        board.append(EMPTY)
    # return the board
    return board

def display_board(board):
    """Display game board on screen."""
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")

def legal_moves(board):
    """Create list of legal moves."""
    # Create an empty list to hold the legal moves
    moves = []
    # For each square in the board (0-9)
    for square in range(NUM_SQUARES):
        # If the square at the board position is empty
        if board[square] == EMPTY:
            # then add this square as a legal move
            moves.append(square)
    # return the legal moves
    return moves

def winner(board):
    """Determine the game winner."""
    # Data structure to hold winning square combinations
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    
    # For each row in ways to win
    for row in WAYS_TO_WIN:
        # if the positions 0,1,2 in a ways to win row are of the same piece
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            # then declare the winner as that piece
            winner = board[row[0]]
            # return the Winner
            return winner

    # If there are no empty positons but then declare a Tie
    if EMPTY not in board:
        # Return tie
        return TIE

    # Return None if there is either no Winner or Tie
    return None

def human_move(board, human):
    """Get human move."""  
    # Get the possible legal moves
    legal = legal_moves(board)
    # Initialise the move to None
    move = None
    # While the move is not legal
    while move not in legal:
        # Ask the human player for a move
        move = ask_number("Where will you move? (0 - 8):", 0, NUM_SQUARES)
        # If the move is not legal, tell the human player
        if move not in legal:
            print("\nThat square is already occupied, foolish human.  Choose another.\n")
    print("Fine...")
    # Return the move
    return move

def computer_move(board, computer, human):
    """Make computer move."""
    # make a copy to work with since function will be changing list
    board = board[:]
    # the best positions to have, in order
    BEST_MOVES = (2, 6, 4, 0, 8, 1, 3, 5, 7)

    print("I shall take square number", end=" ")
    
    # if computer can win, take that move
    # For every legal move possible
    for move in legal_moves(board):
        # For the local copy of the board set that legal move to the computer player
        board[move] = computer#
        # If this move is a winner
        if winner(board) == computer:
            # then print and return the move
            print(move)
            return move
        # done checking this move, undo it
        board[move] = EMPTY
    
    # if human can win, block that move
    # For every legal move possible
    for move in legal_moves(board):
        # Set the local copy of board to a human player move
        board[move] = human
        # If the human would win for this move
        if winner(board) == human:
            # then take this move, print and return
            print(move)
            return move
        # done checkin this move, undo it
        board[move] = EMPTY

    # since no one can win on next move, pick best open square
    # For every move in possible best moves
    for move in BEST_MOVES:
        # If this move is legal
        if move in legal_moves(board):
            # then print and retur this move
            print(move)
            return move

def next_turn(turn):
    """Switch turns."""
    # Swaps the turn over
    if turn == X:
        return O
    else:
        return X
    
def congrat_winner(the_winner, computer, human):
    """Congratulate the winner."""
    if the_winner != TIE:
        print(the_winner, "won!\n")
    else:
        print("It's a tie!\n")

    if the_winner == computer:
        print("As I predicted, human, I am triumphant once more.  \n" \
              "Proof that computers are superior to humans in all regards.")

    elif the_winner == human:
        print("No, no!  It cannot be!  Somehow you tricked me, human. \n" \
              "But never again!  I, the computer, so swear it!")

    elif the_winner == TIE:
        print("You were most lucky, human, and somehow managed to tie me.  \n" \
              "Celebrate today... for this is the best you will ever achieve.")

def main():
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)

    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)

    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)

# start the program
main()
input("\n\nPress the enter key to quit.")