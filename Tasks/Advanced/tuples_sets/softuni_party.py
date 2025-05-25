guest_num = int(input())

reservations = set()

for _ in range(guest_num):
    current_guest = input()
    reservations.add(current_guest)

reservation = input()

while reservation != "END":
    reservations.remove(reservation)
    reservation = input()

print(len(reservations))

sorted_reservation = sorted(reservations)
print(*sorted_reservation, sep="\n")
