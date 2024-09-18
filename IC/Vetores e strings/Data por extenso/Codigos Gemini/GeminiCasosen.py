meses = ["Janeiro", "Fevereiro", "Marco", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

dia, mes, ano = input("Digite a data no formato ddmmyyyy: ")

print(f"{meses[int(mes) - 1]} {dia}, {ano}")
