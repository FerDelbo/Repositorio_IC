# filename: infratores.py
limite = float(input("Qual o limite de velocidade? "))
velocidades = [float(v) for v in input("Quais as velocidades medidas? ").split()]
infractores = []
qtd_infracoes = 0

for v in velocidades[1:]:
    if (v - limite) / limite > 0.2 and (v - limite) / limite < 0.5:
        infractores.append(velocidades.index(v))
        qtd_infracoes += 1

print("Posições dos motoristas que infringiram a velocidade:")
for i in infractores:
    print(i)
print("Quantidade de motoristas que infringiram a velocidade:", qtd_infracoes)
