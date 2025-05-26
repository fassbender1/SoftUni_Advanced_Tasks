# without matrix and an additional for loop with if check

rows = int(input())

diagonals_sum = 0

for row_index in range(rows):
    row_data = [int(el) for el in input().split()]
    diagonals_sum += row_data[row_index]

print(diagonals_sum)


# with matrix

# rows = int(input())
#
# matrix = []
# diagonals_sum = 0
#
# for row_index in range(rows):
#     row_data = [int(el) for el in input().split()]
#     matrix.append(row_data)
#     for column_index in range(len(row_data)):
#         if column_index == row_index:
#             diagonals_sum += matrix[row_index][column_index]
#
# print(diagonals_sum)

# without matrix

# rows = int(input())
#
# diagonals_sum = 0
#
# for row_index in range(rows):
#     row_data = [int(el) for el in input().split()]
#     for column_index in range(len(row_data)):
#         if column_index == row_index:
#             diagonals_sum += row_data[column_index]
#
# print(diagonals_sum)


