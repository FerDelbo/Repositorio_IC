from numpy import *

vet = array(eval(input()))

v20 = vet[0] + (vet[0] * (20/100))
v50 = vet[0] + (vet[0] * (50/100))
c = 0

for i in range(size(vet)):
	
	if(vet[i] > v20 and vet[i] < v50):
		print(i)
		c = c + 1
		
print(c)
