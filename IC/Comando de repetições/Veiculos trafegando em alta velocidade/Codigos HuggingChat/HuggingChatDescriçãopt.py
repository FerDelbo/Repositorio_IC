# List of motorists with their speed and speed limit
motorists = [
    {'speed': 80, 'limit': 60},
    {'speed': 120, 'limit': 80},
    {'speed': 90, 'limit': 70},
    {'speed': 110, 'limit': 80},
    # Add more data as needed
]

# Initialize counters
count_infractions = 0
count_total = 0

# Iterate over each motorist
for motorist in motorists:
    # Calculate how much the motorist exceeded the speed limit
    excess_speed = motorist['speed'] - motorist['limit']

    # Check if the motorist exceeded the speed limit
    if excess_speed > 0:
        # Calculate how much the speed limit was exceeded
        excess_percentage = (excess_speed / motorist['limit']) * 100

        # Check if the excess speed was between 20% and 50%
        if 20 < excess_percentage < 50:
            # Increment the counter for infractions
            count_infractions += 1

        # Increment the total counter
        count_total += 1

# Print the results
print(f"There were {count_infractions} motorists who infringed the speed limit between 20% and 50%.")
print(f"This accounts for {count_infractions / count_total * 100}% of all motorists.")
