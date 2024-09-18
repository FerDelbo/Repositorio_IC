# filename: data_extenso.py
data = input()  # dd/mm/yyyy

dia = int(data[:2]) 
mes = int(data[2:4])
ano = int(data[4:])

meses = {
    1: 'janeiro',
    2: 'fevereiro',
    3: 'março',
    4: 'abril',
    5: 'maio',
    6: 'junho',
    7: 'julho',
    8: 'agosto',
    9: 'setembro',
    10: 'outubro',
    11: 'novembro',
    12: 'dezembro'
}

print(f'{dia:02d} de {meses[mes]} de {ano}')
