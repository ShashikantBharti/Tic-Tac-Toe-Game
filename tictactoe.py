'''
***********************************
    RETURN INITIALIZED BOARD
***********************************
Initialize Board for Tic Tac Toe
Return Type Dictionary
'''
def get_board():
    # Assign each box a number : 1 to 9 
    board = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return board


'''
************************************
        PRINT UPDATED BOARD
************************************
Print Updated Board On screen
Parameter Dictionary
'''
def print_board(board):
    print(f" {board['1']} | {board['2']} | {board['3']}")
    print(f" - + - + - ")
    print(f" {board['4']} | {board['5']} | {board['6']}")
    print(f" - + - + - ")
    print(f" {board['7']} | {board['8']} | {board['9']}")


'''
***********************************
     CHECK IF PLAYER WON
***********************************
@params Board Dictionary
@return String Or Boolean
'''
def is_win(board):
    # Calculate Remainig Moves
    moves_left = [x for x in board.values() if isinstance(x, int)]
    if board['1'] == board['2'] and board['1'] == board['3']: return board['1']+' Won!'
    if board['1'] == board['5'] and board['1'] == board['9']: return board['1']+' Won!'
    if board['1'] == board['4'] and board['1'] == board['7']: return board['1']+' Won!'
    if board['2'] == board['5'] and board['2'] == board['8']: return board['2']+' Won!'
    if board['3'] == board['6'] and board['3'] == board['9']: return board['3']+' Won!'
    if board['3'] == board['5'] and board['3'] == board['7']: return board['3']+' Won!'
    if board['4'] == board['5'] and board['4'] == board['6']: return board['4']+' Won!'
    if board['7'] == board['8'] and board['7'] == board['9']: return board['7']+' Won!'
    # Check all moves completed 
    if len(moves_left) == 0: return 'Draw'
    return False

'''
******************************************
        UPDATE BOARD AT EACH MOVE
******************************************
@params board, player
@return Won Player

'''
def update_board(board, player):
    # List position of box
    positions = list(map(str, list(range(1, 10))))
    # Check if any player won and return that 
    if is_win(board):
        return is_win(board)
    # Play until Draw or Victory
    while True:
        # Print Which player's turn is
        print(f"\n {player}'s turn")
        pos = input('Enter position: ')
        # Check if move is possible for entered position
        if pos not in positions:
            print('=====================\n Position is invalid!\n=====================')
            continue
        # Check if position is already selected by any player   
        if isinstance(board[pos], str):
            print('===========================\n Position already occupied!\n===========================')
            continue
        break
    # Update board
    board[pos] = player
    print_board(board)


'''
**************************************
            SELECT PLAYER 
**************************************
@return selected player
'''
def select_player():
     while True:
        # Select Player
        p = str(input('\n Choose X or O: ')).upper()
        if p == 'X' or p == 'O':
            return p  # Return selected player
        else:
            print('=============\n Wrong Input!\n=============')
            continue

# Start the Game
'''
**************************************
        GAME START FROM HERE
**************************************
@return None

'''
def play():
    # Initialize board
    board = get_board()
    # Get player
    p = select_player()
    print_board(board)
    for i in range(1, 10):
        # Move for Player O
        if p == 'O':
            if update_board(board, p):
                print(f"======================\n        {update_board(board, p)}\n======================")
                return
            p = 'X'
        # Move for Player X
        if p == 'X':
            if update_board(board, p):
                print(f"======================\n        {update_board(board, p)}\n======================")
                return
            p = 'O'

'''
********************************************
    PLAY FUNCTION CALLED TO START GAME
********************************************

'''
play()


