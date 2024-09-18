dia = input("Digite a data no formato ddmmyyyy: ")
dia = int(dia)
mes = dia // 100 % 100
ano = dia // 10000
meses = ["janeiro", "fevereiro", "marco", "abril", "maio", "junho", "julho",
         "agosto", "setembro", "outubro", "novembro", "dezembro"]
print(f"{dia % 100} de {meses[mes - 1]} de {ano}")
