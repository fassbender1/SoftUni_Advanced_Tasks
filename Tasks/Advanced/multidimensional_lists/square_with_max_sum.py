rows, columns = [int(x) for x in input().split(", ")]

matrix = []

for _ in range(rows):
    row_data = [int(x) for x in input().split(", ")]
    matrix.append(row_data)

max_sum = -99999999999999999
sub_matrix = []

for row_index in range(rows - 1):
    for col_index in range(columns - 1):
        current_element = matrix[row_index][col_index]
        next_element = matrix[row_index][col_index + 1]
        current_element_below = matrix[row_index + 1][col_index]
        next_element_below = matrix[row_index + 1][col_index + 1]

        current_sum = current_element + next_element + current_element_below + next_element_below
        if current_sum > max_sum:
            max_sum = current_sum
            sub_matrix = [[current_element, next_element], [current_element_below, next_element_below]]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)









