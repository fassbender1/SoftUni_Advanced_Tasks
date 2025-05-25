longest_intersection = set()

for _ in range(int(input())):
    first, second = input().split("-")
    first_start, first_end = [int(el) for el in first.split(",")]
    second_start, second_end = [int(el) for el in second.split(",")]

    first_set = set(range(first_start, first_end + 1))
    second_set = set(range(second_start, second_end + 1))

    intersection = first_set.intersection(second_set) # first_set & second_set

    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(f"Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}")
