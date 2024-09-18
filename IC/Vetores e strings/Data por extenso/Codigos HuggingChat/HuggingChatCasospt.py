from datetime import datetime
import calendar

# Ler a entrada do usuário
data = input("Digite a data no formato 'ddmmaaaa': ")

# Converter a entrada para um objeto datetime
data_obj = datetime.strptime(data, "%d%m%Y")

# Obter o nome do mês por extenso
nome_mes = calendar.month_name[data_obj.month]

# Formatar a data por extenso
data_por_extenso = data_obj.strftime("%d") + " de " + nome_mes + " de " + data_obj.strftime("%Y")

# Imprimir a data por extenso
print(data_por_extenso)
