# filename: speed_limit_checker.py
max_speed_allowed = float(input("Enter the maximum speed allowed: "))
speeds = list(map(float, input("Enter the list of speeds: ").split()))
infractions = 0
for i, speed in enumerate(speeds[1:], start=1):
    if max_speed_allowed*1.2 < speed < max_speed_allowed*1.5:
        print(i)
        infractions += 1
print(f'The number of drivers who violated the limit is: {infractions}')
