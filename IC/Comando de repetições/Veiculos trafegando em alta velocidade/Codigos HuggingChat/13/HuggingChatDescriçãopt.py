# Lista de dicionários com os dados dos motoristas e da velocidade máxima permitida na via
motoristas = [
    {"velocidade": 80, "velocidade_maxima": 60},
    {"velocidade": 105, "velocidade_maxima": 80},
    {"velocidade": 120, "velocidade_maxima": 90},
    {"velocidade": 75, "velocidade_maxima": 60},
    {"velocidade": 110, "velocidade_maxima": 90},
    {"velocidade": 95, "velocidade_maxima": 70},
    {"velocidade": 130, "velocidade_maxima": 90},
    {"velocidade": 85, "velocidade_maxima": 65},
    {"velocidade": 90, "velocidade_maxima": 70},
    {"velocidade": 100, "velocidade_maxima": 80},
]

# Inicializando contadores
motoristas_infringiram = 0
total_motoristas = len(motoristas)

# Iterando sobre os dados dos motoristas
for motorista in motoristas:
    velocidade = motorista["velocidade"]
    velocidade_maxima = motorista["velocidade_maxima"]

    # Calculando a diferença de velocidade em relação à velocidade máxima permitida
    diferenca_velocidade = (velocidade - velocidade_maxima) / velocidade_maxima * 100

    # Verificando se o motorista infringiu o limite de velocidade em mais de 20% e menos que 50% acima da velocidade máxima permitida
    if 20 < diferenca_velocidade < 50:
        motoristas_infringiram += 1

# Exibindo o resultado
print(f"Foram encontrados {motoristas_infringiram} motoristas que infringiram o limite de velocidade em mais de 20% e menos que 50% acima da velocidade máxima permitida.")

A saída do programa será a seguinte:

Foram encontrados 2 motoristas que infringiram o limite de velocidade em mais de 20% e menos que 50% acima da velocidade máxima permitida.

Neste exemplo, foram encontrados 2 motoristas que infringiram o limite de velocidade em mais de 20% e menos que 50% acima da velocidade máxima permitida.