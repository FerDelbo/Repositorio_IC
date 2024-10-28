def verifica_infracao(velocidades, limite):
  """Verifica quais motoristas infringiram o limite de velocidade em mais de 20% e menos que 50% acima da velocidade máxima permitida.

  Args:
    velocidades: Vetor com os registros de velocidade dos carros.
    limite: Limite de velocidade máxima da via.

  Returns:
    Lista com as posições dos motoristas que infringiram o limite de velocidade.
  """

  # Calcula 20% e 50% acima do limite de velocidade
  limite_20 = limite * 1.2
  limite_50 = limite * 1.5

  # Verifica quais motoristas infringiram o limite
  infratores = []
  for i, velocidade in enumerate(velocidades[1:]):
    if velocidade > limite_20 and velocidade <= limite_50:
      infratores.append(i + 1)

  return infratores


def main():
  # Lê o limite de velocidade da via
  limite = int(input("Informe o limite de velocidade da via: "))

  # Lê os registros de velocidade dos carros
  velocidades = list(map(int, input("Informe os registros de velocidade dos carros (separados por espaço): ").split()))

  # Verifica quais motoristas infringiram o limite
  infratores = verifica_infracao(velocidades, limite)

  # Imprime as posições dos motoristas que infringiram o limite
  for infrator in infratores:
    print(infrator)

  # Imprime a quantidade de motoristas que infringiram o limite
  print(f"Quantidade de motoristas que infringiram o limite: {len(infratores)}")


if __name__ == "__main__":
  main()
