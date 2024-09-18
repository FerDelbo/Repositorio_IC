def speed_limit_violators(drivers):
    speed_limit = 60
    violators = []

    for driver in drivers:
        driver_name = driver['name']
        driver_speed = driver['speed']
        percentage_above_limit = ((driver_speed - speed_limit) / speed_limit) * 100

        if 20 < percentage_above_limit < 50:
            violators.append(driver_name)

    return violators

# Test the function with a sample list of drivers
drivers = [
    {'name': 'Alice', 'speed': 70},
    {'name': 'Bob', 'speed': 80},
    {'name': 'Carol', 'speed': 90},
    {'name': 'David', 'speed': 100},
]

violators = speed_limit_violators(drivers)
print(f"The following drivers exceeded the speed limit by more than 20% and less than 50%: {violators}")