# from collections import deque
#
# green_light_duration = int(input())
# free_window_duration = int(input())
#
# cars_queue = deque()
# total_cars_passed = 0
#
# while True:
#     command = input()
#
#     if command == "END":
#         print(f"Everyone is safe.")
#         print(f"{total_cars_passed} total cars passed the crossroads.")
#         break
#
#     elif command == "green":
#         time_left = green_light_duration
#
#         while cars_queue and time_left > 0:
#             car = cars_queue.popleft()
#             car_length = len(car)
#
#             if car_length <= time_left:
#                 time_left -= car_length
#                 total_cars_passed += 1
#             else:
#                 hit_index = time_left + free_window_duration
#                 print("A crash happened!")
#                 print(f"{car} was hit at {car[hit_index]}.")
#                 exit()
#     else:
#         cars_queue.append(command)
#

from collections import deque

green_light_duration = int(input())
free_window_duration = int(input())

cars_queue = deque()
total_cars_passed = 0

while True:
    command = input()

    if command == "END":
        print("Everyone is safe.")
        print(f"{total_cars_passed} total cars passed the crossroads.")
        break

    elif command == "green":
        time_left = green_light_duration

        while cars_queue and time_left > 0:
            car = cars_queue.popleft()
            car_length = len(car)

            if car_length <= time_left:

                time_left -= car_length
                total_cars_passed += 1
            else:

                remaining = car_length - time_left
                if remaining <= free_window_duration:

                    total_cars_passed += 1
                    time_left = 0
                else:

                    hit_index = time_left + free_window_duration
                    print("A crash happened!")
                    print(f"{car} was hit at {car[hit_index]}.")
                    exit()

    else:

        cars_queue.append(command)