def get_month_name(month_num):
    months = {
        "01": "janeiro",
        "02": "fevereiro",
        "03": "março",
        "04": "abril",
        "05": "maio",
        "06": "junho",
        "07": "julho",
        "08": "agosto",
        "09": "setembro",
        "10": "outubro",
        "11": "novembro",
        "12": "dezembro"
    }
    return months[month_num]

def get_day_name(day_num):
    days = {
        "01": "primeiro",
        "02": "segundo",
        "03": "terceiro",
        "04": "quarto",
        "05": "quinto",
        "06": "sexto",
        "07": "sétimo",
        "08": "oitavo",
        "09": "nono",
        "10": "décimo",
        "11": "décimo primeiro",
        "12": "décimo segundo",
        "13": "décimo terceiro",
        "14": "décimo quarto",
        "15": "décimo quinto",
        "16": "décimo sexto",
        "17": "décimo sétimo",
        "18": "décimo oitavo",
        "19": "décimo nono",
        "20": "vigésimo",
        "21": "vigésimo primeiro",
        "22": "vigésimo segundo",
        "23": "vigésimo terceiro",
        "24": "vigésimo quarto",
        "25": "vigésimo quinto",
        "26": "vigésimo sexto",
        "27": "vigésimo sétimo",
        "28": "vigésimo oitavo",
        "29": "vigésimo nono",
        "30": "trigésimo",
        "31": "trigésimo primeiro"
    }
    return days[day_num]

# Get date input from user
date_input = input("Digite a data no formato 'ddmmaaaa': ")

# Parse date
day = date_input[:2]
month = date_input[2:4]
year = date_input[4:]

# Get full month and day names
full_month_name = get_month_name(month)
full_day_name = get_day_name(day)

# Print full date
print(f"{full_day_name} de {full_month_name} de {year}")