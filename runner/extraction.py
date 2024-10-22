import xml.etree.ElementTree as ET
import openpyxl
import glob
import sys

class XMLExtractor:
    def __init__(self, fileXML, nameExercise, nameLLM, language, prompt):
        self.fileXML = fileXML
        self.nameExercise = nameExercise
        self.nameLLM = nameLLM
        self.language = language
        self.prompt = prompt

    def extractData(self):
        # Transformar o arquivo XML em uma árvore
        tree = ET.parse(self.fileXML)
        root = tree.getroot()

        # Obter atributos do testsuite
        listTestsuite = root.attrib

        # Dicionário de componentes a serem extraídos
        components = {
            "NomeExercicio": self.nameExercise,
            "NomeLLM": self.nameLLM,
            "Data/Hora": listTestsuite['timestamp'],
            "QtdFalhas": listTestsuite['failures'],
            "QtdAcerto": str(int(listTestsuite['tests']) - int(listTestsuite['failures'])),
            "NomeFalha": '',
            "NomeAcerto": '',
            "Idioma": self.language,
            "Prompt": self.prompt,
            "Git": ''
        }

        import git
        repo = git.Repo(search_parent_directories=True)
        sha = repo.head.object.hexsha
        components['Git'] = sha 

        falhas = []
        acertos = []

        # Iterar sobre os elementos 'testcase' e coletar nomes de testes que falharam ou passaram
        for testcase in root.iter('testcase'):
            nome_teste = testcase.attrib['name']
            if testcase.find('failure') is not None:
                falhas.append(nome_teste)
            else:
                acertos.append(nome_teste)

        components['NomeFalha'] = "; ".join(falhas)
        components['NomeAcerto'] = "; ".join(acertos)

        return components

    def saveExcel(self, components):
        # Abrir a planilha
        excel_file = '/home/fernando/Área de Trabalho/Projeto/planilhaIC.xlsx'
        workbook = openpyxl.load_workbook(excel_file)
        sheet = workbook.active

        # Adicionar os dados à planilha
        sheet.append([
            components["NomeExercicio"],
            components["NomeLLM"],
            components["Data/Hora"],
            components["QtdFalhas"],
            components["QtdAcerto"],
            components["NomeFalha"],
            components["NomeAcerto"],
            components["Idioma"],
            components["Prompt"],
            components["Git"]
        ])

        # Salvar a planilha
        workbook.save(excel_file)
    
def run(nameExercise, nameLLM, language, prompt):
    #print("Iniciando!")
    xml= glob.glob(f'/home/**/*{nameExercise}.xml', recursive=True)
    #print(xml)
    extractor = XMLExtractor(xml[0], nameExercise, nameLLM, language, prompt)
    dados = extractor.extractData()
    extractor.saveExcel(dados)
    #print("salvo vom sucesso!")

if __name__ == "__main__":
    nameExercise = sys.argv[1]
    nameLLM = sys.argv[2]
    run(nameExercise, nameLLM)
    