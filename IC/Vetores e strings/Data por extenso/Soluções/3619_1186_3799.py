#from numpy import*
v=input("v:")
dia=int(v[:2])
mes=int(v[2:4])
ano=int(v[4:])
if(mes==1):
	x="janeiro"
elif(mes==2):
	x="fevereiro"
elif(mes==3):
	x="marco"
elif(mes==4):
	x="abril"
elif(mes==5):
	x="maio"
elif(mes==6):
	x="junho"
elif(mes==7):
	x="julho"
elif(mes==8):
	x="agosto"
elif(mes==9):
	x="setembro"
elif(mes==10):
	x="outubro"
elif(mes==11):
	x="novembro"
elif(mes==12):
	x="dezembro"

print(dia,"de",x,"de",ano)

