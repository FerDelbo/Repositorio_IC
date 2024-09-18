# Read the four notes from the user
note1 = float(input("Enter the first note: "))
note2 = float(input("Enter the second note: "))
note3 = float(input("Enter the third note: "))
note4 = float(input("Enter the fourth note: "))

# Calculate the weighted sum
weighted_sum = note1 * 1 + note2 * 2 + note3 * 3 + note4 * 4

# Calculate the weighted average
weighted_average = weighted_sum / (1 + 2 + 3 + 4)

# Print the result
print("The weighted average is:", weighted_average)