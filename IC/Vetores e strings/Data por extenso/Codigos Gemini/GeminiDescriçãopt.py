# filename: ex_date_extenso.py
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

dia = input('Dia [dd]: ')
mes = input('Mes [mm]: ')
ano = input('Ano [aaaa]: ')

data = '{}-{}-{}'.format(dia, mes, ano)

data_extenso = f'{dia} de {locale.month_name[int(mes)]} de {ano}'

print(data_extenso)
