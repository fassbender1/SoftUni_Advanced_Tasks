presents = int(input())
size = int(input())

matrix = []
Santa_position = []
nice_kids = []
nice_kids_with_gifts = 0

for row in range(size):
    matrix.append(input().split())
    for column in range(size):
        if matrix[row][column] == "S":
            Santa_position = [row, column]
        elif matrix[row][column] == "V":
            nice_kids.append([row, column])

possible_moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while presents > 0:
    command = input()
    if command == "Christmas morning":
        break

    row, column = Santa_position[0] + possible_moves[command][0], Santa_position[1] + possible_moves[command][1]

    if 0 <= row < size and 0 <= column < size:
        if matrix[row][column] == "V":
            presents -= 1
            nice_kids_with_gifts += 1
            matrix[row][column] = "-"
        elif matrix[row][column] == "C":
            for move in possible_moves.values():
                next_row, next_column = row + move[0], column + move[1]
                if matrix[next_row][next_column] in "VX" and presents > 0:
                    presents -= 1
                    if matrix[next_row][next_column] == "V":
                        nice_kids_with_gifts += 1
                    matrix[next_row][next_column] = "-"

        matrix[Santa_position[0]][Santa_position[1]] = "-"
        Santa_position = [row, column]
        matrix[row][column] = "S"

if presents < 1 and len(nice_kids) - nice_kids_with_gifts > 0:
    print(f"Santa ran out of presents!")

[print(*line) for line in matrix]

if len(nice_kids) - nice_kids_with_gifts > 0:
    print(f"No presents for {len(nice_kids) - nice_kids_with_gifts} nice kid/s.")
else:
    print(f"Good job, Santa! {len(nice_kids)} happy nice kid/s.")












