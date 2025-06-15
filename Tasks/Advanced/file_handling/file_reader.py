import os.path

from Advanced.constants import abs_project_path

path = os.path.join(abs_project_path, "lab_files", "text.txt")
file = open(path)

# numbers = [int(el) for el in file.read().split("\n")]
# print(sum(numbers))

total_sum = 0

for el in file.readlines():
    if el.endswith("\n"):
        el = el[:-1]
    total_sum += int(el)

print(total_sum)