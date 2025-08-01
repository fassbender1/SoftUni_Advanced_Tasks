import itertools

def possible_permutations(nums: list):
    for perm in itertools.permutations(nums):
        yield list(perm)

# def possible_permutations(nums: list):
#     if len(nums) <= 1:
#         yield nums
#     else:
#         for i in range(len(nums)):
#             for perm in possible_permutations(nums[:i] + nums[i + 1:]):
#                 yield [nums[i]] + perm

[print(n) for n in possible_permutations([1, 2, 3])]
[print(n) for n in possible_permutations([1])]