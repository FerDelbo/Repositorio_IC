#from numpy import *
data =input("Entre com a data: ")


dia= data[0:2]

if(data[2:4] == "01"): 
	mes="janeiro"
elif(data[2:4]== "02"):
	mes="fevereiro"
elif(data[2:4]== "03"):
	mes="marco"
elif(data[2:4]== "04"):
	mes="abril"
elif(data[2:4]== "05"):
	mes="maio"
elif(data[2:4]== "06"):
	mes="junho"
elif(data[2:4]== "07"):
	mes="julho"
elif(data[2:4]== "08"):
	mes="agosto"
elif(data[2:4]== "09"):
	mes="setembro"
elif(data[2:4]== "10"):
	mes="outubro"
elif(data[2:4]== "11"):
	mes="novembro"
elif(data[2:4]== "12"):
	mes="dezembro"

ano=data[4:]
print(dia,"de",mes,"de",ano)

