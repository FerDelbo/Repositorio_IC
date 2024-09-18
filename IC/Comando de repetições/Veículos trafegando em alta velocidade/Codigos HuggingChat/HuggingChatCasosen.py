def find_speed_violations(speeds):
    speed_limit = speeds[0]
    violations = 0
    for i in range(1, len(speeds)):
        if speeds[i] > speed_limit * 1.2 and speeds[i] < speed_limit * 1.5:
            print(i)
            violations += 1
    print(violations)

# Test cases
#find_speed_violations([60.0, 73.9, 22.9, 72.1, 72.0, 100.6])
#find_speed_violations([11.6, 60.6, 16.6, 11.35])
#find_speed_violations([72.9, 29.1, 7.29, 90.7, 66.6])
find_speed_violations(eval(input()))
