rows, columns = [int(el) for el in input().split(", ")]

matrix = []

for _ in range(rows):
    row_data = [int(el) for el in input().split()]
    matrix.append(row_data)

for col_index in range(columns):
    columns_sum = 0
    for row_index in range(rows):
        columns_sum += matrix[row_index][col_index]
    print(columns_sum)

