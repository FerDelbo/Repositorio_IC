from numpy import*
v = array(eval(input()))
x=v[0]
x1=v[0]+(v[0]*0.20)
x2=v[0]+(v[0]*0.50)
y=0
for i in range(size(v)):
	if(v[i]>x1 and v[i]<x2):
		y=y+1
		print(i)
	else:
		y=y
print(y)
