from collections import deque

boxes_with_materials = [int(x) for x in input().split()]
magic_values = deque(int(x) for x in input().split())

magic_for_presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}

presents_made = {}

while boxes_with_materials and magic_values:
    total_magic = boxes_with_materials[-1] * magic_values[0]
    if total_magic in magic_for_presents:
        new_present = magic_for_presents[total_magic]
        if new_present not in presents_made:
            presents_made[new_present] = 0
        presents_made[new_present] += 1
        boxes_with_materials.pop()
        magic_values.popleft()
    elif total_magic < 0:
        boxes_with_materials.append(boxes_with_materials.pop() + magic_values.popleft())
    elif total_magic > 0:
        magic_values.popleft()
        boxes_with_materials[-1] += 15
    else:
        if boxes_with_materials[-1] == 0:
            boxes_with_materials.pop()
        if magic_values[0] == 0:
            magic_values.popleft()

if ("Doll" in presents_made and "Wooden train" in presents_made) or (
        "Teddy bear" in presents_made and "Bicycle" in presents_made):
    print(f"The presents are crafted! Merry Christmas!")
else:
    print(f"No presents this Christmas!")

if boxes_with_materials:
    print(f"Materials left: {', '.join(str(x) for x in boxes_with_materials[::-1])}")

if magic_values:
    print(f"Magic left: {', '.join(str(x) for x in magic_values)}")

for key, value in sorted(presents_made.items()):
    if value > 0:
        print(f"{key}: {value}")










