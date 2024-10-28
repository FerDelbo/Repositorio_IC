import argparse
import codeGenerator
from utils import extraction #Responsavel por extrair os componentes do aqruivo XML e salvar em uma planilha
import testExecute

class CodeEvaluator:
    def __init__(self, nameExercise, nameLLM, language, prompt):
        #self.base_output_dirctory = output_dirctory
        #self.base_input_dirctory = input_dirctory
        self.nameProblems = nameExercise
        self.nameLLM = nameLLM
        self.language = language
        self.prompt_type = prompt
        # self.k = qtd #quantas vezes ele vai gerar

    def run(self,):
        from datetime import datetime

        now = datetime.now()
        session = str(now.day) + "de" + str(now.month)
        #passo 1 buscar o problema
        #passo 2 trasformar em um dicionario
        #passo 3 selecionar a parte desejavel
        #passo 4 selciona a llm
        #passo 5 manda para a llm
        #passo 6 pega a resposta e salva em um diretorio fora do repositorio
        executeCode = codeGenerator.codeRun(self.nameLLM, self.nameProblems, self.language, self.prompt_type, session)
        #passo 7 com o código salvo é realizdo os casos de teste
        #passo 8 pega o resultado e traforma em XML
        #nameLLM, partPrompt, language, session
        executeTestCase = testExecute.TestExecute(self.nameLLM, self.prompt_type, self.language, session)
        executeTestCase.runTestCase(self.nameProblems)
        #passo 9 é feita uma limpa no XML e pega o conteudo para jogar em uma planikha fora desse repositorio
        extraction.run(self.nameProblems, self.nameLLM, self.language, self.prompt_type)
        #programa finalizado
    
    
    # def discolver_problems(self,):
    #     list problems = glob.glob(f'/**/Repositorio_IC/**/Prompts/*{self.language}.txt',recursive=true)
    #     return problems
    # #def createLLM(self,) -> None:
    #     pass

parser = argparse.ArgumentParser(description="Inciar gerador de soluções.")
# Adicionando os argumentos
parser.add_argument('nameProblems', type=str, help='Nome do exercício')
parser.add_argument('nameLLM', type=str, help='Nome da LLM')
parser.add_argument('language', type=str, help='Idioma')
parser.add_argument('partPrompt', type=str, help='Parte do prompt selecionada')
#parser.add_argument('session', type=str, help='Sessão realizada do teste')
#Analisando os argumentos
args = parser.parse_args()

start = CodeEvaluator(args.nameProblems, args.nameLLM, args.language, args.partPrompt)
start.run()