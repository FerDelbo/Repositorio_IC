# Recebe o limite de velocidade e as velocidades medidas
limite_velocidade = float(input("Informe o limite de velocidade da via: "))
velocidades = list(map(float, input("Informe as velocidades medidas separadas por espaço: ").split()))

# Inicializa o acumulador de infrações
infracoes = 0

# Itera sobre as velocidades medidas
for velocidade in velocidades[1:]:
    # Verifica se a velocidade é maior que 20% e menor que 50% acima do limite
    if velocidade > limite_velocidade * 1.2 and velocidade < limite_velocidade * 1.5:
        # Imprime a posição do motorista que infringiu
        print(velocidades.index(velocidade) + 1)
        # Incrementa o acumulador de infrações
        infracoes += 1

# Imprime a quantidade de infrações
print(f"Total de infrações: {infracoes}")
