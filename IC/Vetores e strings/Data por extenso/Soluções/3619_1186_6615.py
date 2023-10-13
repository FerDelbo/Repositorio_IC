data = input("data: ")
dia = data[:2]
ano = data[-4:]
mes = data[2:4]
if(mes=="01"):
	new_data = dia +" "+ "de janeiro de" +" "+ ano
elif(mes=="02"):
	new_data = dia +" "+ "de fevereiro de" +" "+ ano
elif(mes=="03"):
	new_data = dia +" "+ "de marco de" +" "+ ano
elif(mes=="04"):
	new_data = dia + " "+"de abril de" +" "+ ano
elif(mes=="05"):
	new_data = dia + " "+"de maio de" +" "+ ano
elif(mes=="06"):
	new_data = dia +" "+ "de junho de" +" "+ ano
elif(mes=="07"):
	new_data = dia +" "+ "de julho de" +" "+ ano
elif(mes=="08"):
	  new_data = dia +" "+ "de agosto de" +" "+ ano
elif(mes=="09"):
	  new_data = dia +" "+ "de setembro de" +" "+ ano
elif(mes=="10"):
	  new_data = dia +" "+ "de outubro de" +" "+ ano
elif(mes=="11"):
	  new_data = dia +" "+ "de novembro de" +" "+ ano
elif(mes=="12"):
	  new_data = dia +" "+ "de dezembro de" +" "+ ano
print(new_data)