import sys
import generativeIA
#from utils import generativeIA # Responsavel por fazer a requisição a API das LLM, gerar o código e salvar no repositorio
from utils import testV # Responsavel pelos casos de teste do exercico de Veículos trafegando em alta velocidade
from utils import testM # Responsavel pelos casos de teste do exercico de Média ponderada
from utils import testD # Responsavel pelos casos de teste do exercico de Data por extenso
from utils import extraction #Responsavel por extrair os componentes do aqruivo XML e salvar em uma planilha

nameExercise = sys.argv[1] # Nome do exercicio
nameLLM = sys.argv[2] # Nome da LLM
partPrompt = sys.argv[3] # Parte do prompt é selecionada
language = sys.argv[4] # Idioma
session = sys.argv[5] #sesão que foi realizada o teste

generativeIA.generativeCodeRun(nameLLM, nameExercise, language, partPrompt, session)

if nameExercise == "Veiculos":
    testV.runTest(nameLLM, partPrompt, language, session)
    extraction.run(nameExercise, nameLLM)
   
elif nameExercise == "Média":
    testM.runTest(nameLLM, partPrompt, language, session)
    extraction.run(nameExercise, nameLLM)
    
elif nameExercise == "Data":
    testD.runTest(nameLLM, partPrompt, language, session)
    extraction.run(nameExercise, nameLLM)

else:
    print("Arquivo não encontrado! Veja a formatação adequado dos dados")