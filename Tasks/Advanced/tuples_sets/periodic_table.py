num_of_chemicals = int(input())

unique_elements = set()

#for _ in range(num_of_chemicals):
#   chem_element = input().split()
#   for el in chem_element:
#       unique_elements.add(el)

#for el in range(int(input())):
#    unique_elements = unique_elements.union(input().split())

for _ in range(int(input())):
    for el in input().split():
        unique_elements.add(el)

print(*unique_elements, sep="\n")
