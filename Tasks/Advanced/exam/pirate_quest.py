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

size = int(input())
matrix = []
total_treasures = 0
ship_position = None

for row in range(size):
    row_data = list(input())
    if "S" in row_data:
        ship_position = (row, row_data.index("S"))
    for el in row_data:
        if el == "*":
            total_treasures += 1
    matrix.append(row_data)

durability = 100
has_charm_been_used = False
has_crashed = False
command = input()

while command != "stop":
    current_row, current_col = ship_position
    next_row, next_col = calculate_next_place(current_row, current_col, command, size)
    next_element = matrix[next_row][next_col]
    matrix[current_row][current_col] = "."
    matrix[next_row][next_col] = "S"
    ship_position = (next_row, next_col)

    if next_element == "*":
        total_treasures -= 1
        if total_treasures <= 0:
            print(f"Yo-ho-ho! All treasure chests collected!")
            break

    if next_element == "C" and not has_charm_been_used:
        durability += 25
        if durability > 100:
            durability = 100
        has_charm_been_used = True

    if next_element == "M":
        durability -= 25
        if durability <= 0:
            print(f"Shipwreck! Last known coordinates ({next_row}, {next_col})")
            has_crashed = True
            break


    command = input()

if total_treasures > 0 and not has_crashed:
    print(f"Retreat! Some treasures remain unclaimed.")

print(f"Ship Durability: {durability}")

if total_treasures > 0:
    print(f"Unclaimed chests: {total_treasures}")

for row in matrix:
    print(''.join(row))





















