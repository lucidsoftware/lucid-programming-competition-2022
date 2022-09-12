import sys

def most_recent_free_dock(arrival, free_since_list, docks):
    return min([dock for dock in range(docks) if arrival >= free_since_list[dock]], 
               key=lambda dock: (arrival - free_since_list[dock]) % 60)

docks = int(sys.stdin.readline())
passenger_ships = int(sys.stdin.readline())
if passenger_ships > 0:
    arrivals = [int(arrival) for arrival in sys.stdin.readline().split(' ')]
    departures = [int(departure) for departure in sys.stdin.readline().split(' ')]

def main(docks, passenger_ships, arrivals, departures):
    cargo_ships = 0
    free_since_list = [0] * docks
    for ship_index in range(passenger_ships):
        next_arrival = arrivals[ship_index]
        dock_to_use = most_recent_free_dock(next_arrival, free_since_list, docks)
        cargo_ships += (next_arrival - free_since_list[dock_to_use]) // 60
        free_since_list[dock_to_use] = departures[ship_index]
    for free_time in free_since_list:
        cargo_ships += (720 - free_time) // 60
    print(cargo_ships)
    
main(docks, passenger_ships, arrivals, departures)