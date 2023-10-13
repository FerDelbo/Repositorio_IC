x = input("digite a data: ")

dia  = x[0:2]

if x[2:4] == "01":
	mes = "de janeiro de"
elif x[2:4] == "02":
	mes = "de fevereiro de"
elif x[2:4] == "03":
	mes = "de marco de"
elif x[2:4] == "04":
	mes = "de abril de"
elif x[2:4] == "05":
	mes = "de maio de"
elif x[2:4] == "06":
	mes = "de junho de"
elif x[2:4] == "07":
	mes = "de julho de"
elif x[2:4] == "08":
	mes = "de agosto de"
elif x[2:4] == "09":
	mes = "de setembro de"
elif x[2:4] == "10":
	mes = "de outubro de"
elif x[2:4] == "11":
	mes = "de novembro de"
elif x[2:4] == "03":
	mes = "de dezembro de"
	
ano = x[4:]

print(dia,mes,ano)