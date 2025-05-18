string = list(input())
match = []

for index in range(len(string)):
    if string[index] == "(":
        match.append(index)
    elif string[index] == ")":
        start_index = match.pop()
        print(''.join(string[start_index:index+1]))


