from collections import deque

quantity = int(input())
name = input()
queue = deque()

while name != "Start":
    queue.append(name)
    name = input()

command = input()

while command != "End":
    if command.isdigit():
        person_name = queue.popleft()
        requested = int(command)
        if requested <= quantity:
            quantity -= requested
            print(f"{person_name} got water")
        else:
            print(f"{person_name} must wait")
    elif command.startswith("refill"):
        _, liters_to_fill = command.split(" ")
        quantity += int(liters_to_fill)
    command = input()

print(f"{quantity} liters left")
