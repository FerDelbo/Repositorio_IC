# Dicionários para mapear números para palavras
meses = {
    "01": "janeiro", "02": "fevereiro", "03": "março", "04": "abril",
    "05": "maio", "06": "junho", "07": "julho", "08": "agosto",
    "09": "setembro", "10": "outubro", "11": "novembro", "12": "dezembro"
}

# Função para converter a data em formato "ddmmaaaa" para extenso
def data_por_extenso(data):
    dia = data[0:2]
    mes = data[2:4]
    ano = data[4:8]

    data_extenso = dia + " de " + meses[mes] + " de " + ano;
    return data_extenso

# Função principal
if __name__ == "__main__":
    data_input = input("Digite uma data no formato ddmmaaaa: ")
    
    if len(data_input) == 8 and data_input.isnumeric():
        data_extenso = data_por_extenso(data_input)
        print("Data por extenso:", data_extenso)
    else:
        print("Formato de data inválido. Por favor, insira uma data válida no formato ddmmaaaa.")
