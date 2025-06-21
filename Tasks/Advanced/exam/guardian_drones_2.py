from collections import deque

mechanical_parts = [int(el) for el in input().split()]
power_cells = deque([int(el) for el in input().split()])

required_drones = {
    "Sentinel-X": 100,
    "Viper-MKII": 85,
    "Aegis-7": 75,
    "Striker-R": 65,
    "Titan-Core": 55
}

drones_made = []
assembled_names = set()

while len(drones_made) < 5 and mechanical_parts and power_cells:
    current_part = mechanical_parts.pop()
    current_cell = power_cells.popleft()
    activation_power = current_part + current_cell

    built = False

    for name, power in required_drones.items():
        if activation_power == power and name not in assembled_names:
            drones_made.append(name)
            assembled_names.add(name)
            built = True
            break

    if not built:
        candidates = [(n, p) for n, p in required_drones.items() if p < activation_power and n not in assembled_names]
        if candidates:
            best = max(candidates, key=lambda x: x[1])
            drones_made.append(best[0])
            assembled_names.add(best[0])
            reduced_cell = current_cell - 30
            if reduced_cell > 0:
                power_cells.append(reduced_cell)
            built = True
        else:
            reduced_cell = current_cell - 1
            if reduced_cell > 0:
                power_cells.append(reduced_cell)


if len(drones_made) == 5:
    print("Mission Accomplished! All Guardian Drones activated!")
else:
    print("Mission Failed! Some drones were not built.")

if drones_made:
    print(f"Assembled Drones: {', '.join(drones_made)}")

if mechanical_parts:
    print(f"Mechanical Parts: {', '.join(str(p) for p in reversed(mechanical_parts))}")

if power_cells:
    print(f"Power Cells: {', '.join(str(c) for c in power_cells)}")