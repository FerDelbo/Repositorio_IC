from datetime import datetime
import calendar

# Mapping month numbers to their names
months = {
    "01": "january",
    "02": "february",
    "03": "march",
    "04": "april",
    "05": "may",
    "06": "june",
    "07": "july",
    "08": "august",
    "09": "september",
    "10": "october",
    "11": "november",
    "12": "december"
}

# Get input
date_input = input("Enter a date in the format ddmmyyyy: ")

# Convert input to date object
date_obj = datetime.strptime(date_input, "%d%m%Y")

# Get day name
day_name = calendar.day_name[date_obj.weekday()]

# Print date in words
print(f"{day_name.lower()}, {date_obj.day} of {months[date_input[2:4]]}, {date_input[4:]}")

