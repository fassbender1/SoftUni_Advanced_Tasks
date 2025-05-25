lines = int(input())

cars_left = set()

for _ in range(lines):
    direction, plate = input().split(", ")
    if direction == "IN":
        cars_left.add(plate)
    else:
        cars_left.remove(plate)


if cars_left:
    for car in cars_left: # print(*cars_left, sep="\n")
        print(car)
else:
    print(f"Parking Lot is Empty")
