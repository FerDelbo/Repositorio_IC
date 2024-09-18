# Leia as quatro notas do aluno
nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
nota4 = float(input())

# Calcule a média ponderada
media_ponderada = round((nota1 * 1 + nota2 * 2 + nota3 * 3 + nota4 * 4) / (1 + 2 + 3 + 4), 1)

# Imprima a média ponderada
print(media_ponderada)
