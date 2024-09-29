from numpy import *

v = array(eval(input()))

m20 = v[0] + (v[0] * (20/100))
m50 = v[0] + (v[0] * (50/100))
c = 0

for i in range(size(v)):
	
	if(v[i] > m20 and v[i] < m50):
		print(i)
		c = c + 1
		
print(c)