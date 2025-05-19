from collections import deque

numbers_string = input().split()
stack = []

while numbers_string:
    stack.append(numbers_string.pop())

print(" ".join(stack))
