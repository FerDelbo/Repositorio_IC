
dt=input("digite a data:")
d= dt[0:2]
m= dt[2:4]
ano= dt[4: ]

if (m=="01"):
	m= d +" de "+ "janeiro" +" de "+ ano
elif (m=="02"):
	m= d +" de "+ "fevereiro" +" de "+ ano
elif (m=="03"):
	m= d +" de "+ "marco" +" de "+ ano
elif (m=="04"):
	m= d +" de "+ "abril" +" de "+ ano
elif (m=="05"):
	m= d +" de "+ "maio" +" de "+ ano
elif (m=="06"):
	m= d +" de "+ "junho" +" de "+ ano
elif (m=="07"):
	m= d +" de "+ "julho" +" de "+ ano
elif (m=="08"):
	m= d +" de "+ "agosto" +" de "+ ano
elif (m=="09"):
	m= d +" de "+ "setembro" +" de "+ ano
elif (m=="10"):
	m= d +" de "+ "outubro" +" de "+ ano
elif (m=="11"):
	m= d +" de "+ "novembro" +" de "+ ano
elif (m=="12"):
	m= d +" de "+ "dezembro" +" de "+ ano
print (m)

