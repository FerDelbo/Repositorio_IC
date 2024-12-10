import argparse
import codeGenerator
import extraction #Responsavel por extrair os componentes do aqruivo XML e salvar em uma planilha
import testExecute
import glob
import os
#o intuito é colocar o caminho do repositorio inicial o que já contem e um de saida para ele salvar as infos

class CodeEvaluator:
    def __init__(self, input_dirctory, output_dirctory, nameExercise, nameLLM, language, prompt, testcase):
        self.base_input_dirctory = input_dirctory #onde vai ser salvo
        self.base_output_dirctory = output_dirctory #repositorio ic
        self.nameProblems = nameExercise
        self.nameLLM = nameLLM
        self.language = language
        self.prompt_type = prompt
        self.fileTC = testcase
        # self.k = qtd #quantas vezes ele vai gerar

    def _pathOutput(self):
        path = self.base_output_dirctory + f"/{self.nameProblems}/{self.nameLLM}"
        if os.path.exists(path):
            return path
        else:
            os.makedirs(path, exist_ok=True)
            return path

    def run(self,):
        from datetime import datetime
        
        now = datetime.now()
        session = str(now.day) + "do" + str(now.month)
        #passo 1 buscar o problema
        #passo 2 trasformar em um dicionario
        #passo 3 selecionar a parte desejavel
        #passo 4 selciona a llm
        #passo 5 manda para a llm
        #passo 6 pega a resposta e salva em um diretorio fora do repositorio
        path = self._pathOutput()
        executeCode = codeGenerator.codeRun(self.base_input_dirctory, path, self.nameLLM, self.nameProblems, self.language, self.prompt_type, session)
        #passo 7 com o código salvo é realizdo os casos de teste
        #passo 8 pega o resultado e traforma em XML
        executeTestCase = testExecute.TestExecute(self.nameProblems, self.nameLLM, self.prompt_type, self.language, session, path, self.base_input_dirctory, self.fileTC)
        executeTestCase.runTestCase()
        #passo 9 é feita uma limpa no XML e pega o conteudo para jogar em uma planikha fora desse repositorio
        extraction.run(self.nameProblems, self.nameLLM, self.language, self.prompt_type, path)
        #programa finalizado

parser = argparse.ArgumentParser(description="Inciar gerador de soluções.")
# Adicionando os argumentos
parser.add_argument('input', type=str, help='diretorio de entrada')
parser.add_argument('output', type=str, help='diretorio de saida')
parser.add_argument('nameProblems', type=str, help='Nome do exercício')
parser.add_argument('nameLLM', type=str, help='Nome da LLM')
parser.add_argument('language', type=str, help='Idioma')
#parser.add_argument('partPrompt', type=str, help='Parte do prompt selecionada')
parser.add_argument('-n', '--listPrompt', action="append")
parser.add_argument('testCase', type=str, help="casos de teste")

#Analisando os argumentos
args = parser.parse_args()

start = CodeEvaluator(args.input, args.output, args.nameProblems, args.nameLLM, args.language, args.listPrompt, args.testCase)
start.run()