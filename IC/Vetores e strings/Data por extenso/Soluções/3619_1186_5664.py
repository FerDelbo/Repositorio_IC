d= input('data: ')

if d[2:4]=='01':
	m='janeiro'
	
if d[2:4]=='02':
	m='fevereiro'
	
if d[2:4]=='03':
	m='marco'
	
if d[2:4]=='04':
	m='abril'
	
if d[2:4]=='05':
	m='maio'
	
if d[2:4]=='06':
	m='junho'
	
if d[2:4]=='07':
	m='julho'
	
if d[2:4]=='08':
	m='agosto'
	
if d[2:4]=='09':
	m='setembro'
	
if d[2:4]=='10':
	m='outubro'
	
if d[2:4]=='11':
	m='novembro'
	
if d[2:4]=='12':
	m='dezembro'
	

print(d[0:2]+' de '+m+' de '+d[4:8])