row, column = [int(el) for el in input().split(", ")]

matrix = []

sum_of_all = 0

for _ in range(row):
    row_data = [int(el) for el in input().split(", ")]
    matrix.append(row_data)
    sum_of_all += sum(row_data)

print(sum_of_all)
print(matrix)

