# filename: dataextenso.py
meses = ['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
dias_semana = ['segunda-feira', 'terca-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira', 'sabado', 'domingo']

def data_por_extenso(data):
  dia = int(data[:2])
  mes = int(data[2:4]) - 1
  ano = int(data[4:])
  return f'{dia} de {meses[mes]} de {ano}'

data = input('Informe a data no formato "ddmmaaaa": ')
print(data_por_extenso(data))
