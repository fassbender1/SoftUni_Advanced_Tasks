number = int(input())

values_odd = set()
values_even = set()

for row in range(1, number + 1):
    name = input()
    total_value = 0
    for char in name:
        ascii_value = ord(char)
        total_value += ascii_value
    divided = total_value // row
    if divided % 2 == 0:
        values_even.add(divided)
    else:
        values_odd.add(divided)

if sum(values_odd) == sum(values_even):
    print(*values_odd.union(values_even), sep=", ")

elif sum(values_odd) > sum(values_even):
    print(*values_odd.difference(values_even), sep=", ")

elif sum(values_odd) < sum(values_even):
    print(*values_odd.symmetric_difference(values_even), sep=", ")
