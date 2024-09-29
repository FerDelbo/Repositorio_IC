# filename: speed_violations.py

def check_speed_violations(speed_vector):
    max_speed = speed_vector[0]
    violations = []
    num_violations = 0

    for i in range(1, len(speed_vector)):
        current_speed = speed_vector[i]
        violation_range_min = max_speed * 1.2
        violation_range_max = max_speed * 1.5

        if current_speed > violation_range_min and current_speed < violation_range_max:
            violations.append(i)
            num_violations += 1

    for violation in violations:
        print(violation)

    print(num_violations)

# Example usage:
#speed_vector = [60, 70, 80, 90, 100, 110, 120]  # Replace this with your actual input data
from numpy import*
speed_vector = array(eval(input()))
check_speed_violations(speed_vector)