# Criar uma lista de velocidades de motoristas
velocidades = [80, 95, 110, 125, 75, 90, 105, 130]

# Definir o limite de velocidade
limite_velocidade = 100

# Criar uma lista para armazenar os motoristas que infringiram o limite
infratores = []

# Iterar sobre as velocidades
for velocidade in velocidades:

    # Calcular a porcentagem acima do limite de velocidade
    porcentagem_acima = (velocidade - limite_velocidade) / limite_velocidade * 100

    # Verificar se a porcentagem acima do limite está entre 20% e 50%
    if 20 <= porcentagem_acima < 50:
        infratores.append(velocidade)

# Exibir a lista de infratores
print("Motoristas que infringiram o limite de velocidade em mais de 20% e menos que 50% acima da velocidade máxima permitida:")
print(infratores)

# Contar o número de infratores
num_infratores = len(infratores)

# Exibir o número de infratores
print("Número de motoristas infratores:", num_infratores)
