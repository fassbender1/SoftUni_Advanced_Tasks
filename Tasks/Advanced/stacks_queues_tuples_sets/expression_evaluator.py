from collections import deque

command = input().split()
elements = deque()

operators = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a // b
}

for el in command:
    if el not in "+-*/":
        elements.append(int(el))
    else:
        while len(elements) > 1:
            first_num = elements.popleft()
            second_num = elements.popleft()
            # if el == "+":
            #     elements.appendleft(first_num + second_num)
            # elif el == "-":
            #     elements.appendleft(first_num - second_num)
            # elif el == "*":
            #     elements.appendleft(first_num * second_num)
            # elif el == "/":
            #     elements.appendleft(first_num // second_num)
            elements.appendleft(operators[el](first_num, second_num))

print(elements[0])



