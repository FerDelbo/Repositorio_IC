# Collect input from the user
grade1 = float(input("Enter the first grade: "))
grade2 = float(input("Enter the second grade: "))
grade3 = float(input("Enter the third grade: "))
grade4 = float(input("Enter the fourth grade: "))

# Calculate weighted average
weighted_average = round((grade1 * 1 + grade2 * 2 + grade3 * 3 + grade4 * 4) / (1 + 2 + 3 + 4), 1)

# Print the result
#print("The weighted average is:", weighted_average)
print(weighted_average)