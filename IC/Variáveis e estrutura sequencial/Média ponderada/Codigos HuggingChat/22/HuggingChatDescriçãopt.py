# Initialize the weights
weights = [1, 2, 3, 4]

# Initialize the total weight
total_weight = sum(weights)

# Ask the user for the notes
notes = [float(input(f"Enter note {i+1}: ")) for i in range(4)]

# Calculate the weighted average
weighted_average = sum([notes[i] * weights[i] for i in range(4)]) / total_weight

print(f"The weighted average is: {weighted_average}")

This program will ask the user to input the four notes one by one. Then, it will calculate the weighted average using the given weights and print it out.