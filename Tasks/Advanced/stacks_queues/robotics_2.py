from collections import deque

robots_input = input().split(";")
robots = []

for robot_data in robots_input:
    name, time_str = robot_data.split("-")
    robots.append({"name": name, "process_time": int(time_str), "available_in": 0})

start_time = input()
hh, mm, ss = map(int, start_time.split(":"))
current_time = hh * 3600 + mm * 60 + ss

products = deque()

while True:
    product = input()
    if product == "End":
        break
    products.append(product)

while products:
    current_time += 1
    product = products.popleft()

    assigned = False

    for robot in robots:
        if robot["available_in"] <= current_time:
            robot["available_in"] = current_time + robot["process_time"]
            hours = (current_time // 3600) % 24
            minutes = (current_time % 3600) // 60
            seconds = current_time % 60
            print(f"{robot['name']} - {product} [{hours:02d}:{minutes:02d}:{seconds:02d}]")
            assigned = True
            break

    if not assigned:
        products.append(product)

