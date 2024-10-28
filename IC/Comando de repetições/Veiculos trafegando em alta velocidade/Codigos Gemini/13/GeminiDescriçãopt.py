# Lista de velocidades registradas
velocidades_registradas = [65, 70, 80, 90, 100, 110, 120, 130, 140, 150]

# Velocidade máxima permitida
velocidade_maxima = 80

# Calcula a porcentagem de excesso de velocidade para cada motorista
excesso_porcentagem = [(v - velocidade_maxima) / velocidade_maxima * 100 for v in velocidades_registradas]

# Cria um dicionário para armazenar os motoristas infratores e seus excessos de velocidade
motoristas_infratores = {}

# Itera sobre as porcentagens de excesso de velocidade
for excesso in excesso_porcentagem:
    # Verifica se o motorista infringiu o limite de velocidade em mais de 20% e menos que 50%
    if 20 <= excesso < 50:
        # Adiciona o motorista ao dicionário, se ainda não estiver presente
        if velocidades_registradas[excesso_porcentagem.index(excesso)] not in motoristas_infratores:
            motoristas_infratores[velocidades_registradas[excesso_porcentagem.index(excesso)]] = []
        # Adiciona o excesso de velocidade à lista de excessos do motorista
        motoristas_infratores[velocidades_registradas[excesso_porcentagem.index(excesso)]].append(excesso)

# Imprime os motoristas infratores e seus excessos de velocidade
for motorista, excessos in motoristas_infratores.items():
    print(f"Motorista com velocidade {motorista} km/h excedeu o limite em:")
    for excesso in excessos:
        print(f" - {excesso:.2f}%")
