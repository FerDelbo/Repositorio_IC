# filename: speed_limit.py

max_speed = float(input("Enter the maximum speed limit: "))
speeds = list(map(float, input("Enter the speed records: ").split()))

# check if the first value is valid
if speeds[0] <= 0:
    print("Invalid input: the maximum speed limit must be a positive number.")
    

# initialize the accumulator
num_infractions = 0

# iterate over the speed records
for i in range(1, len(speeds)):
    speed = speeds[i]

    # check if the speed is valid
    if speed <= 0:
        print("Invalid input: the speed records must be positive numbers.")
        

    # check if the speed limit is violated
    if speed > max_speed * 1.2 and speed < max_speed * 1.5:
        print("Infraction at position", i)
        num_infractions += 1

# print the number of infractions
print("Number of infractions:", num_infractions)

