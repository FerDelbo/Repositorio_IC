from numpy import*

soma = 0

v = array(eval(input()))

lmin = v[0] + 0.20 * v[0]
lmax = v[0] + 0.50 * v[0]
for i in range(1, size(v)):
	if(v[i] > lmin and v[i] < lmax):
		print(i)
		soma = soma + 1
print(soma)
