# Read the input date
date_input = input("Enter the date (ddmmaaaa): ")

# Extract day, month, and year
day = int(date_input[:2])
month = date_input[2:4]
year = int(date_input[4:])

# Create a dictionary to map month numbers to names
months = {
    "01": "January", "02": "February", "03": "March", "04": "April",
    "05": "May", "06": "June", "07": "July", "08": "August",
    "09": "September", "10": "October", "11": "November", "12": "December"
}

# Convert the month number to a month name
month_name = months[month]

# Print the date in the desired format
print(f"{day} de {month_name} de {year}")