class InvalidColumnError(Exception):
    pass

class ColumnFullError(Exception):
    pass

slots_to_win = 4

def create_matrix(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]

def validate_column_choice(column_n, col_count):
    if not (0 <= column_n <= col_count):
        raise InvalidColumnError

def apply_player_choice(mtrx, col_selected, player_number):
    for row_check in range(len(mtrx) - 1, -1, -1):
        if mtrx[row_check][col_selected] == 0:
            mtrx[row_check][col_selected] = player_number
            return row_check, col_selected
    raise ColumnFullError

def print_matrix(mtrx):
    for line in mtrx:
        print(line)

def has_won(mtrx, rows, cols, player_number, slots_required = slots_to_win):
    return any([
        is_main_diagonal_winner(mtrx, rows, cols, player_number, slots_required),
        is_anti_diagonal_winner(mtrx, rows, cols, player_number, slots_required),
        is_vertical_winner(mtrx, rows, cols, player_number, slots_required),
        is_horizontal_winner(mtrx, rows, cols, player_number, slots_required)
    ])

def is_main_diagonal_winner(mtrx, rows, cols, player_number, slots_required):
    slots_filled = 1
    for index in range(1, slots_required):
        if is_player_number_on_slot(mtrx, rows - index, cols + index, player_number):
            slots_filled += 1
        else:
            break

    for index in range(1, slots_required):
        if is_player_number_on_slot(mtrx, rows + index, cols - index, player_number):
            slots_filled += 1
        else:
            break

    return slots_filled >= slots_required

def is_anti_diagonal_winner(mtrx, rows, cols, player_number, slots_required):
    slots_filled = 1
    for index in range(1, slots_required):
        if is_player_number_on_slot(mtrx, rows - index, cols - index, player_number):
            slots_filled += 1
        else:
            break

    for index in range(1, slots_required):
        if is_player_number_on_slot(mtrx, rows + index, cols + index, player_number):
            slots_filled += 1
        else:
            break

    return slots_filled >= slots_required

def is_horizontal_winner(mtrx, rows, cols, player_number, slots_required):
    slots_filled = 1
    for index in range(1, slots_required):
        if is_player_number_on_slot(mtrx, rows, cols + index, player_number):
            slots_filled += 1
        else:
            break

    for index in range(1, slots_required):
        if is_player_number_on_slot(mtrx, rows, cols - index, player_number):
            slots_filled += 1
        else:
            break

    return slots_filled >= slots_required


def is_vertical_winner(mtrx, rows, cols, player_number, slots_required):
    return all(is_player_number_on_slot(mtrx, rows + index, cols, player_number) for index in range(slots_required))

def is_player_number_on_slot(mtrx, rows, cols, player_number):
    try:
        return mtrx[rows][cols] == player_number
    except IndexError:
        return False


rows_count = 6
cols_count = 7

matrix = create_matrix(rows_count, cols_count)

player_num = 1
counter = 0

while True:
    player_num = 2 if player_num % 2 == 0 else 1
    try:
        column_num = int(input(f"Player {player_num}, please choose a column: ")) - 1
        validate_column_choice(column_num, cols_count - 1)
        row, col = apply_player_choice(matrix, column_num, player_num)
        print_matrix(matrix)

        if has_won(matrix, row, col, player_num):
            print(f"The winner is player {player_num}!!!")
            break

        counter += 1

        if counter == rows_count * cols_count:
            print(f"DRAW! No more available moves left on board.")
            break

    except InvalidColumnError:
        print(f"Invalid Number. Please select a number between 1 and {cols_count}!")
    except ColumnFullError:
        print(f"The column is full! Please select another!")
    except ValueError:
        print(f"Input is not a digit, please enter a valid number!")

    player_num += 1






















