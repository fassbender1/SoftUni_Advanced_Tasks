size = int(input())

matrix = []
Alice = []

for row in range(size):
    matrix.append(input().split())
    for column in range(size):
        if matrix[row][column] == "A":
            matrix[row][column] = "*"
            Alice = [row, column]


possible_moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
tea_bags_collected = 0

while tea_bags_collected < 10:
    move = possible_moves[input()]
    next_row_position = Alice[0] + move[0]
    next_column_position = Alice[1] + move[1]
    Alice_new_position = [next_row_position, next_column_position]

    if next_row_position < 0 or next_row_position >= size or next_column_position < 0 or next_column_position >= size:
        break

    if matrix[Alice_new_position[0]][Alice_new_position[1]] == "R":
        matrix[Alice_new_position[0]][Alice_new_position[1]] = "*"
        break

    if matrix[Alice_new_position[0]][Alice_new_position[1]].isdigit():
        tea_bags_collected += int(matrix[Alice_new_position[0]][Alice_new_position[1]])

    matrix[Alice_new_position[0]][Alice_new_position[1]] = "*"
    Alice = Alice_new_position

if tea_bags_collected >= 10:
    print(f"She did it! She went to the party.")
else:
    print(f"Alice didn't make it to the tea party.")

[print(*row) for row in matrix]

