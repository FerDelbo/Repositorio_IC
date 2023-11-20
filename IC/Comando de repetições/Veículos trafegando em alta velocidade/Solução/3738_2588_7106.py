from numpy import *

vel = array(eval(input()))

vmin = vel[0] + (vel[0] * (20/100))
vmax = vel[0] + (vel[0] * (50/100))
a = 0

for i in range (size(vel)):
	
	if(vel[i] > vmin and vel[i] <vmax):
		print(i)
		a = a +1 
		
print(a)
