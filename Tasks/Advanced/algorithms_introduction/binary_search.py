def binary_search(nums, target):
    left_index = 0
    right_index = len(nums) - 1

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_element = nums[mid_index]
        if mid_element == target:
            return mid_index
        if mid_element < target:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return -1

numbers = [int(x) for x in input().split()]
target_num = int(input())
result = binary_search(numbers, target_num)
print(result)
