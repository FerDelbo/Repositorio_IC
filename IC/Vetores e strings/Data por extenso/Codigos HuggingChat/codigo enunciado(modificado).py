def date_to_words(date):
    day = date[0:2]
    month = {
        "01":"Jan",
        "02":"Feb",
        "03":"Mar",
        "04":"Apr",
        "05":"May",
        "06":"Jun",
        "07":"Jul",
        "08":"Aug",
        "09":"Sep",
        "10":"Oct",
        "11":"Nov",
        "12":"Dec",
    }
    month_index = date[2:4]
    m = month[month_index]
    year = date[4:8]
    return f"{day} de {m} de {year}"
    

d = str(input("Enter the date in the format 'ddmmyyyy': ")) 
print(date_to_words(d))
