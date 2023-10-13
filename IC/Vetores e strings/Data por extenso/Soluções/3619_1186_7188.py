da= (input())
dia= da[0:2]
ano= da[4:]
if da[2:4]== "01":
	m= "de janeiro de"
elif da[2:4]== "02":
	m= "de fevereiro de"
elif da[2:4]== "03":
	m= "de marco de"
elif da[2:4]== "04":
	m= "de abril de"
elif da[2:4]== "05":
	m= "de maio de"
elif da[2:4]== "06":
	m= "de junho de"
elif da[2:4]== "07":
	m= "de julho de"
elif da[2:4]== "08":
	m= "de agosto de"
elif da[2:4]== "09":
	m= "de setembro de"
elif da[2:4]== "10":
	m= "de outubro de"
elif da[2:4]== "11":
	m= "de novembro de"
elif da[2:4]== "12":
	m= "de dezembro de"

print(dia,m,ano)