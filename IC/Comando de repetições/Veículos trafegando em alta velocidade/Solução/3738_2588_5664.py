from numpy import *

vet = array(eval(input()))

l1=vet[0]+vet[0]*20/100
l2=vet[0]+vet[0]*50/100

cont=0
for i in range(size(vet)):
	if l1<vet[i]<l2:
		cont = cont + 1
		print(i)
print(cont)
