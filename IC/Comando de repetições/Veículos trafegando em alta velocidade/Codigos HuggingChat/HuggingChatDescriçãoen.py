1. Use Python code to define a function that takes in the actual speed of the driver and the maximum speed allowed, and checks if the driver violated the speed limit by more than 20% and less than 50%.
2. Use the function to process a list of driver speeds and determine which and how many drivers violated the speed limit within the given range.

Step 1: Define the function to check the speed limit violation.
```python
def check_speed_limit(actual_speed, max_speed):
    speed_limit_violation = actual_speed > max_speed * 1.2 and actual_speed < max_speed * 1.5
    return speed_limit_violation
```

Step 2: Process a list of driver speeds and determine the violators.
```python
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
```

