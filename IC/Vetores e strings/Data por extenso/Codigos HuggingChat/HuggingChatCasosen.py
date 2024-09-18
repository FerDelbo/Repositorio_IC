from datetime import datetime

def convert_date(date_string):
    date_object = datetime.strptime(date_string, '%d%m%Y')
    formatted_date = date_object.strftime('%B %d, %Y')
    return formatted_date

# Test the function with the given input
input_date = '01092023'
output_date = convert_date(input_date)
print(output_date)
