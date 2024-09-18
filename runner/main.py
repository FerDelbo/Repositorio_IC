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

import testV # Responsavel pelos casos de teste do exercico de Veículos trafegando em alta velocidade
import testM # Responsavel pelos casos de teste do exercico de Média ponderada
import testD # Responsavel pelos casos de teste do exercico de Data por extenso
import extraction #Responsavel por extrair os componentes do aqruivo XML e salvar em uma planilha

#import importlib
#importlib.reload(testV)

nameExercise = sys.argv[1] # Nome do exercicio
arg2 = sys.argv[2] # Nome da LLM
arg3 = sys.argv[3] # Parte do prompt é selecionada
arg4 = sys.argv[4] # Idioma
stop = True

if nameExercise == "Veiculos":
    testV.runTest(arg2, arg3, arg4)
    
elif nameExercise == "Média":
    testM.runTest(arg2, arg3, arg4)
    
elif nameExercise == "Data":
    testD.runTest(arg2, arg3, arg4)

else:
    print("Arquivo não encontrado! Veja a formatação adequado dos dados")
    stop = False

if stop:
    xml = extraction.buscarXML(nameExercise)
    extractor = XMLExtractor(xml[0], nameExercise, arg2)
    extractor.run()