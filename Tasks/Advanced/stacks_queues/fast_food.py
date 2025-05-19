from collections import deque

quantity = int(input())
order_queue = deque(int(x) for x in input().split())

print(max(order_queue))

while order_queue and order_queue[0] <= quantity:
    quantity -= order_queue.popleft()

if order_queue:
    print(f"Orders left:", *order_queue)
else:
    print("Orders complete")


