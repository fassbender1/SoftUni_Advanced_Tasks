from collections import deque

cups_capacity = deque(int(x) for x in input().split())
bottles_filled = [int(x) for x in input().split()]

wasted_water = 0

while cups_capacity and bottles_filled:
    current_cup = cups_capacity[0]
    current_bottle = bottles_filled.pop()

    if current_bottle >= current_cup:
        wasted_water += current_bottle - current_cup
        cups_capacity.popleft()
    else:
        cups_capacity[0] -= current_bottle

if not cups_capacity:
    print(f"Bottles: {' '.join(str(x) for x in reversed(bottles_filled))}")
else:
    print(f"Cups: {' '.join(str(x) for x in cups_capacity)}")

print(f"Wasted litters of water: {wasted_water}")
