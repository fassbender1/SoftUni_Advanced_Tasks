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

    built = False

    # Match exact power first, in defined order
    for name in required_drones:
        power = required_drones[name]
        if activation_power == power and name not in drones_made:
            drones_made[name] = power
            built = True
            break

    if not built:
        # Try building any unmatched drone with lower power requirement
        candidates = [(n, p) for n, p in required_drones.items() if p < activation_power and n not in drones_made]
        if candidates:
            best = max(candidates, key=lambda x: x[1])
            drones_made[best[0]] = best[1]
            reduced_cell = current_cell - 30
            if reduced_cell > 0:
                power_cells.append(reduced_cell)
            built = True
        else:
            # Nothing can be built, reduce power cell by 1 and re-add if > 0
            reduced_cell = current_cell - 1
            if reduced_cell > 0:
                power_cells.append(reduced_cell)

# Output
if len(drones_made) == 5:
    print("Mission Accomplished! All Guardian Drones activated!")
else:
    print("Mission Failed! Some drones were not built.")

if drones_made:
    print("Assembled Drones: ", end="")
    ordered_names = [name for name in required_drones if name in drones_made]
    print(", ".join(ordered_names))

if mechanical_parts:
    print(f"Mechanical Parts: {', '.join(str(p) for p in reversed(mechanical_parts))}")

if power_cells:
    print(f"Power Cells: {', '.join(str(c) for c in power_cells)}")