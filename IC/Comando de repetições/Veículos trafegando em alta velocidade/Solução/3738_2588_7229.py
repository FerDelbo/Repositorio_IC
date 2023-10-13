from numpy import*

rvel = array(eval(input()))

limite = rvel[0]
lmin = limite * 0.2 + limite 
lmax = limite * 0.5 + limite
contador = 0

for i in range (1,size(rvel)):
	if rvel[i]>lmin and rvel[i]<lmax:
		print(i)
		contador = contador + 1

print(contador)
