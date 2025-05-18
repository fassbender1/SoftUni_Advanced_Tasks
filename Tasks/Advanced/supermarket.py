from collections import deque

command = input()
stack = deque()

while command != "End":
    name = command
    if name == "Paid":
        while stack:
            print(stack.popleft())
    else:
        stack.append(name)
    command = input()

print(f"{len(stack)} people remaining.")
