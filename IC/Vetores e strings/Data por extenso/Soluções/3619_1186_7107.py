d = int(input())

d = str(d)

if(d[2] == "0"):
	if(d[3] == "1"):
		mm = "de janeiro de"
		
	elif(d[3] == "2"):
		mm = "de fevereiro de"
		
	elif(d[3] == "3"):
		mm = "de marco de"
		
	elif(d[3] == "4"):
		mm = "de abril de"
		
	elif(d[3] == "5"):
		mm = "de maio de"
		
	elif(d[3] == "6"):
		mm = "de junho de"
		
	elif(d[3] == "7"):
		mm = "de julho de"
		
	elif(d[3] == "8"):
		mm = "de agosto de"
		
	elif(d[3] == "9"):
		mm = "de setembro de"
		
else:
	if(d[3] == "0"):
		mm = "de outubro de"
		
	elif(d[3] == "1"):
		mm = "de novembro de"
		
	elif(d[3] == "2"):
		mm = "de dezembro de"

print(d[:2], mm, d[4:])