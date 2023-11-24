def ddmmyyyy_to_words(date):
    # Split the date into separate digits for each component (day, month, year)
    day = date[0:2]
    month = date[2:4]
    year = date[4:8]
    meses = {
    "01": "janeiro", "02": "fevereiro", "03": "março", "04": "abril",
    "05": "maio", "06": "junho", "07": "julho", "08": "agosto",
    "09": "setembro", "10": "outubro", "11": "novembro", "12": "dezembro"
}
    # Print the result
    print(f"{day} {meses[month]} {year}")

date = input("Enter the date in format 'ddmmyyyy': ")
ddmmyyyy_to_words(date)