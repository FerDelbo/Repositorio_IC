#pip install langchain-openai
#pip install langchain-mistralai
#pip install google-generativeai langchain-google-genai
import sys
import glob
import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_mistralai import ChatMistralAI 
from langchain_openai import ChatOpenAI
#from langchain.text_splitter import RegexTextSplitter
import re

from utils import keys
from keys import GEMINI_KEY
from keys import GPT_KEY
from keys import MISTRAL_KEY

class codeGenerator:
    def __init__(self, llm, name, language, partition, session):
        self.llm = llm
        self.nameExercise = name
        self.language = language
        self.partPrompt = partition
        self.session = session
        self.temperature = 1
        self.prompt = {} #dicionario vazio
        
    def __convertTxt(self, fileTxt):
        #aquei ocorre a conversão de um txt em um dicionario
        with open(fileTxt, 'r') as arquivo:
            linhas = arquivo.readlines() #transforma o txt em um lista
        previousLine = "" 
        for index,  i in enumerate(linhas): #laço que percorre a lista criada anteriormente
            if "Test case" in i or "Casos de teste" in i:
                value = linhas[index:]
                self.prompt.update({i:''})
                for j in value:
                    self.prompt[i] += j 
                break
            elif ":\n" in i and previousLine == "\n": #comparação para separar chave de valor
                self.prompt.update({i:''}) #define a chave com um valor vazio por enquanto
            elif len(self.prompt) >= 1: #deve conter pelo menos 1 chave no dicionario  
                lastKey = list(self.prompt)[-1] #pega a ultima chave 
                self.prompt[str(lastKey)] += i #define o valor para a ultima chave que foi definida
            previousLine = i
        #print(self.prompt)

    def __createPrompt(self, dirctory):
        #Aqui ocrre a filtragem dos diretorios e subdiretorios para a utilização do txt
        #Veiculos, Média, Data
        path = glob.glob(f"{dirctory}*/**/{self.nameExercise}*/**/Prompts/**/*.{self.language}.txt", recursive=True)
        #print(path)
        self.__convertTxt(path[0])

    def saveCode(self, response, outDirctory):
        #salvar o arquivo
        directory = glob.glob(f"{outDirctory}/{self.nameExercise}/{self.llm}/{self.session}", recursive=True)
        if len(directory) == 0:
            path = self.__createSession(outDirctory)
            print("seção criada")
            nome = f'{self.llm}{self.partPrompt[0]}{self.language}.py'
            full_path = os.path.join(path, nome)
        else:
            nome = f'{self.llm}{self.partPrompt[0]}{self.language}.py'
            full_path = os.path.join(directory[0], nome)
        
        solution = self.__removeLines(response.content)
        file = open(full_path, 'w')
        file.write(solution)
        file.close()

    def __createSession(self, outDirctory):
        #print("criando seção")
        #directory = glob.glob(f"{outDirctory}/{self.nameExercise}/{self.llm}", recursive=True)
        base_path = outDirctory
        new_subdirectory_path = os.path.join(base_path, self.session)
        os.makedirs(new_subdirectory_path, exist_ok=True)
        return new_subdirectory_path

    
    def __removeLines(self, solution):
        # Definir a expressão regular para extrair o conteúdo entre blocos de código delimitados por ```
        pattern = r"```(?:\w*\n)?(.*?)```"
        # Usar re.search para encontrar o primeiro bloco de código
        match = re.search(pattern, solution, re.DOTALL)
        # Extrair e limpar o bloco de código se encontrado
        first_code_block = match.group(1).strip() if match else None
        if first_code_block is None :
            return solution
        return first_code_block

    def createMessage(self, inputDir, output):
        self.__createPrompt(inputDir)
        if self.language == "en":
            message = self.prompt['Description:\n']
            l = ['Format for data input and output:\n', 'Tips:\n', 'Test cases:\n']
            fragments = self.partPrompt[1]
        elif "en2" in self.language:
            message = self.prompt['Description:\n']
            l = ['Format for data input and output:\n', 'Hints:\n', 'Test cases:\n']
            if len(self.partPrompt) == 3:
                fragments = self.partPrompt[2]
            else:
                fragments = self.partPrompt[1]
        else:
            message = self.prompt['Descrição:\n']
            l = ['Formato para entrada e saída de dados:\n', 'Dicas:\n', 'Casos de teste:\n']
            fragments = self.partPrompt[0]

        if fragments == "Descrição" or fragments == "Description": 
            return message
        if fragments in "Casos de teste" or fragments in "Test cases":
            message = " ".join(self.prompt.values())
            return message 
        else:
            for i in l:
                if fragments in i:
                    newTxt = self.prompt[i]
                    message = message + newTxt
                    return message
                else:
                    newTxt = self.prompt[i]
                    message = message + newTxt
        
def codeRun(inputDirctory, outDirctory, nameLLM, nameExercice, language, partPrompt, session):
    start = codeGenerator(nameLLM, nameExercice, language, partPrompt, session)
    message = start.createMessage(inputDirctory, outDirctory)

    if nameLLM == "Gemini":
        modelLLM = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GEMINI_KEY)
    elif nameLLM == "ChatGPT":
        modelLLM = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=GPT_KEY)
    elif nameLLM == "HuggingChat":
        modelLLM = ChatMistralAI(model="open-codestral-mamba", mistral_api_key=MISTRAL_KEY)
        #modelLLM = ChatMistralAI(model="codestral-latest", mistral_api_key=MISTRAL_KEY)
    elif nameLLM == "ChatGPT4o":
        modelLLM = ChatOpenAI(model="gpt-4o", openai_api_key=GPT_KEY)

    #print(message)    
    response = modelLLM.invoke(message)
    print(response.content)
    start.saveCode(response, outDirctory)

if __name__ == "__main__":
    
    nameLLM = sys.argv[1] #nome da LLM
    nameExercice = sys.argv[2] #nome do exercicio
    language =  sys.argv[3] #idioma
    partPrompt = sys.argv[4] #parte do prompt
    #session = sys.argv[5] #qual sesção de teste esta ocorendo

    CodeRun(nameLLM, nameExercice, language, partPrompt, session)