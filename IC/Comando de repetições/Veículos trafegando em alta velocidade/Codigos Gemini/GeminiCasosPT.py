# filename: speed_limit.py
limit = float(input("Enter the speed limit: "))
speeds = [float(speed) for speed in input("Enter the speeds: ").split()]

over_speed_count = 0
for i, speed in enumerate(speeds):
    if speed > limit and speed <= limit * 1.2:
        print(i + 1)
        over_speed_count += 1

print(f"{over_speed_count} drivers exceeded the speed limit by more than 20% and less than 50%.")
