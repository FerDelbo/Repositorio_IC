from numpy import*
v= array(eval(input()))
lim= v[0]
inf= 0
lmin= (lim*0.2)+lim
lmax= (lim*0.5)+lim
for i in range(1,size(v)):
	if lmin<v[i]<lmax:
		print(i)
		inf = inf+1
print(inf)
		
		


		
	
		