n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]

primary_diagonal = [matrix[index][index] for index in range(n)]
secondary_diagonal = [matrix[index][-1 - index] for index in range(n)]

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))

