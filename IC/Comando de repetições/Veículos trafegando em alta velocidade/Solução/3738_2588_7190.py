from numpy import *

v = array(eval(input()))
o = 0
i = 1
x =v[0] + (20/100*v[0])
y =v[0] + (50/100*v[0])

for i in range(size(v)):
	
	if(x<v[i]<y):
		print(i)
		o = o + 1
	i = i+1
	
print(o)
