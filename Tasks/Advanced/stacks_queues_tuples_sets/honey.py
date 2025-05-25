from collections import deque

bees = deque(int(x) for x in input().split())
nectar = [int(x) for x in input().split()]
operations = deque(input().split())

honey_made = 0

operators = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if b != 0 else 0
}

while bees and nectar:
    if nectar[-1] >= bees[0]:
        honey_made += abs(operators[operations[0]](bees[0], nectar[-1]))
        nectar.pop()
        bees.popleft()
        operations.popleft()
    else:
        nectar.pop()


print(f"Total honey made: {honey_made}")
if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")













