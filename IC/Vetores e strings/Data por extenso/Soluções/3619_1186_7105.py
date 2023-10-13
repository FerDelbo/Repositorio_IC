n = input()
i = 0
mes = ""

if(n[2] == "0" and n[3] == "1"):
	mes = "janeiro"
elif(n[2] == "0" and n[3] == "2"):
	mes = "fevereiro"
elif(n[2] == "0" and n[3] == "3"):
	mes = "marco"
elif(n[2] == '0' and n[3] == '4'):
	mes = "abril"
elif(n[2] == '0' and n[3] == '5'):
	mes = "maio"
elif(n[2] == '0' and n[3] == '6'):
	mes = "junho"
elif(n[2] == '0' and n[3] == '7'):
	mes = "julho"
elif(n[2] == '0' and n[3] == '8'):
	mes = "agosto"
elif(n[2] == '0' and n[3] == '9'):
	mes = "setembro"
elif(n[2] == '1' and n[3] == '0'):
	mes = "outubro"
elif(n[2] == '1' and n[3] == '1'):
	mes = "novembro"
elif(n[2] == '1' and n[3] == '2'):
	mes = "dezembro"
	
print(n[0:2], "de", mes, "de", n[4:8])