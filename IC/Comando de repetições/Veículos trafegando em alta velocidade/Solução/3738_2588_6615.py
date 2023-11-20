from numpy import*
v = array(eval(input()))
j= 0
Lim = v[0]
liM = Lim + (Lim * 0.50)
lim = Lim + (Lim * 0.20)
for i in range(1,size(v)):
	if(lim<v[i]<liM):
		print(i)	
		j = j +1
print(j)
