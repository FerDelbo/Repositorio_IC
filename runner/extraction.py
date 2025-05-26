import xml.etree.ElementTree as ET
import openpyxl
import glob
import sys

class XMLExtractor:
    def __init__(self, fileXML, nameExercise, nameLLM, language, prompt, temp, test_results):
        self.fileXML = fileXML
        self.nameExercise = nameExercise
        self.nameLLM = nameLLM
        self.language = language
        self.partPrompt = prompt
        self.temperature = temp
        self.inputOutputLLM = test_results

    def extractData(self):
        # Transformar o arquivo XML em uma árvore
        tree = ET.parse(self.fileXML)
        root = tree.getroot()

        # Obter atributos do testsuite
        listTestsuite = root.attrib
        
        from datetime import datetime
        listTestsuite['timestamp'] = datetime.now()
        # Dicionário de componentes a serem extraídos
        components = {
            "NomeExercicio": self.nameExercise,
            "NomeLLM": self.nameLLM,
            "Temperatura": self.temperature,
            "Data/Hora": listTestsuite['timestamp'],
            "QtdFalhas": str(int(listTestsuite['failures']) + int(listTestsuite['errors'])),
            "QtdAcerto": str(int(listTestsuite['tests']) - int(listTestsuite['failures']) - int(listTestsuite['errors'])),
            "NomeFalha": '',
            "NomeAcerto": '',
            "Idioma": self.language,
            "Prompt": self.partPrompt[0],
            "Git": '',
            "NomeCasoTeste" : [],
            "ResultadoCasoTeste" : [],
        }
        
        del(datetime)

        import git
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
        del(git)
        return components

    def saveExcel(self, components):
        # Abrir a planilha
        excel_file = '/home/fernando/Área de trabalho/Projeto/testesNovos.xlsx'
        # excel_file = '/home/fernando/Área de trabalho/Projeto/solucoesLLM.xlsx'
        workbook = openpyxl.load_workbook(excel_file)
        sheet = workbook.active

        # Adicionar os dados à planilha
        for i in self.inputOutputLLM.keys():
            resultado_caso_teste = [
                components["NomeExercicio"],
                components["Idioma"],
                components["NomeLLM"],
                components["Temperatura"],
                components["Prompt"],
                components["Data/Hora"],
                components["QtdFalhas"],
                components["QtdAcerto"],
                components["NomeFalha"],
                components["NomeAcerto"],
                components["Git"],
                str(components['NomeCasoTeste'][i-1]),
                str(components['ResultadoCasoTeste'][i-1]),
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
    
def run(nameExercise, nameLLM, language, prompt, outDir, temp, test_results, k):
    xml= glob.glob(f'{outDir}/**/*{prompt}*_{nameExercise}_{k}.xml', recursive=True)
    extractor = XMLExtractor(xml[0], nameExercise, nameLLM, language, prompt, temp, test_results)
    dados = extractor.extractData()
    extractor.saveExcel(dados)
    
if __name__ == "__main__":
    nameExercise = sys.argv[1]
    nameLLM = sys.argv[2]
    run(nameExercise, nameLLM)
    