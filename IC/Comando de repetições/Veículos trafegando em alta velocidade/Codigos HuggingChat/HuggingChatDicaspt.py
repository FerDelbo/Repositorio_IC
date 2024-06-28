
Here is the Python code:

```python
def speed_violations(speed_records):
    max_speed = speed_records[0]
    violations = []
    for i in range(1, len(speed_records)):
        current_speed = speed_records[i]
        if current_speed > max_speed * 1.2 and current_speed < max_speed * 1.5:
            violations.append(i)
    return violations, len(violations)

speed_records = [100, 110, 125, 130, 140, 150, 160, 170, 180]
violations, count = speed_violations(speed_records)
for violation in violations:
    print(violation)
print("Total violations:", count)
```

This program defines a function called `speed_violations` that takes a list of speed records as input. The maximum speed is the first element in the list. The function iterates over the remaining elements in the list, checking if the current speed is more than 20% and less than 50% above the maximum speed. If it is, it adds the position of the current speed in the list to the `violations` list.

After defining the function, the program creates a sample list of speed records and calls the `speed_violations` function with this list. The function returns the `violations` list and the count of violations. The program prints each position in the `violations` list and the total number of violations.

Please save the code in a Python file and execute it.
