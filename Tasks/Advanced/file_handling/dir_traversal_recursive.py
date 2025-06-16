import os

file_info = {}
directory = "../lab_files/"

def get_files(folder, level):
    if level == -1:
        return

    for el in os.listdir(folder):
        f = os.path.join(folder, el)
        if os.path.isfile(f):
            extension = os.path.splitext(el)[1]
            if extension not in file_info:
                file_info[extension] = []
            file_info[extension].append(el)
        else:
            get_files(f, level - 1)

get_files(directory, 2)

with open(os.path.join(directory, "report2.txt"), "w") as output_file:
    for ext, filenames in sorted(file_info.items()):
        output_file.write(f"{ext}\n")
        for file_name in sorted(filenames):
            output_file.write(f"- - - {file_name}\n")