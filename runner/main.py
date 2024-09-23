import sys
import os

# Adiciona o diretório do arquivo testV.py ao sys.path
path_to_test_Veiculo = os.path.abspath('/home/fernando/Área de Trabalho/Projeto/Repositorio_IC/IC/Comando de repetições/Veículos trafegando em alta velocidade/Testes/')
sys.path.append(path_to_test_Veiculo)
# Adiciona o diretório do arquivo testM.py ao sys.path
path_to_test_Media = os.path.abspath('/home/fernando/Área de Trabalho/Projeto/Repositorio_IC/IC/Variáveis e estrutura sequencial/Média ponderada/Testes')
sys.path.append(path_to_test_Media)
# Adiciona o diretório do arquivo testD.py ao sys.path
path_to_test_Data = os.path.abspath('/home/fernando/Área de Trabalho/Projeto/Repositorio_IC/IC/Vetores e strings/Data por extenso/Testes')
sys.path.append(path_to_test_Data)

#from .IC.Comando.Veículos.Testes import testV
import testV # Responsavel pelos casos de teste do exercico de Veículos trafegando em alta velocidade
import testM # Responsavel pelos casos de teste do exercico de Média ponderada
import testD # Responsavel pelos casos de teste do exercico de Data por extenso
import extraction #Responsavel por extrair os componentes do aqruivo XML e salvar em uma planilha

#import importlib
#importlib.reload(testV)

nameExercise = sys.argv[1] # Nome do exercicio
nameLLM = sys.argv[2] # Nome da LLM
partPrompt = sys.argv[3] # Parte do prompt é selecionada
language = sys.argv[4] # Idioma

if nameExercise == "Veiculos":
    testV.runTest(nameLLM, partPrompt, language)
    extraction.run(nameExercise, nameLLM)
   
elif nameExercise == "Média":
    testM.runTest(nameLLM, partPrompt, language)
    extraction.run(nameExercise, nameLLM)
    
elif nameExercise == "Data":
    testD.runTest(nameLLM, partPrompt, language)
    extraction.run(nameExercise, nameLLM)

else:
    print("Arquivo não encontrado! Veja a formatação adequado dos dados")