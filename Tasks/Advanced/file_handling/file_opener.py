import os

file_path = os.path.join("files", "test.txt")
file = open(file_path)

print(file.read())
