class InvalidNumberRangeError(Exception):
    pass

class InvalidNumberValueError(Exception):
    pass

class PositionAlreadyTakenError(Exception):
    pass

position_mapper = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2)
}

def read_player_data():
    player_one = input("Player one name: ")
    player_two = input("Player two name: ")
    player_one_sign = input(f"{player_one} would you like to play with 'X' or 'O'? ").upper()

    while player_one_sign not in ["X", "O"]:
        print("Invalid choice, please select 'X' or 'O'")
        player_one_sign = input(f"{player_one} would you like to play with 'X' or 'O'? ").upper()
    player_two_sign = 'O' if player_one_sign == 'X' else 'X'
    return ((player_one, player_one_sign), (player_two, player_two_sign))

def print_board_numeration():
    print("This is the numeration of the board:")
    print("| 1 | 2 | 3 |")
    print("| 4 | 5 | 6 |")
    print("| 7 | 8 | 9 |")

def print_game_board(board: list[list[str]]):
    for row in board:
        print("| " + " | ".join(row) +  " |")

def check_position(position: int, board: list[list[str]]):
    try:
        position = int(position)
    except ValueError:
        raise InvalidNumberValueError

    if position < 1 or position > 9:
        raise InvalidNumberRangeError

    row_index, col_index = position_mapper[position]
    if board[row_index][col_index] != ' ':
        raise PositionAlreadyTakenError
    return (row_index, col_index)

def is_row_winner(board: list[list[str]], current_sign: str) -> bool:
    for row in board:
        if row.count(current_sign) == 3:
            return True
    return False

def is_col_winner(board: list[list[str]], current_sign: str) -> bool:
    for col_index in range(len(board)):
        col_count = 0
        for row_index in range(len(board)):
            if board[row_index][col_index] == current_sign:
                col_count += 1
        if col_count == 3:
            return True
    return False

def is_main_diagonal(board: list[list[str]], current_sign: str) -> bool:
    count = 0
    for row_index in range(len(board)):
        if board[row_index][row_index] == current_sign:
            count += 1
    if count == 3:
        return True
    return False

def is_opposite_diagonal(board: list[list[str]], current_sign: str) -> bool:
    count = 0
    for index in range(len(board)):
        if board[index][len(board) -1 - index] == current_sign:
            count += 1
    if count == 3:
        return True
    return False

def is_diagonal_winner(board: list[list[str]], current_sign: str) -> bool:
    if is_main_diagonal(board,current_sign):
        return True
    if is_opposite_diagonal(board, current_sign):
        return True
    return False

def is_winner(board: list[list[str]], current_sign: str) -> bool:
    is_row = is_row_winner(board, current_sign)
    is_col = is_col_winner(board, current_sign)
    is_diagonal = is_diagonal_winner(board, current_sign)
    if is_row or is_col or is_diagonal:
        return True
    return False

board = [[' ', ' ', ' '] for _ in range(3)]

player_one_data, player_two_data = read_player_data()
print_board_numeration()
print(f"{player_one_data[0]} starts first!")

turns = 1

while True:
    current_player_data, current_player_sign = player_one_data if turns % 2 != 0 else player_two_data
    position = int(input(f"{current_player_data} select a position between [1-9]: "))

    try:
        row_index, col_index = check_position(position, board)
    except (InvalidNumberValueError, InvalidNumberRangeError):
        print(f"Please enter a number between 1 and 9.")
        continue
    except PositionAlreadyTakenError:
        print(f"Please select an empty position")
        continue
    else:
        board[row_index][col_index] = current_player_sign
        print_game_board(board)
        turns += 1

        if turns >= 5 and is_winner(board, current_player_sign):
            print(f"{current_player_data} WON!!!")
            break

        if turns == 10:
            print(f"DRAW!!!")
            print(f"No winner in this game.")
            break

























