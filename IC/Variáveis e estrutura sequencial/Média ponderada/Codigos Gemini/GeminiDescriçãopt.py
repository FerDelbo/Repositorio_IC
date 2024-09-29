# Ler as quatro notas do aluno
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

# Calcular a média ponderada
media_ponderada = (nota1 * 1 + nota2 * 2 + nota3 * 3 + nota4 * 4) / 10

# Imprimir a média ponderada
print(f"A média ponderada é: {media_ponderada}")
