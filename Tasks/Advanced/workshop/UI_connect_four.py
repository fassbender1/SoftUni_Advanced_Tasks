import tkinter as tk
from tkinter import messagebox

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

def update_ui(labels, row, col, player_num):
    player_color = "red" if player_num == 1 else "blue"
    labels[row][col].config(bg=player_color)

def reset_game(mtrx, label):
    for r in range(len(mtrx)):
        for c in range(len(mtrx[0])):
            mtrx[r][c] = 0
            label[r][c].config(bg="white")

def handle_column_click(mtrx, label, col_num, player_number, counter, row_c, col_c, slots):
    try:
        validate_column_choice(col_num, col_c - 1)
        row, col = apply_player_choice(mtrx, col_num, player_number)
        update_ui(label, row, col, player_number)
        if has_won(mtrx, row, col, player_number):
            messagebox.showinfo("GAME OVER!", f"The winner is player {player_number}")
            reset_game(mtrx, label)
            return 1, 0

        counter += 1
        if counter == row_c * col_c:
            messagebox.showinfo("GAME OVER!", "The game is a DRAW!")
            reset_game(mtrx, label)
            return 1,0

        return 2 if player_number == 1 else 1, counter
    except ColumnFullError:
        messagebox.showerror("The column is full! Please select another!")
    return player_number, counter


def create_user_interface(root, rows, cols, slots):
    matrix = create_matrix(rows, cols)
    labels = [[tk.Label(root, text=" ", bg="white", relief="solid", width=7, height=4)
               for _ in range(cols)] for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            labels[r][c].grid(row=r+1, column=c)

    game_state = {
        "player_num": 1,
        "counter": 0
    }

    def on_click(column_num, state):
        state["player_num"], state["counter"] = handle_column_click(
            matrix, labels, column_num, state["player_num"], state["counter"], rows, cols, slots
        )

    buttons = [tk.Button(root,
                         text="🡇",
                         width=6,
                         height=1,
                         bg="green",
                         command=lambda col_idx=col: on_click(col_idx, game_state)
                         ) for col in range(cols)]

    for col_index, button in enumerate(buttons):
        button.grid(row=0, column=col_index)


def start_game():
    root = tk.Tk()
    root.title("Connect Four")
    slots_to_win = 4
    rows_count = 6
    cols_count = 7
    create_user_interface(root, rows_count, cols_count, slots_to_win)
    root.mainloop()

if __name__ == "__main__":
    start_game()




















