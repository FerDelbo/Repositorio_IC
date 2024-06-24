# filename: speed_limit.py

speed_limit = int(input("Enter the maximum speed limit of the road: "))
speeds = list(map(int, input("Enter the speed records of the cars that traveled on the road, separated by spaces: ").split()))

violations = []
for i in range(1, len(speeds)):
    if speeds[i] > speed_limit * 1.2 and speeds[i] < speed_limit * 1.5:
        violations.append(i)

if violations:
    print("The drivers who violated the speed limit (by more than 20% and less than 50%) are at the following positions in the vector:")
    for violation in violations:
        print(violation)
    print(f"Total number of drivers who violated the speed limit: {len(violations)}")
else:
    print("No drivers violated the speed limit.")
