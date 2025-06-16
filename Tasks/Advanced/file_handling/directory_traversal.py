import os

# from Advanced.constants import abs_project_path

file_info = {}

directory = "../lab_files/"

# for el in os.listdir(path = os.path.join(abs_project_path,"lab_files")):

for el in os.listdir(directory):
    f = os.path.join(directory, el)
    if os.path.isfile(f):
        extension = el.split(".")[-1]
        if extension not in file_info:
            file_info[extension] = []
        file_info[extension].append(el)
    else:
        for element in os.listdir(f):
            file_name = os.path.join(f, element)
            if os.path.isfile(file_name):
                ext = element.split(".")[-1]
                if ext not in file_info:
                    file_info[ext] = []
                file_info[ext].append(element)

with open(os.path.join(directory, "report.txt"), "w") as output_file:
    for ext, filenames in sorted(file_info.items()):
        output_file.write(f".{ext}\n")
        for file_name in sorted(filenames):
            output_file.write(f"- - - {file_name}\n")
