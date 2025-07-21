def genrange(start: int, end: int):
    # for num in range(start, end + 1):
    #     yield num
    while start <= end:
        yield start
        start += 1

print(list(genrange(1, 10)))