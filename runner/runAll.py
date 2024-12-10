import subprocess
from concurrent.futures import ThreadPoolExecutor

comandos_txt = "/home/fernando/Área de Trabalho/Projeto/comandos.txt"
exercicios_txt = "/home/fernando/Área de Trabalho/Projeto/idName2.txt"

#comandos existentes
with open(comandos_txt, "r") as f:
    comandos_base = f.readlines()
# IDs dos exercícios
with open(exercicios_txt, "r") as f:
    ids_exercicios = [linha.strip() for linha in f]

novos_comandos = []
for id_exercicio in ids_exercicios:
    for comando in comandos_base:
        if "1027" in comando:
            novos_comandos.append(comando.replace("1027", id_exercicio))

def execComando(comando):
    print(f"Executando: {comando.strip()}")
    processo = subprocess.run(comando.strip(), shell=True)
    if processo.returncode != 0:
        print(f"Erro ao executar: {comando.strip()}")

with ThreadPoolExecutor(max_workers=4) as executor:  # Ajuste o número de workers conforme necessário
    futures = [executor.submit(execComando, comando) for comando in novos_comandos]

    # Aguardar todos os comandos terminarem
    for future in futures:
        future.result()

print("Todos os comandos foram executados.")