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

drones_made = {}

while len(drones_made) < len(required_drones) and mechanical_parts and power_cells:
    current_part = mechanical_parts.pop()
    current_cell = power_cells.popleft()
    activation_power = current_part + current_cell
    is_built = False

    for key, value in required_drones.items():
        if activation_power == value and key not in drones_made:
            drones_made[key] = value
            is_built = True
            break

    if not is_built:
        candidates = [(n, p) for n, p in required_drones.items() if
                          p < activation_power and n not in drones_made]
        if candidates:
            best = max(candidates, key=lambda x: x[1])
            drones_made[best[0]] = best[1]
            reduced_cell = current_cell - 30
            if reduced_cell > 0:
                power_cells.append(reduced_cell)
            is_built = True
        else:
            reduced_cell = current_cell - 1
            if reduced_cell > 0:
                power_cells.append(reduced_cell)


if len(drones_made) == len(required_drones):
    print(f"Mission Accomplished! All Guardian Drones activated!")
else:
    print(f"Mission Failed! Some drones were not built.")

if drones_made:
    print(f"Assembled Drones: {', '.join([str(el) for el in drones_made])}")
if mechanical_parts:
    print(f"Mechanical Parts: {', '.join(str(el) for el in reversed(mechanical_parts))}")
if power_cells:
    print(f"Power Cells: {', '.join(str(el) for el in power_cells)}")






















