from fibonacci_core import create_sequence, locate

command = input()
seq = None

while command != "Stop":
    num = int(command.split()[-1])
    if command.startswith("Locate"):
        if not seq:
            print("Please first create a sequence")
            command = input()
            continue
        result = locate(seq, num)
        print(result)
    elif command.startswith("Create"):
        seq = create_sequence(num)
        print(*seq)

    command = input()
