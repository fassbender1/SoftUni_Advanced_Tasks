def create_sequence(number):
    seq = [0, 1]
    for _ in range(number - 2):
        seq.append(seq[-1] + seq[-2])
    return seq

def locate(seq, number):
    try:
        return f"The number - {number} is at index {seq.index(number)}"
    except ValueError:
        return f"The number {number} is not in the sequence"
