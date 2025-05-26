number = int(input())

matrix = []

for _ in range(number):
    row_data = list(input())
    matrix.append(row_data)

wanted_symbol = input()
position = None

for row_index in range(number):
    if position:
        break

    for col_index in range(number):
        if matrix[row_index][col_index] == wanted_symbol:
            position = (row_index, col_index)
            break

if position:
    print(position)
else:
    print(f"{wanted_symbol} does not occur in the matrix")



