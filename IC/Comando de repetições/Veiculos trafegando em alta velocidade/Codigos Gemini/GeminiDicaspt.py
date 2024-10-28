# Pega o limite de velocidade da via
limite_velocidade = float(input("Insira o limite de velocidade da via (km/h): "))

# Cria um vetor com os registros de velocidade dos carros
registros_velocidade = list(map(float, input("Insira os registros de velocidade dos carros (km/h), separados por espaço: ").split()))

# Variável acumuladora para contar as infrações
infracoes = 0

# Percorre o vetor de registros de velocidade
for i, velocidade in enumerate(registros_velocidade):
    # Verifica se a velocidade é mais de 20% e menos que 50% acima do limite
    if velocidade > limite_velocidade * 1.2 and velocidade < limite_velocidade * 1.5:
        # Imprime a posição do motorista que infringiu a velocidade
        print(i + 1)
        # Incrementa a variável acumuladora
        infracoes += 1

# Imprime a quantidade de motoristas que infringiram o limite
print(f"\nQuantidade de motoristas que infringiram o limite: {infracoes}")
