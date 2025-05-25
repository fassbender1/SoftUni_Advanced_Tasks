names_number = int(input())

names = set()

for _ in range(names_number):
    current_name = input()
    if current_name in names:
        continue
    names.add(current_name)

print(*names, sep="\n")

