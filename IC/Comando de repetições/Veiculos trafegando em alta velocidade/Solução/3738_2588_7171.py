#trafego
from numpy import*

vet = array(eval(input()))

cont=0
lim= vet[0]
lmax= lim + (lim*0.5)
lmin= lim + (lim*0.2)

for i in range(1,size(vet)):
	if ((vet[i]>lmin) and (vet[i]<lmax)):
		print(i)
		cont= cont +1
print(cont)
