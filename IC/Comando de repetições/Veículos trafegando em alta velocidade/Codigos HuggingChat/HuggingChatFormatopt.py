
Here's the code:

```python
def find_speed_violators(speeds):
    max_speed = speeds[0]
    violators = []

    for i in range(1, len(speeds)):
        speed = speeds[i]
        limit_exceeded = speed > max_speed * 1.20
        limit_not_exceeded_by_50 = speed < max_speed * 1.50

        if limit_exceeded and limit_not_exceeded_by_50:
            violators.append(i)

    return violators, len(violators)

# Example usage:
speeds = [90, 100, 120, 140, 160, 180]
violators, violations_count = find_speed_violators(speeds)

print("Posições dos motoristas que infringiram o limite de velocidade:")
for violator in violators:
    print(violator)

print(f"\nTotal de motoristas que infringiram o limite: {violations_count}")
```

To use this script, simply replace the `speeds` list with the actual data. The output will display the position of each infringing driver in the list and the total number of infringements.

Now, please execute the code and provide the result so that I can verify the answer.

