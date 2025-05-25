first_subset = set(int(x) for x in input().split())
second_subset = set(int(x) for x in input().split())

for _ in range(int(input())):
    line = input().split()
    command = line[0] + " " + line[1]
    numbers = [int(x) for x in line[2:]]
    if command == "Add First":
        first_subset.update(numbers)
    elif command == "Add Second":
        second_subset.update(numbers)
    elif command == "Remove First":
        first_subset.difference_update(numbers)
    elif command == "Remove Second":
        second_subset.difference_update(numbers)
    elif command == "Check Subset":
        print(first_subset.issubset(second_subset) or second_subset.issubset(first_subset))

print(*sorted(first_subset), sep=", ")
print(*sorted(second_subset), sep=", ")
