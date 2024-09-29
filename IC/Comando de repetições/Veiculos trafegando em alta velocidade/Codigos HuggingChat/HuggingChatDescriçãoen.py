def check_speed_limit(actual_speed, max_speed):
    speed_limit_violation = actual_speed > max_speed * 1.2 and actual_speed < max_speed * 1.5
    return speed_limit_violation

def find_speed_limit_violators(driver_speeds, max_speed):
    violators = []
    for driver_speed in driver_speeds:
        if check_speed_limit(driver_speed, max_speed):
            violators.append(driver_speed)
    return len(violators), violators

# Example usage:
max_speed = 60  # Maximum speed allowed for the road
driver_speeds = [80, 75, 65, 90, 100, 70]  # List of actual speeds of drivers
num_violators, violators = find_speed_limit_violators(driver_speeds, max_speed)
print(f"Number of violators: {num_violators}")
print("Violators:", violators)

