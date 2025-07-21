def squares(n: int):
    for num in range(1, n + 1):
        square = num ** 2
        yield square

print(list(squares(5)))