#data
date=input("Digite a data:")

dia=date[:2]

if (date[2:4]=="01"):
	new=(dia+ " de janeiro de "+date[4:])
elif (date[2:4]=="02"):
	new=(dia+ " de fevereiro de "+date[4:])
elif (date[2:4]=="03"):
	new=(dia+ " de marco de "+date[4:])
elif (date[2:4]=="04"):
	new=(dia+ " de abril de "+date[4:])
elif (date[2:4]=="05"):
	new=(dia+ " de maio de "+date[4:])
elif (date[2:4]=="06"):
	new=(dia+ " de junho de "+date[4:])
elif (date[2:4]=="07"):
	new=(dia+ " de julho de "+date[4:])
elif (date[2:4]=="08"):
	new=(dia+ " de agosto de "+date[4:])
elif (date[2:4]=="09"):
	new=(dia+ " de setembro de "+date[4:])
elif (date[2:4]=="10"):
	new=(dia+ " de outubro de "+date[4:])
elif (date[2:4]=="11"):
	new=(dia+ " de novembro de "+date[4:])
elif (date[2:4]=="12"):
	new=(dia+ " de dezembro de "+date[4:])
print(new)