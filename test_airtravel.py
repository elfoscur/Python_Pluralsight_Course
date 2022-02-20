from airtravel import Flight, Aircraft


a = Aircraft("G-EUPT", "Airbus A319", num_rows=22, num_seats_per_row=6)

print(a.seating_plan())


f = Flight("AA123", a)

from pprint import pprint as pp

pp(f._seating)
