import os
import re
from Advanced.constants import abs_project_path

path = os.path.join(abs_project_path, "lab_files", "word_count_ex")

with open(os.path.join(path, "input.txt")) as file:
    text = file.read()

with open(os.path.join(path, "words.txt")) as file:
    words = file.read().split()

data = {}
count = 0

for word in words:
    pattern = rf"\b{word}\b"
    word_count = len(re.findall(pattern, text, re.IGNORECASE))
    data[word] = word_count

sorted_data = sorted(data.items(), key=lambda kvp: -kvp[1])

with open(os.path.join(path,"output.txt"), "w") as file:
    for key, value in sorted_data:
        file.write(f"{key} - {value}\n")











