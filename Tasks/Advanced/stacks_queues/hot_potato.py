from collections import deque

names = input().split()
nth_toss = int(input())
queue = deque(names)

while len(queue) != 1:
    queue.rotate(-(nth_toss - 1))
    removed_kid = queue.popleft()
    print(f"Removed {removed_kid}")

print(f"Last is {queue[0]}")

