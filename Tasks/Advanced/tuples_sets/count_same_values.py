numbers = tuple([float(x) for x in input().split()])

data = {}

for element in numbers:
    data[element] = numbers.count(element)

for key, value in data.items():
    print(f"{key :.1f} - {value} times")