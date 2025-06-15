import os

from Advanced.constants import abs_project_path

path = os.path.join(abs_project_path, "lab_files", "fire_write_ex.txt")

with open(path, "w") as file:
    file.write(input())
