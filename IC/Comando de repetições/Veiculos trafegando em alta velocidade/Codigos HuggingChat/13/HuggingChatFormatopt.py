def find_speeding_drivers(speed_limit, speeds):
    exceeded_speed_limit = []
    for i, speed in enumerate(speeds):
        if speed > speed_limit * 1.2 and speed < speed_limit * 1.5:
            exceeded_speed_limit.append(i)
    return exceeded_speed_limit, len(exceeded_speed_limit)

# Test the function
speed_limit = 60
speeds = [60, 75, 85, 90, 65, 70, 100, 80]
exceeded_speeds, num_exceeded = find_speeding_drivers(speed_limit, speeds)

# Output the positions of drivers who violated the speed limit
for position in exceeded_speeds:
    print(f"Driver at position {position} exceeded the speed limit")
print(f"Total number of drivers who exceeded the speed limit: {num_exceeded}")

You can replace the `speeds` list with your own data to test the program with different input. The output will display the positions of the drivers who violated the speed limit and the total number of drivers who exceeded the speed limit.