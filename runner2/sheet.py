import xml.etree.ElementTree as ET
import openpyxl
import glob
import sys
from datetime import datetime
import git


class Sheet:
    def __init__(self, exercise, llm, path, dict_test_results):
        self.exercise = exercise #Pegar qual o nome e linguem usada
        self.llm = llm# Nome da LLM e temperatura
        self.path = path# Caminho da planilha salva
        self.total_test = dict_test_results['total']
        self.passed_test = dict_test_results['passed']
        self.failed_test = dict_test_results['failed']
        self.passed_test_names = dict_test_results['passed_names']
        self.failed_test_names = dict_test_results['failed_names']
        self.expected_and_obtained = dict_test_results['esperado_e_obtido']

    def extractData(self):
        # Transformar o arquivo XML em uma árvore
        tree = ET.parse(self.fileXML)
        root = tree.getroot()

        # Obter atributos do testsuite
        listTestsuite = root.attrib
        
        listTestsuite['timestamp'] = datetime.now()
        # Dicionário de componentes a serem extraídos
        components = {
            "NomeExercicio": self.exercise.getName(),
            "NomeLLM": self.lmm.getName(),
            "Temperatura": self.temperature,
            "Data/Hora": listTestsuite['timestamp'],
            "QtdFalhas": str(int(listTestsuite['failures']) + int(listTestsuite['errors'])),
            "QtdAcerto": str(int(listTestsuite['tests']) - int(listTestsuite['failures']) - int(listTestsuite['errors'])),
            "NomeFalha": '',
            "NomeAcerto": '',
            "Idioma": self.exercise.getLanguage(),
            # "Prompt": self.partPrompt[0],
            "Git": '',
            "NomeCasoTeste" : [],
            "ResultadoCasoTeste" : [],
        }
        

        repo = git.Repo(search_parent_directories=True)
        sha = repo.head.object.hexsha
        components['Git'] = sha 

        falhas = []
        acertos = []

         # Coletar nomes de testes que falharam ou passaram
        i = 0
        for testcase in root.iter('testcase'):
            print("=====", testcase.attrib['name'], i)
            i += 1
            nome_teste = testcase.attrib['name']
            components['NomeCasoTeste'].append(nome_teste)
            components['ResultadoCasoTeste'].append(not(testcase.find('failure') is not None or testcase.find('error') is not None))
            if testcase.find('failure') is not None or testcase.find('error') is not None:
                falhas.append(nome_teste)
            else:
                acertos.append(nome_teste)


        components['NomeFalha'] = "; ".join(falhas)
        components['NomeAcerto'] = "; ".join(acertos)
        self.components = components


    def saveExcel(self):
        # Abrir a planilha
        excel_file = self.path
        # excel_file = '/home/fernando/Área de trabalho/Projeto/solucoesLLM.xlsx'
        workbook = openpyxl.load_workbook(excel_file)
        sheet = workbook.active

        # Adicionar os dados à planilha
        for i in self.inputOutputLLM.keys():
            resultado_caso_teste = [
                self.components["NomeExercicio"],
                self.components["Idioma"],
                self.components["NomeLLM"],
                self.components["Temperatura"],
                self.components["Prompt"],
                self.components["Data/Hora"],
                self.components["QtdFalhas"],
                self.components["QtdAcerto"],
                self.components["NomeFalha"],
                self.components["NomeAcerto"],
                self.components["Git"],
                str(self.components['NomeCasoTeste'][i-1]),
                str(self.components['ResultadoCasoTeste'][i-1]),
                str(self.inputOutputLLM[i]['esperado']),
                str(self.inputOutputLLM[i]['obtido']),
                # self.inputOutputLLM[1]['obtido'],
                # self.inputOutputLLM[2]['esperado'],
                # self.inputOutputLLM[2]['obtido'],
                # self.inputOutputLLM[3]['esperado'],
                # self.inputOutputLLM[3]['obtido'],
            ]
            sheet.append(resultado_caso_teste)
        # Salvar a planilha
        workbook.save(excel_file)
    