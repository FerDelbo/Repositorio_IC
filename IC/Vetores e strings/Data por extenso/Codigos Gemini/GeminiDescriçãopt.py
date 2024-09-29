def data_por_extenso(data):
  """Converte uma data no formato "ddmmaaaa" para extenso."""

  meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho",
           "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

  dia = int(data[:2])
  mes = int(data[2:4]) - 1
  ano = int(data[4:])

  return f"{dia} de {meses[mes]} de {ano}"


# Lê a data do usuário
data = input("Digite uma data no formato \"ddmmaaaa\": ")

# Converte a data para extenso
data_extenso = data_por_extenso(data)

# Imprime a data por extenso
print(data_extenso)
