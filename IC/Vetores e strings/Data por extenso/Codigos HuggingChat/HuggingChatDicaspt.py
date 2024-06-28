
Here's the plan:
1. Define a dictionary to map month numbers to their names in Portuguese.
2. Prompt the user to enter a date in the "ddmmaaaa" format.
3. Extract the day, month, and year from the input string.
4. Use the dictionary to get the month name based on the month number.
5. Print the date in the desired format.

Let's execute the code.

```python
# Define the dictionary for month names
month_names = {
    '01': 'janeiro',
    '02': 'fevereiro',
    '03': 'marco',
    '04': 'abril',
    '05': 'maio',
    '06': 'junho',
    '07': 'julho',
    '08': 'agosto',
    '09': 'setembro',
    '10': 'outubro',
    '11': 'novembro',
    '12': 'dezembro'
}

# Prompt the user to enter a date
date_input = input("Enter a date in the format 'ddmmaaaa': ")

# Extract the day, month, and year
day = date_input[:2]
month = date_input[2:4]
year = date_input[4:]

# Get the month name
month_name = month_names[month]

# Print the date in full text format
print(f"{day} de {month_name} de {year}")
```

The user will need to run this code and provide the input date in the requested format. The program will then output the date in full text format.

Let's wait for the user to execute the code and provide us with the output.
