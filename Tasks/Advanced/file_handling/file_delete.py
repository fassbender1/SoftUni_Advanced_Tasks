import os

from Advanced.constants import abs_project_path

try:
    path = os.path.join(abs_project_path, "files", "level1", "Secret_Cow_Level", "Cows", "test.txt")
    os.remove(path)
except FileNotFoundError:
    print("File already deleted")