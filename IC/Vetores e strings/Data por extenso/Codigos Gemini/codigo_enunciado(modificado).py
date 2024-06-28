
def converte_data(data):
  dia = data[0:2]
  mes = data[2:4]
  ano = data[4:]


  # Converte o mês para extenso
  meses = {
    1: "janeiro",
    2: "fevereiro",
    3: "março",
    4: "abril",
    5: "maio",
    6: "junho",
    7: "julho",
    8: "agosto",
    9: "setembro",
    10: "outubro",
    11: "novembro",
    12: "dezembro"
  }

  return f"{dia} de {meses[int(mes)]} de {ano}"


# Lê a data do usuário
data = input("Digite uma data no formato ddmmaaaa: ")

# Converte a data e imprime o resultado
data_por_extenso = converte_data(data)
print(data_por_extenso);