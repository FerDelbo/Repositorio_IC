from numpy import*
vet = array(eval(input()))
infra=0
lim= vet[0]
limax= lim+(lim*0.5)
limim= lim+(lim*0.2)
for i in range(1,size(vet)):
	if limim < vet[i] < limax:
		print(i)
		infra= infra + 1
	
print(infra)
