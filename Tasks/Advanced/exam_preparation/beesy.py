moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

def calculate_next_place(current_r_index, current_c_index, current_direction, n):
    row_movement, col_movement = moves[current_direction]
    next_row_index = (current_r_index + row_movement) % n
    next_col_index = (current_c_index + col_movement) % n
    return next_row_index, next_col_index

def print_matrix(mtrx):
    for row in mtrx:
        print(''.join(row))


size = int(input())
matrix = []

bee_position = None
has_restored_eng = False
initial_energy = 15
collected_nectar = 0


for i in range(size):
    row_data = list(input())
    if "B" in row_data:
        bee_position = (i, row_data.index("B"))
    matrix.append(row_data)

direction = input()

while True:
    current_row, current_col = bee_position
    next_row, next_col = calculate_next_place(current_row, current_col, direction, size)
    next_element = matrix[next_row][next_col]
    matrix[current_row][current_col] = "-"
    matrix[next_row][next_col] = "B"
    bee_position = (next_row, next_col)
    initial_energy -= 1

    if next_element.isdigit():
        collected_nectar += int(next_element)

    if next_element == "H":
        if collected_nectar >= 30:
            print(f"Great job, Beesy! The hive is full. Energy left: {initial_energy}")
        else:
            print(f"Beesy did not manage to collect enough nectar.")
        break

    if initial_energy <= 0 and collected_nectar < 30:
        print(f"This is the end! Beesy ran out of energy.")
        break
    if initial_energy <= 0 and collected_nectar >= 30 and not has_restored_eng:
        initial_energy = collected_nectar - 30
        collected_nectar = 30
        has_restored_eng = True
    if initial_energy <= 0:
        print(f"This is the end! Beesy ran out of energy.")
        break

    direction = input()

print_matrix(matrix)
















