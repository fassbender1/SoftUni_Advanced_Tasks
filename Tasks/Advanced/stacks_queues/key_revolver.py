from collections import deque

price_per_bullet = int(input())
gun_barrel_size = int(input())
bullets = [int(x) for x in input().split()]
locks = deque(int(x) for x in input().split())
value = int(input())

bullets_fired = 0

while bullets and locks:
    bullets_fired += 1
    current_bullet = bullets.pop()
    value -= price_per_bullet
    if locks[0] >= current_bullet:
        locks.popleft()
        print("Bang!")
    else:
        print("Ping!")

    if bullets_fired == gun_barrel_size and bullets:
        bullets_fired = 0
        print("Reloading!")


if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f"{len(bullets)} bullets left. Earned ${value}")

