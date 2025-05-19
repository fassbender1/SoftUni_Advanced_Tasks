number = int(input())

stack = []

for _ in range(number):
    command = input().split()
    if command[0] == "1":
        stack.append(int(command[1]))
    elif stack:
        if command[0] == "2":
            stack.pop()
        elif command[0] == "3":
            print(max(stack))
        elif command[0] == "4":
            print(min(stack))

print(", ".join(str(num) for num in reversed(stack)))
