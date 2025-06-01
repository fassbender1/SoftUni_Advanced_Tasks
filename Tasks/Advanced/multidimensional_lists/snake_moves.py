from collections import deque

rows, columns = [int(x) for x in input().split()]
text = deque(input())

matrix = []

for row in range(rows):
    matrix.append([""] * columns)
    for column in range(columns):
        if row % 2 == 0:
            matrix[row][column] = text[0]
        else:
            matrix[row][-1 - column] = text[0]
        text.rotate(-1)

[print(*row, sep="") for row in matrix]
