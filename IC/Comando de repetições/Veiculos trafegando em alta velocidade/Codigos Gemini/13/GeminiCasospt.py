# Função para verificar se o motorista infringiu o limite de velocidade
def infringiu_limite(velocidade_medida, limite_velocidade):
    porcentagem_acima = (velocidade_medida - limite_velocidade) / limite_velocidade * 100
    return 20 <= porcentagem_acima < 50

# Entrada de dados
velocidades = list(map(float, input().split()))
limite_velocidade = velocidades[0]
del velocidades[0]  # Remove o limite de velocidade da lista

# Variável acumuladora para contar as infrações
infracoes = 0

# Percorre a lista de velocidades e verifica as infrações
for velocidade in velocidades:
    if infringiu_limite(velocidade, limite_velocidade):
        print(velocidades.index(velocidade) + 1)  # Imprime a posição do motorista que infringiu
        infracoes += 1

# Imprime a quantidade de infrações
print(infracoes)
