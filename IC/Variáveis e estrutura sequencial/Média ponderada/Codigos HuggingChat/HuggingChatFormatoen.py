# Read four notes from the student
note1 = float(input("Enter the first note: "))
note2 = float(input("Enter the second note: "))
note3 = float(input("Enter the third note: "))
note4 = float(input("Enter the fourth note: "))

# Calculate the weighted average
weighted_average = (note1 * 1 + note2 * 2 + note3 * 3 + note4 * 4) / (1 + 2 + 3 + 4)

# Round the result to one decimal place
weighted_average_rounded = round(weighted_average, 1)

# Print the weighted average
#print("The weighted average is:", weighted_average_rounded)
print(weighted_average_rounded)