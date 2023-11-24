#import datetime
import calendar

def data_por_extenso(data):
    try:
        dia = int(data[0:2])
        mes = int(data[2:4])
        ano = int(data[4:])
        
        
        # Obtém o nome do mês
        nome_mes = calendar.month_name[mes]#problema é estar em ingles 

        # Formata a data por extenso
        data_extenso = f"{dia} de {nome_mes} de {ano}"

        return data_extenso

    except ValueError as e:
        return str(e)

# Solicita a data ao usuário
data_input = input("Digite a data no formato 'ddmmaaaa': ")

# Chama a função para obter a data por extenso
data_extenso = data_por_extenso(data_input)

# Imprime a data por extenso
print("Data por extenso:", data_extenso)
