import os

from Advanced.constants import abs_project_path

file_info = {}

directory = 0

for el in os.listdir(path = os.path.join(abs_project_path,"lab_files")):
    file_info = el

print(file_info)