def verificar_infracoes(velocidades, limite_velocidade):
    """
    Determina quais e quantos motoristas infringiram o limite de velocidade em mais de 20% e menos que 50% acima da velocidade máxima permitida.

    Parâmetros:
        velocidades (lista): Lista das velocidades dos motoristas em km/h.
        limite_velocidade (int): Limite de velocidade em km/h.

    Retorna:
        lista: Lista com os nomes dos motoristas que infringiram o limite de velocidade dentro da faixa especificada.
    """
    # Calcula a faixa de velocidade que representa uma infração de mais de 20% e menos que 50% acima do limite.
    faixa_infracao = (1 + 20 / 100) * limite_velocidade, (1 + 50 / 100) * limite_velocidade

    # Cria uma lista para armazenar os nomes dos motoristas infratores.
    motoristas_infratores = []

    # Itera sobre as velocidades dos motoristas.
    for velocidade in velocidades:
        # Verifica se a velocidade está dentro da faixa de infração.
        if faixa_infracao[0] < velocidade < faixa_infracao[1]:
            # Adiciona o nome do motorista à lista de infratores.
            motoristas_infratores.append(velocidade)

    # Retorna a lista de motoristas infratores.
    return motoristas_infratores


# Exemplo de uso
velocidades = [80, 100, 120, 150, 90, 110, 130]
limite_velocidade = 100

motoristas_infratores = verificar_infracoes(velocidades, limite_velocidade)

print("Motoristas que infringiram o limite de velocidade em mais de 20% e menos que 50%:")
for motorista in motoristas_infratores:
    print(f"- {motorista} km/h")
