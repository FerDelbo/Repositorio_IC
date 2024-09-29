from numpy import *

v = array(eval(input()))

# Variavel loop

n = 0 # numero de infracoes

for i in range(size(v)):
	
	if (v[i] < (v[0] + v[0] * 0.50) and v[i] > (v[0] + v[0] * 0.20)):
		
		print (i)
		n = n + 1
		
	

print (n)