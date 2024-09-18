def find_speed_violators(speeds):
    speed_limit = speeds[0]
    violators = []
    violators_count = 0

    for i in range(1, len(speeds)):
        if speeds[i] > speed_limit * 1.20 and speeds[i] < speed_limit * 1.50:
            violators.append(i + 1)  # 1-indexed position
            violators_count += 1

    for violator in violators:
        print(violator)

    #print("Number of violators:", violators_count) #cosigo original
    print(violators_count)

# Test the function with example input
#speeds = [60, 65, 70, 80, 100, 120, 130] #cosigo original
from numpy import*
speeds = array(eval(input()))
find_speed_violators(speeds)