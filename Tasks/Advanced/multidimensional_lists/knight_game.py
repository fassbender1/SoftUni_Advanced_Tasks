rows = int(input())

matrix = []
knights = []

for row in range(rows):
    matrix.append(list(input()))
    for col in range(rows):
        if matrix[row][col] == "K":
            knights.append([row, col])

knights_removed = 0
possible_moves = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]

while True:
    max_hits = 0
    knight_max_hits = [0, 0]

    for k_row, k_col in knights:
        hits = 0
        for move in possible_moves:
            next_row = k_row + move[0]
            next_col = k_col + move[1]
            if 0 <= next_row < rows and 0 <= next_col < rows:
                if matrix[next_row][next_col] == "K":
                    hits += 1

        if hits > max_hits:
            max_hits = hits
            knight_max_hits = [k_row, k_col]

    if max_hits == 0:
        break

    knights.remove(knight_max_hits)
    matrix[knight_max_hits[0]][knight_max_hits[1]] = 0
    knights_removed += 1

print(knights_removed)


















