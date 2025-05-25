def create_set_from_ranges(range_str):
    start, end = range_str.split(",")
    return set(range(start, end + 1))


longest_intersection = set()

for _ in range(int(input())):
    first, second = input().split("-")

    first_set = create_set_from_ranges(first)
    second_set = create_set_from_ranges(second)

    intersection = first_set.intersection(second_set) # first_set & second_set

    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(f"Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}")