n = int(input())

matrix = [[int(x) for x in input().split(", ")] for _ in range(n)]

primary_diagonal = [matrix[index][index] for index in range(n)]
secondary_diagonal = [matrix[index][-1 -index] for index in range(n)]

print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")

