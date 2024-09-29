from numpy import*

v = array(eval(input()))

cont= 0

i1 = v[0] + v[0]*0.2
i2 = v[0] + v[0]*0.5


for i in range(1, size(v)):
	
	if(v[i] > i1 and v[i] <i2):
		cont=cont +1
		print(i)


print(cont)