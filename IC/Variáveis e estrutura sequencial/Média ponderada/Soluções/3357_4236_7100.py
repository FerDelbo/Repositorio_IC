nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
nota3 = float(input("Terceira nota: "))
nota4 = float(input("Quarta nota: "))

from math import *

mp = (1*nota1 + 2*nota2 + 3*nota3 + 4*nota4) / (1 + 2 + 3 + 4)

print(round(mp, 2))