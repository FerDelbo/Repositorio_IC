from numpy import*
vel = array(eval(input()))

k=0
lim= vel[0]
lmax=lim + (0.2*lim)
lmin= lim +(0.5*lim)
for i in range(1,size(vel)):
	if (vel [i] > lmax) and (vel [i] < lmin):
		print(i)
		k=k+1
print(k)
		

