def func_executor(*args):
    result = ""
    for executor in args:
        func = executor[0]
        func_args = executor[1]

        func_result = func(*func_args)
        result += f"{func.__name__} - {func_result}\n"
    return result


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))

























