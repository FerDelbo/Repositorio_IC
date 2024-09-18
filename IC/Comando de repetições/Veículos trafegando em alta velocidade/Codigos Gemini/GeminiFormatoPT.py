# filename: speed_ticket.py

def infringiu_velocidade(limite_velocidade: float, velocidade_medida: float) -> bool:
    porcentagem = (velocidade_medida - limite_velocidade) / limite_velocidade * 100
    return 20 <= porcentagem < 50

if __name__ == "__main__":
    with open('velocidades.txt', 'r') as f:
        velocidades = [float(velocidade) for velocidade in f.readlines()]
    limite_velocidade = velocidades[0]
    infratores = [i for i, velocidade in enumerate(velocidades[1:], 1) if infringiu_velocidade(limite_velocidade, velocidade)]
    print(f"Motoristas infratores: {infratores}")
    print(f"Quantidade de motoristas infratores: {len(infratores)}")
