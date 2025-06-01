n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

bombs = input().split()


directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

for bomb in bombs:
    row, col = map(int, bomb.split(','))
    bomb_value = matrix[row][col]

    if bomb_value > 0:

        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < n and 0 <= c < n and matrix[r][c] > 0:
                matrix[r][c] -= bomb_value

        matrix[row][col] = 0

alive_cells = [cell for row in matrix for cell in row if cell > 0]

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")

for row in matrix:
    print(' '.join(str(cell) for cell in row))

