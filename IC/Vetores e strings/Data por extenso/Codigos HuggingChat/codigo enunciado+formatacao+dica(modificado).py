def ddmmyyyy_to_words(date):
    """Convert a date in the format 'ddmmyyyy' to words."""
    day = int(date[0:2])
    meses = {
    "01": "janeiro", "02": "fevereiro", "03": "março", "04": "abril",
    "05": "maio", "06": "junho", "07": "julho", "08": "agosto",
    "09": "setembro", "10": "outubro", "11": "novembro", "12": "dezembro"}
    #month = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}[month]
    year = int(date[4:])
    m = meses[date[2:4]]
    # Format the output string
    output = f"{day} of {m}, {year}"
    
    return output

d = input("Enter the date of format 'ddmmyyyy': ")
print(ddmmyyyy_to_words(d))