from numpy import*
v = array(eval(input()))
lim1 = v[0] + 0.20 * v[0]
lim2 = v[0] + 0.50 * v[0]
cont=0

for i in range(1,size(v)):
	if v[i] > lim1 and v[i]< lim2:
		print(i)
		cont=cont + 1
print(cont)
	
