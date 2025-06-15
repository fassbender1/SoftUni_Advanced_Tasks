import os

with (open(os.path.join("line_numbers", "text.txt", 'r')) as input_file,
      open(os.path.join("line_numbers", "output.txt", 'w')) as output_file):
    result = []

    for row, line in enumerate(input_file):
        letters_counter = 0
        symbol_counter = 0
        for ch in line:
            if ch.isalpha():
                letters_counter += 1
            else:
                symbol_counter += 1
        result.append(f"Line {row + 1}: {line} ({letters_counter})({symbol_counter})")

    output_file.write("\n".join(result))