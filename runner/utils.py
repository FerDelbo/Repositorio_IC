import sys
import os

# Adiciona o diretório do arquivo testV.py ao sys.path
path_to_test_Veiculo = os.path.abspath('/home/fernando/Área de Trabalho/Projeto/Repositorio_IC/IC/Comando de repetições/Veiculos trafegando em alta velocidade/Testes/')
sys.path.append(path_to_test_Veiculo)
# Adiciona o diretório do arquivo testM.py ao sys.path
path_to_test_Media = os.path.abspath('/home/fernando/Área de Trabalho/Projeto/Repositorio_IC/IC/Variáveis e estrutura sequencial/Média ponderada/Testes')
sys.path.append(path_to_test_Media)
# Adiciona o diretório do arquivo testD.py ao sys.path
path_to_test_Data = os.path.abspath('/home/fernando/Área de Trabalho/Projeto/Repositorio_IC/IC/Vetores e strings/Data por extenso/Testes')
sys.path.append(path_to_test_Data)

#path_to_generativeIA = os.path.abspath('/home/fernando/Área de Trabalho/Projeto/apis')
#sys.path.append(path_to_generativeIA)

path_to_keys = os.path.abspath('/home/fernando/Área de Trabalho/Projeto/apis')
sys.path.append(path_to_keys)

#class testExecute 
#class generativeAI
#class codeGenerator
#class extraction
#-> chama todas as classes #class codeEvaluator


#import generativeIA
import testV # Responsavel pelos casos de teste do exercico de Veículos trafegando em alta velocidade
import testM # Responsavel pelos casos de teste do exercico de Média ponderada
import testD # Responsavel pelos casos de teste do exercico de Data por extenso
import extraction #Responsavel por extrair os componentes do aqruivo XML e salvar em uma planilha
import keys
#/home/fernando/Área de Trabalho/Projeto/Repositorio_IC/IC/Comando de repetições/Veículos trafegando em alta velocidade/Testes/testV.py
#/home/fernando/Área de Trabalho/Projeto/Repositorio_IC/IC/Comando de repetições/Veiculos trafegando em alta velocidade/Testes/testV.py