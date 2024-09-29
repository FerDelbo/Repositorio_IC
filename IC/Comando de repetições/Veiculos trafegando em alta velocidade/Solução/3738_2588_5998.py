from numpy import *
v = array(eval(input()))
ultrapassou20 = 0

limite_inferior = v[0]+(v[0]*0.2)

for i in range(1,size(v)):
	if v[0]+(v[0]*0.2)<v[i]<v[0]+(v[0]*0.5):
		ultrapassou20 = ultrapassou20 + 1
		print(i)
	else:
		ultrapassou20 = ultrapassou20 + 0
print(ultrapassou20)
