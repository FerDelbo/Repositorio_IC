def Data_por_extenso(ddmmaaaa):
    dia = ddmmaaaa[0] + ddmmaaaa[1]
    mes =  ddmmaaaa[2] + ddmmaaaa[3]
    ano = ddmmaaaa[4] + ddmmaaaa[5] + ddmmaaaa[6] + ddmmaaaa[7]#Concatenando strings
    meses = {"01": "Janeiro",
             "02": "Fevereiro",
             "03": "Marco",
             "04": "Abril",
             "05": "Maio",
             "06": "Junho",
             "07": "Julho",
             "08": "Agosto",
             "09": "Setembro",
             "10": "Outubro",
             "11": "Novembro",
             "12": "Dezembro"}
    print(f"{dia} de {meses[mes]} de {ano}")

entrada = str(input("Informe a data em numeros no formato 'ddmmaaaa': "))
Data_por_extenso(entrada)

#Possiveis casos de teste que podem ser testados