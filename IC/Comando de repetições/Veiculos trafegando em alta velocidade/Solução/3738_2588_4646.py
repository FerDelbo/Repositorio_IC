from numpy import*
v = array(eval(input()))
l = v[0]
k = 0
lmin = l+(l*0.20)
lmax = l+(l*0.50)
for i in range(1,size(v)):
	if(v[i] > lmin and v[i] < lmax):
		print(i)
		k = k+1
print(k)
	
