1. Define a function `find_speed_violators` that takes in the input list of speeds and calculates the speed limit based on the first value in the list.
2. Iterate through the rest of the list, checking if each speed is more than 20% and less than 50% above the speed limit.
3. If a speed violates the limit, print its position in the list (1-indexed) and increment a counter.
4. After iterating through the list, print the total number of violators.

Here's the Python code for the user to execute:

```python
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

    print("Number of violators:", violators_count)

# Test the function with example input
speeds = [60, 65, 70, 80, 100, 120, 130]
find_speed_violators(speeds)
```

This code block defines the function `find_speed_violators` and tests it with an example input. The user can replace the `speeds` list with their actual input data. The function will print the position of each violator and the total number of violators.

After the execution, if the result shows the correct output, everything is done.

