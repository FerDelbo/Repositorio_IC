from numpy import*
import collections
v = array(eval(input()))
v2 = []

for i in range(size(v)):
	a = 0.2*v[0]+v[0]
	b = 0.5*v[0]+v[0]
	if (v [i] > a) and (v [i] < b):
		v2.append(i)
		print(i)
print(size(v2))
	
