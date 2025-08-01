from math import sqrt

def get_primes(nums: list):
    for num in nums:
        if num < 2:
            continue
        for i in range(2, int(sqrt(num)) + 1):
        # for i in range(2, num):
            if num % i == 0:
                break
        else:
            yield num

print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print(list(get_primes([-2, 0, 0, 1, 1, 0])))