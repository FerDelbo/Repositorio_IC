# filename: date_extenso.py
dias = ["primeiro", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte", "vinte e um", "vinte e dois", "vinte e três", "vinte e quatro", "vinte e cinco", "vinte e seis", "vinte e sete", "vinte e oito", "vinte e nove", "trinta", "trinta e um"]
meses = ["janeiro", "fevereiro", "marco", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

data = input("Informe a data no formato ddmmaaaa: ")
dia = int(data[:2])
mes = int(data[2:4])
ano = int(data[4:])

print(f"{dia} de {meses[mes-1]} de {ano}")
