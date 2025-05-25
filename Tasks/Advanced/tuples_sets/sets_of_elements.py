one, two = [int(x) for x in input().split()]

set_one = set()
set_two = set()

for _ in range(one):
    set_one.add(input())

for _ in range(two):
    set_two.add(input())

same_elements = set_one.intersection(set_two)  # set_one & set_two

print(*same_elements, sep="\n")





