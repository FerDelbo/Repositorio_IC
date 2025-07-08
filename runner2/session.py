import os
from datetime import datetime
import uuid
from generatorCode import LLM
import pyexcel
import re

class Session:
    def __init__(self, outDirectory, inputDirectory):
        self.start_date = str(datetime.date(datetime.now()))
        self.session_id = self.start_date + str(uuid.uuid4())
        self.outDirectory = outDirectory
        self.inputDirectory = inputDirectory
    
    def createSession(self):
        base_path = self.outDirectory
        new_subdirectory_path = os.path.join(base_path, self.start_date)    
        os.makedirs(new_subdirectory_path, exist_ok=True)
        return new_subdirectory_path
        
    def setSession(self, day, month):
        self.session = str(day) + "do" + str(month)

    def getInputDirectory(self):
        return self.inputDirectory
    
    def getOutputDirectory(self):
        return self.outDirectory
    
# TODO: Realizar os SET de input e output directory


class SessionManager:
    def __init__(self, file):
        self.archive = file
    
    def create(self, base_directory, output_directory):
        self.session = Session(inputDirectory=base_directory, outDirectory=output_directory)
        self.outDirectory = Session.createSession(self.session)
        return self.outDirectory
        
    def __test_case_formatting(self, test_case):
        # Divide em blocos de test case
        blocks = re.split(r"-- TEST CASE \d+:", test_case)

        result = {}

        for block in blocks:
            # Extrai o input
            match_input = re.search(r"---- input:\s*(\[.*?\])", block, re.DOTALL)
            # Extrai o correct output (até a próxima seção ou fim)
            match_output = re.search(r"---- correct output:\s*(.*?)(?:----|\Z)", block, re.DOTALL)

            if match_input and match_output:
                input = match_input.group(1).strip()
                output = match_output.group(1).strip()
                result[input] = output

        return result

    def listExercise(self, problem_id, language):
        records = pyexcel.get_records(file_name=self.archive)

        for row in records:
            if row['Problema ID'] == problem_id:
                self.exercise = Exercise(
                    id=row['Problema ID'],
                    name=row['Nome do exercício'],
                    language=language,
                    content=row['Enunciado revisado'],
                    # test_case=row['Casos de teste'],
                    test_case=self.__test_case_formatting(row['Casos de teste']),
                    solution=row['Solução de referência']
                )
                return self.exercise
        else:
            return None
    
    def settingLLM(self, name_llm, temperature):
        self.llm = LLM(name_llm, self.exercise, temperature)
        return self.llm

    def saveContent(self):
        base_path = self.outDirectory
        new_path = f'{self.exercise.getId()}/{self.llm.getName()}/{self.exercise.getName()}_{self.session}.py'
        full_path = os.path.join(base_path, new_path)
        create_path = os.path.dirname(full_path)
        os.makedirs(create_path, exist_ok=True)
        open(full_path, 'w').write(self.llm.getContent())
        self.path_code = full_path

class Exercise:
    def __init__(self, id, name, language, content, test_case, solution):
        self.id = id
        self.name = name
        self.language = language
        self.content = content
        self.test_case = test_case
        self.solution = solution

    def getName(self):
        return self.name

    def getLanguage(self):
        return self.language
    
    def getId(self):
        return self.id
    
    def getContent(self):
        return self.content

    def getTestCase(self):
        return self.test_case
    
    def getSolution(self):
        return self.solution