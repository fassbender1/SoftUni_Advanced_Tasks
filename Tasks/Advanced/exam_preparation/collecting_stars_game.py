size = int(input())
matrix = []
player_position = []
stars_collected = 2

for row in range(size):
    row_data = input().split()
    matrix.append(row_data)
    if "P" in row_data:
        player_position = [row, row_data.index("P")]
        matrix[row][row_data.index("P")] = "."

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
    "starting_position": (0, 0)
}

while 0 < stars_collected < 10:
    direction = input()
    next_row = player_position[0] + moves[direction][0]
    next_col = player_position[1] + moves[direction][1]

    if not(0 <= next_row < size and 0 <= next_col < size):
        next_row, next_col = moves["starting_position"]

    if matrix[next_row][next_col] == "*":
        stars_collected += 1
        matrix[next_row][next_col] = "."
    elif matrix[next_row][next_col] == "#":
        stars_collected -= 1
        continue

    player_position = [next_row, next_col]

if stars_collected == 10:
    print(f"You won! You have collected 10 stars.")
else:
    print(f"Game over! You are out of any stars.")

print(f"Your final position is [{player_position[0]}, {player_position[1]}]")

matrix[player_position[0]][player_position[1]] = "P"

for row in matrix:
    print(" ".join(row))













