rows = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

while True:
    command = input().split()
    if command[0] == "END":
        break
    row, column, value = map(int, command[1:])

    if row < 0 or row >= rows or column < 0 or column >= len(matrix[0]):
        print("Invalid coordinates")
        continue

    if command[0] == "Add":
        matrix[row][column] += value
    elif command[0] == "Subtract":
        matrix[row][column] -= value

[print(*row) for row in matrix]



