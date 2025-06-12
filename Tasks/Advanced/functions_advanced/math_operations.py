# def math_operations(*args, **kwargs):
#     firsts = []
#     seconds = []
#     thirds = []
#     fourths = []
#     for index in range(len(args)):
#         if index % 4 == 0:
#             firsts.append(args[index])
#         elif index % 4 == 1:
#             seconds.append(args[index])
#         elif index % 4 == 2 and index != 0:
#             thirds.append(args[index])
#         elif index % 4 == 3:
#             fourths.append(args[index])
#
#     kwargs['a'] = sum(firsts) + kwargs['a']
#     kwargs['s'] = kwargs['s'] - sum(seconds)
#     if sum(thirds):
#         kwargs['d'] = kwargs['d'] / sum(thirds)
#     kwargs['m'] = kwargs['m'] * sum(fourths)
#     sorted_result = sorted(kwargs.items(), key=lambda kvp: (-kvp[1], kvp[0]))
#     result = ""
#     for key, value in sorted_result:
#         result += f"{key}: {value:.1f}\n"
#     return result


def math_operations(*args, **kwargs):
    ops = ['a', 's', 'd', 'm']
    for i, num in enumerate(args):
        key = ops[i % 4]
        if key == 'a':
            kwargs[key] += num
        elif key == 's':
            kwargs[key] -= num
        elif key == 'd':
            if num != 0:
                kwargs[key] /= num
        elif key == 'm':
            kwargs[key] *= num

    sorted_result = sorted(kwargs.items(), key=lambda kvp: (-kvp[1], kvp[0]))
    result = '\n'.join(f"{k}: {v:.1f}" for k, v in sorted_result)
    return result


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))









