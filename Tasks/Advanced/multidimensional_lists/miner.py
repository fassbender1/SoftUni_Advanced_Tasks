size = int(input())
commands = input().split()

field = []
miner_row = miner_col = 0
total_coal = 0

for r in range(size):
    row = input().split()
    field.append(row)
    for c in range(size):
        if 's' in field[r][c]:
            miner_row, miner_col = r, c

    total_coal += row.count('c')

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

collected_coal = 0

for command in commands:
    dr, dc = moves[command]
    new_row, new_col = miner_row + dr, miner_col + dc

    if 0 <= new_row < size and 0 <= new_col < size:
        miner_row, miner_col = new_row, new_col
        cell = field[miner_row][miner_col]

        if cell == 'c':
            collected_coal += 1
            field[miner_row][miner_col] = '*'
            if collected_coal == total_coal:
                print(f"You collected all coal! ({miner_row}, {miner_col})")
                break
        elif cell == 'e':
            print(f"Game over! ({miner_row}, {miner_col})")
            break
else:
    remaining = total_coal - collected_coal
    print(f"{remaining} pieces of coal left. ({miner_row}, {miner_col})")

