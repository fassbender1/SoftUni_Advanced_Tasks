def print_triangle(size):
    row_data = []
    for row in range(1, size + 2):
        row_data.append(row)
        print(*row_data, sep=" ")
    for row in range(size, 0, -1):
        row_data.remove(row)
        print(*row_data, sep=" ")