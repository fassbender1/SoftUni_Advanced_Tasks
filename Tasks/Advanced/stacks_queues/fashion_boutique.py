clothes = [int(x) for x in input().split()] # [map(int, input().split())]
rack_capacity = int(input())
rack_count = 0

while clothes:
    rack_count += 1
    current_capacity = rack_capacity
    while clothes and clothes[-1] <= current_capacity:
        current_capacity -= clothes.pop()

print(rack_count)

