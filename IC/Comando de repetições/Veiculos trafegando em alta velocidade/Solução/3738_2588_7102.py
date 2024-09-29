from numpy import *
v = array(eval(input()))
u = 0

li = v[0] + (v[0] * 0.2)

for i in range(1,size(v)):
	if v[0] + (v[0] * 0.2) < v[i] < v[0] + (v[0] * 0.5):
		
		u = u + 1
		print(i)
		
	else:
		
		u = u + 0
		
print(u)
