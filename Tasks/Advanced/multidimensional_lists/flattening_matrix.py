rows = int(input())

flat_matrix = []

for _ in range(rows):
    column = [int(x) for x in input().split(", ")]
    # or the following instead of another for loop
    # flat_matrix.extend(column)
    for each_element in column:
        flat_matrix.append(each_element)

print(flat_matrix)
