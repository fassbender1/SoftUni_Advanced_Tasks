from Advanced.constants import abs_project_path

# # using relative path
import os

# path = os.path.join("..", "lab_files", "text.txt")

#using absolute path
path = os.path.join(abs_project_path, "lab_files", "text.txt")

try:
    open(path)
    print("File found!")
except FileNotFoundError:
    print("File not found!")