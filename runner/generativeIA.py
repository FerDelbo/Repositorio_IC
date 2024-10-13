#pip install langchain-openai
#pip install langchain-mistralai
#pip install google-generativeai langchain-google-genai
import sys
import glob
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_mistralai import ChatMistralAI 
from langchain_openai import ChatOpenAI
from utils import keys
from keys import GEMINI_KEY
from keys import GPT_KEY
from keys import MISTRAL_KEY

prompt = {} #dicionario vazio

class generativeIA:
    def __init__(self, llm, name, language, partition, session):
        self.llm = llm
        self.name = name
        self.language = language
        self.partition = partition
        self.session = session

    def __convertTxt(self, fileTxt):
        with open(fileTxt, 'r') as arquivo:
            linhas = arquivo.readlines() #transforma o txt em um lista
        for i in linhas: #laço que percorre a lista criada anteriormente
            if ":\n" in i: #comparação para separar chave de valor
                prompt.update({i:''}) #define a chave com um valor vazio por enquanto
            elif len(prompt) >= 1: #deve conter pelo menos 1 chave no dicionario  
                lastKey = list(prompt)[-1] #pega a ultima chave 
                prompt[str(lastKey)] += i #define o valor para a ultima chave que foi definida
        #print(prompt)

    def createPrompt(self,):
        #Aqui ocrre a filtragem dos diretorios e subdiretorios para a utilização do txt
        #Veiculos, Média, Data
        path = glob.glob(f"/home/**/Repositorio_IC/IC/**/{self.name}*/**/Prompts/**/*{self.language}.txt", recursive=True)
        self.__convertTxt(path[0])

    def saveCode(self, response):
        #salvar o arquivo
        directory = glob.glob(f"/home/**/Repositorio_IC/IC/**/{self.name}*/**/Codigos {self.llm}/{self.session}", recursive=True)
        print(directory)
        if len(directory) == 0:
            path = self.__createSession()
            print("seção criada")
            nome = f'{self.llm}{self.partition}{self.language}.py'
            full_path = os.path.join(path, nome)
        else:
            nome = f'{self.llm}{self.partition}{self.language}.py'
            full_path = os.path.join(directory[0], nome)
        
        file = open(full_path, 'w')
        file.write(str(response.content))
        file.close()
        self.__removeLines(full_path)

    def __createSession(self):
        #print("criando seção")
        directory = glob.glob(f"/home/**/Repositorio_IC/IC/**/{self.name}*/**/Codigos {self.llm}", recursive=True)
        base_path = directory[0]
        new_subdirectory_path = os.path.join(base_path, self.session)
        os.makedirs(new_subdirectory_path, exist_ok=True)
        return new_subdirectory_path
        
    def __removeLines(self, directory):
        #editar        
        with open(directory, 'r') as file:
            lines = file.readlines()
            newLines = []
            flag = False
            for i in lines:
                if "```" in i: #A formatação do codigo vem com esse icone ``` 
                    flag = True
                elif flag != False:
                    newLines.append(i)
        #reescrever
        with open(directory, 'w') as file:
            file.writelines(newLines)

    def createMessage(self):
        message = prompt['Descrição:\n']
        l = ['Formato para entrada e saída de dados:\n', 'Dicas:\n', 'Casos de teste:\n']
        if self.partition == "Descrição": 
            return message
        else:
            for i in l:
                if self.partition in i:
                    newTxt = prompt[i]
                    message = message + newTxt
                    return message
                else:
                    newTxt = prompt[i]
                    message = message + newTxt

def generativeCodeRun(nameLLM, nameExercice, language, partPrompt, session):
    start = generativeIA(nameLLM, nameExercice, language, partPrompt, session)
    start.createPrompt()
    message = start.createMessage()

    if nameLLM == "Gemini":
        modelLLM = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GEMINI_KEY)
    elif nameLLM == "ChatGPT":
        modelLLM = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=GPT_KEY)
    elif nameLLM == "HuggingChat":
        modelLLM = ChatMistralAI(model="open-codestral-mamba", mistral_api_key=MISTRAL_KEY)
        #modelLLM = ChatMistralAI(model="codestral-latest", mistral_api_key=MISTRAL_KEY)
        
    response = modelLLM.invoke(message)
    print(response.content)
    start.saveCode(response)

if __name__ == "__main__":
    
    nameLLM = sys.argv[1] #nome da LLM
    nameExercice = sys.argv[2] #nome do exercicio
    language =  sys.argv[3] #idioma
    partPrompt = sys.argv[4] #parte do prompt
    session = sys.argv[5] #qual sesção de teste esta ocorendo

    generativeCodeRun(nameLLM, nameExercice, language, partPrompt, session)