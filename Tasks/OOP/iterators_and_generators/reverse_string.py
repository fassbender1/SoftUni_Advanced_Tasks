def reverse_text(string: str):
    for char in reversed(string):
        yield char

for char in reverse_text("step"):
    print(char, end='')