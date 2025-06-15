import os

path = os.path.join("..", "lab_files", "text.txt")

try:
    open(path)
    print("File found!")
except FileNotFoundError:
    print("File not found!")