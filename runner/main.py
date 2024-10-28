import sys
#import generativeIA
#from utils import generativeIA # Responsavel por fazer a requisição a API das LLM, gerar o código e salvar no repositorio
# from utils import testV # Responsavel pelos casos de teste do exercico de Veículos trafegando em alta velocidade
# from utils import testM # Responsavel pelos casos de teste do exercico de Média ponderada
# from utils import testD # Responsavel pelos casos de teste do exercico de Data por extenso
from utils import extraction #Responsavel por extrair os componentes do aqruivo XML e salvar em uma planilha
import codeGenrator
import argparse
import testExecute
# Criação do parser
parser = argparse.ArgumentParser(description="Processa parâmetros do exercício.")

# Adicionando os argumentos
parser.add_argument('nameExercise', type=str, help='Nome do exercício')
parser.add_argument('nameLLM', type=str, help='Nome da LLM')
parser.add_argument('partPrompt', type=str, help='Parte do prompt selecionada')
parser.add_argument('language', type=str, help='Idioma')
parser.add_argument('session', type=str, help='Sessão realizada do teste')

# Analisando os argumentos
args = parser.parse_args()

# Acessando os parâmetros
nameExercise = args.nameExercise
nameLLM = args.nameLLM
partPrompt = args.partPrompt
language = args.language
session = args.session

codeGenrator.CodeRun(nameLLM, nameExercise, language, partPrompt, session)
testExecute.runTestCase(nameExercise)

extraction.run(nameExercise, nameLLM, language, partPrompt)

# nameExercise = sys.argv[1] # Nome do exercicio
# nameLLM = sys.argv[2] # Nome da LLM
# partPrompt = sys.argv[3] # Parte do prompt é selecionada
# language = sys.argv[4] # Idioma
# session = sys.argv[5] #sesão que foi realizada o teste

# generativeIA.generativeCodeRun(nameLLM, nameExercise, language, partPrompt, session)

# if nameExercise == "Veiculos":
#     testV.runTest(nameLLM, partPrompt, language, session)
#     extraction.run(nameExercise, nameLLM, language, partPrompt)
   
# elif nameExercise == "Média":
#     testM.runTest(nameLLM, partPrompt, language, session)
#     extraction.run(nameExercise, nameLLM, language, partPrompt)
    
# elif nameExercise == "Data":
#     testD.runTest(nameLLM, partPrompt, language, session)
#     extraction.run(nameExercise, nameLLM, language, partPrompt)

# else:
#     print("Arquivo não encontrado! Veja a formatação adequado dos dados")