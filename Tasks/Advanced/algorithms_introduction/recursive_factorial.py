def get_factorial(num):
    if num == 1:
        return num

    return num * get_factorial(num - 1)

number = int(input())
print(get_factorial(number))