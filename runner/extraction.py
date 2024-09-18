import xml.etree.ElementTree as ET
import openpyxl
import glob
import sys

class XMLExtractor:
    def __init__(self, fileXML, nameExercise, nameLLM):
        self.fileXML = fileXML
        self.nameExercise = nameExercise
        self.nameLLM = nameLLM

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
            "NomeAcerto": ''
        }

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
            components["NomeAcerto"]
        ])

        # Salvar a planilha
        workbook.save(excel_file)
    
    def run(self):
        dados = extractor.extractData()
        extractor.saveExcel(dados)

def buscarXML(arg1):
    #xml= glob.glob(f'**/*{arg1}.xml', recursive=True)
    xml= glob.glob(f'/home/**/*{arg1}.xml', recursive=True)
    return xml

if __name__ == "__main__":
    nameExercise = sys.argv[1]
    nameLLM = sys.argv[2]
    fileXML = buscarXML(nameExercise)
    #print(fileXML)
    extractor = XMLExtractor(fileXML[0], nameExercise, nameLLM)
    extractor.run()
    