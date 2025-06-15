import os

with open(os.path.join("even_lines", "text.txt")) as f:
    for row, line in enumerate(f):
        if row % 2 == 0:
            for ch in {"-", ",", ".", "!", "?"}:
                line = line.replace(ch, "@")
            print(" ".join(reversed(line.split())))

