def media_poderada(nota1, nota2, nota3, nota4):
    nota1 * 1
    nota2 * 2
    nota3 * 3
    nota4 * 4
    resultado = nota1+nota2+nota3+ nota4 / 10
    return resultado

n1 = input("Insira a primeira nota: ")
n2 = input("Insira a segunda nota: ")
n3 = input("Insira a terceira nota: ")
n4 = input("Insira a quarta nota: ")

print(media_poderada(n1, n2, n3, n4))

#Maneira mais rapida e efciente
# i = 1
# resultado = 0
# while(i <= 4):
#     nota = input(f"Insira a nota {i}: ")
#     resultado = resultado +  (float(nota) * i)
#     i= i + 1
# print(resultado)

#Possiveis casos de teste que podemos testar
