import os

file_path = os.path.join("files", "level1", "level2", "file_level2.txt")
file = open(file_path)

print(file.read())
