#!/bin/bash

# Caminho para o diretório atual
diretorio_atual=$(dirname "$0")

# Obter uma lista de arquivos .py no diretório atual
arquivos_python=$(find "$diretorio_atual" -maxdepth 1 -name "*.py")

# Loop para executar o código Python em cada arquivo
for arquivo_python in $arquivos_python; do
    echo "Executando $arquivo_python"

    # Verificar se o arquivo existe
    if [ -f "$arquivo_python" ]; then
        # Executar o arquivo Python com redirecionamento de entrada e capturar a saída
        saida=$(python3 "$arquivo_python" < input.txt)

        # Verificar se a saída é igual à string desejada
        string_desejada="1\n3\n2"

        saida_sem_espacos=$(echo "$saida" | tr -d '[:space:]')
        string_desejada_sem_espacos=$(echo "$string_desejada" | tr -d '[:space:]')

        if [ "$saida_sem_espacos" = "$string_desejada_sem_espacos" ]; then
            echo "A saída está correta!"
            #echo "Saída do programa: $saida"
        else
            echo "A saída é diferente da esperada."
            #echo "Saída do programa: $saida"
        fi

        # Executar o arquivo Python com redirecionamento de entrada e capturar a saída
        saida=$(python3 "$arquivo_python" < input2.txt)

        # Verificar se a saída é igual à string desejada
        string_desejada="2\n1"

        saida_sem_espacos=$(echo "$saida" | tr -d '[:space:]')
        string_desejada_sem_espacos=$(echo "$string_desejada" | tr -d '[:space:]')

        if [ "$saida_sem_espacos" = "$string_desejada_sem_espacos" ]; then
            echo "A saída está correta!"
            #echo "Saída do programa: $saida"
        else
            echo "A saída é diferente da esperada."
            #echo "Saída do programa: $saida"
        fi

        # Executar o arquivo Python com redirecionamento de entrada e capturar a saída
        saida=$(python3 "$arquivo_python" < input3.txt)

        # Verificar se a saída é igual à string desejada
        string_desejada="3\n1"

        saida_sem_espacos=$(echo "$saida" | tr -d '[:space:]')
        string_desejada_sem_espacos=$(echo "$string_desejada" | tr -d '[:space:]')

        if [ "$saida_sem_espacos" = "$string_desejada_sem_espacos" ]; then
            echo "A saída está correta!"
            #echo "Saída do programa: $saida"
        else
            echo "A saída é diferente da esperada."
            #echo "Saída do programa: $saida"
        fi
    else
        echo "O arquivo $arquivo_python não existe."
    fi
done

