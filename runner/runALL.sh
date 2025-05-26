#!/bin/bash

# Caminho do arquivo
ARQUIVO="/home/fernando/Área de trabalho/Projeto/novos_exe"

# Leitura linha a linha
while IFS= read -r i; do
  # Verifica se é número e se é par
  if [[ "$i" =~ ^[0-9]+$ ]] && (( i % 2 == 0 )); then
    echo "Executando para i = $i"
    python3 codeEvaluator.py "enunciadosCodeBench.xlsx" \
      "/home/fernando/Área de trabalho/Projeto/solucaos" \
      "$i" GPT4o pt -n Enunciado \
      "/home/fernando/Área de trabalho/Projeto/Repositorio_IC/IC/problemas codebanch/newexercisesTestCas.txt" \
      1 1
  fi
done < "$ARQUIVO"
