import glob
import os
import generatorCode
import re # Expressão regulares para remover o conteudo indesejavel 

class Save:
    def __init__(self, content, session):
        self.content = content #Aqui eu guardo a classe LLM
        self.session = session

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

    def saveCode(self, outDirctory):
        #salvar o arquivo
        directory = glob.glob(f"{outDirctory}/{self.nameExercise}/{self.llm}/{self.session}", recursive=True)
        if len(directory) == 0: # Esxite uma sessão já criada ?
            path = self.session.createSession()
            nome = f'{self.llm}{self.partPrompt[0]}{self.language}.py'
            full_path = os.path.join(path, nome)
        else:
            nome = f'{self.llm}{self.partPrompt[0]}{self.language}.py'
            full_path = os.path.join(directory[0], nome)
        
        solution = self.content.getContent()
        solution = self.__removeLines(solution)
        with open(full_path, 'w') as file:
            file.write(solution)