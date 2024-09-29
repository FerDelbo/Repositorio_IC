from numpy import*
v = array(eval(input()))
i = 0 
li = v[0]+(v[0]*0.2)
ls = v[0]+(v[0]*0.5)
for j in range(1,size(v)):
	if (li<v[j]<ls):
		i = i + 1
		print(j)
	else:
		i = i + 0
print(i)
