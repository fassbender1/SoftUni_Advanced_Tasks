def reverse_text(string: str):
    for ch in reversed(string):
        yield ch
    # index = len(string)-1
    # while index >= 0:
    #     yield string[index]
    #     index -= 1

for char in reverse_text("step"):
    print(char, end='')