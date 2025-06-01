size = 5

matrix = []
position = []

targets = 0

for row in range(size):
    matrix.append(input().split())
    for column in range(size):
        if matrix[row][column] == "A":
            position = [row, column]
        elif matrix[row][column] == "x":
            targets += 1

possible_moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

targets_hit = []

for _ in range(int(input())):
    command = input().split()

    if command[0] == "shoot":
        row = position[0] + possible_moves[command[1]][0]
        column = position[1] + possible_moves[command[1]][1]
        while 0 <= row < size and 0 <= column < size:
            if matrix[row][column] == "x":
                matrix[row][column] = "."
                targets -= 1
                targets_hit.append([row, column])
                break

            row += possible_moves[command[1]][0]
            column += possible_moves[command[1]][1]

        if targets == 0:
            print(f"Training completed! All {len(targets_hit)} targets hit.")
            break

    elif command[0] == "move":
        row = position[0] + possible_moves[command[1]][0] * int(command[2])
        column = position[1] + possible_moves[command[1]][1] * int(command[2])

        if 0 <= row < size and 0 <= column < size and matrix[row][column] == ".":
            matrix[row][column] = "A"
            matrix[position[0]][position[1]] = "."
            position = [row, column]

if targets > 0:
    print(f"Training not completed! {targets} targets left.")

[print(data) for data in targets_hit]






