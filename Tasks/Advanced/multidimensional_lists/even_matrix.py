rows = int(input())

matrix = []

for _ in range(rows):
    elements = [int(el) for el in input().split(", ") if int(el) % 2 == 0]
    matrix.append(elements)

print(matrix)

# 1 row solution with nested comprehension
# print([[int(el) for el in input().split(", ") if int(el) % 2 == 0] for _ in range(int(input()))])
