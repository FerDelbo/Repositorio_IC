
```python
# Collect input from the user
grade1 = float(input("Enter the first grade: "))
grade2 = float(input("Enter the second grade: "))
grade3 = float(input("Enter the third grade: "))
grade4 = float(input("Enter the fourth grade: "))

# Calculate weighted average
weighted_average = round((grade1 * 1 + grade2 * 2 + grade3 * 3 + grade4 * 4) / (1 + 2 + 3 + 4), 1)

# Print the result
print("The weighted average is:", weighted_average)
```

Please execute this code and provide the output.

The user needs to input the four grades when prompted. The script will then calculate the weighted average and display it. The result will be rounded to one decimal place.

Additional information:
The formula for the weighted average is:
(grade1 * weight1 + grade2 * weight2 + grade3 * weight3 + grade4 * weight4) / (weight1 + weight2 + weight3 + weight4)
The weights in this case are 1, 2, 3, and 4 respectively. The result is rounded to one decimal place using the round() function.
