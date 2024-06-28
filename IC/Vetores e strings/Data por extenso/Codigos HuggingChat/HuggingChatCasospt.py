
```python
from datetime import datetime
import calendar

# Ler a entrada do usuário
data = input("Digite a data no formato 'ddmmaaaa': ")

# Converter a entrada para um objeto datetime
data_obj = datetime.strptime(data, "%d%m%Y")

# Obter o nome do mês por extenso
nome_mes = calendar.month_name[data_obj.month]

# Formatar a data por extenso
data_por_extenso = data_obj.strftime("%d") + " de " + nome_mes + " de " + data_obj.strftime("%Y")

# Imprimir a data por extenso
print(data_por_extenso)
```

Esse código lê a entrada do usuário, converte a entrada para um objeto datetime, obtém o nome do mês por extenso, formata a data por extenso e imprime a data formatada.

Observe que este código assume que a entrada será sempre válida. Se você precisar verificar se a data de entrada é válida, você precisará adicionar alguma lógica de validação.

Por exemplo, para verificar se o mês tem entre 28 e 31 dias, você pode usar o seguinte código:

```python
from datetime import datetime
import calendar

# Ler a entrada do usuário
data = input("Digite a data no formato 'ddmmaaaa': ")

# Converter a entrada para um objeto datetime
try:
    data_obj = datetime.strptime(data, "%d%m%Y")
except ValueError:
    print("Data inválida")
    exit()

# Obter o nome do mês por extenso
nome_mes = calendar.month_name[data_obj.month]

# Verificar se o mês tem entre 28 e 31 dias
if data_obj.day > calendar.monthrange(data_obj.year, data_obj.month)[1]:
    print("Data inválida")
    exit()

# Formatar a data por extenso
data_por_extenso = data_obj.strftime("%d") + " de " + nome_mes + " de " + data_obj.strftime("%Y")

# Imprimir a data por extenso
print(data_por_extenso)
```

Esse código verifica se a data é válida antes de formatá-la e imprimi-la. Se a data não for válida, o código imprimirá "Data inválida" e encerrará a execução do programa.
