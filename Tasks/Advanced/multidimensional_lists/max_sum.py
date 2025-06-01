from sys import maxsize

rows, columns = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

max_sum = -maxsize
max_row = 0
max_col = 0

for row_index in range(rows - 2):
    for col_index in range(columns - 2):
        current_sum = 0
        for r in range(row_index, row_index + 3):
            for c in range(col_index, col_index + 3):
                current_sum+= matrix[r][c]

        if current_sum > max_sum:
            max_sum = current_sum
            max_row = row_index
            max_col = col_index

print(f"Sum = {max_sum}")

max_submatrix = [matrix[r][max_col:max_col + 3] for r in range(max_row, max_row + 3)]
[print(*row) for row in max_submatrix]



