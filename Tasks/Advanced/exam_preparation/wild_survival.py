from collections import deque

bee_groups = deque(int(el) for el in input().split())
bee_eaters = [int(el) for el in input().split()]

bee_eater_possible_kills = 7

while bee_groups and bee_eaters:
    current_bees = bee_groups.popleft()
    current_bee_eaters = bee_eaters.pop()

    while current_bees > 0 and current_bee_eaters > 0:
        current_bees -= bee_eater_possible_kills
        if current_bees >= 0:
            current_bee_eaters -= 1

    if current_bees > 0:
        bee_groups.append(current_bees)
    elif current_bee_eaters > 0:
        bee_eaters.append(current_bee_eaters)


print(f"The final battle is over!")

if not bee_groups and not bee_eaters:
    print(f"But no one made it out alive!")
elif bee_groups and not bee_eaters:
    print(f"Bee groups left: {', '.join(str(el) for el in bee_groups)}")
elif not bee_groups and bee_eaters:
    print(f"Bee-eater groups left: {', '.join(str(el) for el in bee_eaters)}")
