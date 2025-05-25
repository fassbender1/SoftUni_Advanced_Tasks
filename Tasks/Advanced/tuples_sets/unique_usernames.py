number = int(input())

unique = set()

for _ in range(number):
    unique.add(input())

for name in unique:
    print(name)

#print(*unique, sep="\n")

#print("\n".join(unique))