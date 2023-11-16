#from numpy import *

v = (input(":"))
dia = v[0:2]
ano = v[4:]


if(v[3] == "1"):
	m ="janeiro"
if(v[3] == "2"):
	m ="fevereiro"
if(v[3] == "3"):
	m ="marco"
if(v[3] == "4"):
	m ="abril"
if(v[3] == "5"):
	m ="maio"
if(v[3] == "6"):
	m ="junho"
if(v[3] == "7"):
	m="julho"
if(v[3] == "8"):
	m ="agosto"
if(v[3] == "9"):
	m ="setembro"
if(v[2:4] == "10"):
	m ="outubro"
if(v[2:4] == "11"):
	m ="novembro"
if(v[2:4] == "12"):
	m ="dezembro"




print(dia, "de", m ,"de",ano)