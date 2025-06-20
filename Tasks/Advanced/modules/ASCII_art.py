from pyfiglet import figlet_format

def print_art(text):
    ascii_art = figlet_format(text)
    print(ascii_art)

print_art(input())