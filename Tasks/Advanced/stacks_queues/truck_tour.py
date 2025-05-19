from collections import deque

num_of_pumps = int(input())
pumps = deque()

for _ in range(num_of_pumps):
    petrol_amount, distance = input().split()
    pumps.append({"petrol": int(petrol_amount), "dist": int(distance)})

start_position = 0
stops = 0

while stops < num_of_pumps:
    petrol = 0
    for i in range(num_of_pumps):
        petrol += pumps[i]["petrol"]
        dist = pumps[i]["dist"]
        if petrol < dist:
            pumps.rotate(-1)
            start_position += 1
            stops = 0
            break
        petrol -= dist
        stops += 1

print(start_position)













