# This is a python code block

# Read the four grades
grade1 = float(input("Enter the first grade: "))
grade2 = float(input("Enter the second grade: "))
grade3 = float(input("Enter the third grade: "))
grade4 = float(input("Enter the fourth grade: "))

# Calculate the weighted average
weighted_average = ((grade1 * 1) + (grade2 * 2) + (grade3 * 3) + (grade4 * 4)) / (1 + 2 + 3 + 4)

# Print the weighted average rounded to one decimal place
#print("The weighted average is:", round(weighted_average, 1))
print(round(weighted_average, 1))