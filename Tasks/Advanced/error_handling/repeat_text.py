# text = input()
#
# try:
#     times = int(input())
#     print(text*times)
# except ValueError:
#     print(f"Variables times must be an integer")

text = input()

try:
    times = int(input())
except ValueError:
    print(f"Variables times must be an integer")
else:
    print(text * times)