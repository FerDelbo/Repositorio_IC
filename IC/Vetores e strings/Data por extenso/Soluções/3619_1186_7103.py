#from numpy import*
data =input("Data: ")

dias = data[0:2]

if data[2:4]=="01":
	mes = "de janeiro de"
elif data[2:4]=="02":
	mes = "de fevereiro de"
elif data[2:4]=="03":
	mes = "de marco de"
elif data[2:4]=="04":
	mes = "de abril de"
elif data[2:4]=="05":
	mes = "de maio de"
elif data[2:4]=="06":
	mes = "de junho de"
elif data[2:4]=="07":
	mes = "de julho de"
elif data[2:4]=="08":
	mes = "de agosto de"
elif data[2:4]=="09":
	mes = "de setembro de"
elif data[2:4]=="10":
	mes = "de outubro de"
elif data[2:4]=="11":
	mes = "de novembro de"
elif data[2:4]=="12":
	mes = "de dezembro de"

ano = data[4:8]

print(dias,mes,ano)

	

