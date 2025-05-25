parentheses = input()

parentheses_types = {"(": ")", "[": "]", "{": "}"}
stack = []

for char in parentheses:
    if char in parentheses_types:
        stack.append(char)
    elif char in parentheses_types.values():
        if not stack:
            print("NO")
            break
        last_opening_parentheses = stack.pop()
        if parentheses_types[last_opening_parentheses] != char:
            print("NO")
            break
else:
    if stack:
        print("NO")
    else:
        print("YES")



