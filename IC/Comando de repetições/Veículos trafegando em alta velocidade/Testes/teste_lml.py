def verifica_infracoes(velocidades):
    limite_maximo = velocidades[0]
    infratores = []

    for i in range(1, len(velocidades)):
        velocidade_registrada = velocidades[i]
        limite_superior = limite_maximo * 1.5  # Limite superior é 50% acima do limite máximo
        limite_inferior = limite_maximo * 1.2  # Limite inferior é 20% acima do limite máximo

        if velocidade_registrada > limite_inferior and velocidade_registrada <= limite_superior:
            infratores.append(i)

    return infratores
 
recebe_vetor = input() 
velocidades = []
infratores = verifica_infracoes(velocidades.append(recebe_vetor))

if len(infratores) > 0:
    print("Motoristas que infringiram o limite de velocidade:")
    for i in infratores:
        print(f"Motorista na posição {i} com velocidade {velocidades[i]} km/h")

    print(f"Total de motoristas infratores: {len(infratores)}")
else:
    print("Nenhum motorista infringiu o limite de velocidade.")