# filename: get_speeding_drivers.py
import csv
import re

speed_limits = []
drivers = []

with open('speed_limits.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        speed_limits.append(row)

with open('drivers.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        drivers.append(row)

for driver in drivers:
    speed_limit = [s for s in speed_limits if re.match(driver[1], s[0])][0][1]
    if int(driver[2]) - int(speed_limit) > int(speed_limit) * 0.2 and int(driver[2]) - int(speed_limit) < int(speed_limit) * 0.5:
        print(driver[0], driver[1], driver[2])
