import importlib.util
import glob

def module_from_file(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestExecute:
    def __init__(self, nameProblem, nameLLM, partPrompt, language, session, outputDir, inputDir, testcase):
        self.input_dirctory = inputDir
        self.output_dirctory = outputDir
        self.nameproblem = nameProblem
        self.nameLLM = nameLLM
        self.partPrompt = partPrompt
        self.language = language
        self.session = session
        self.fileTestCase = testcase
        self.testCase = {}
    
    def __removeTestCase(self):
        #abre o arquivo com todos os casos de testes e busca o qual vai ser usado de acordo com o id e retira todo o contudo que pertence aquele problema
        with open(self.fileTestCase, 'r') as file:
            lines = file.readlines()
            NewtestCase = []
            flag = False
            problemName = f"Exercício de ID: {self.nameproblem}" 
            for l in lines:
                if problemName in l:
                    flag = True
                if flag:
                    NewtestCase.append(l)
                if flag and "-- GRADE" in l:
                    flag = False
                    break
        
        start = False
        input_value = ""
        for i, linha in enumerate(NewtestCase):
            if linha.startswith("---- input:"):
                start = True
                input_value = ""
            elif linha.startswith("---- correct output:") and i + 1 < len(NewtestCase):
                start = False
                correct_output = NewtestCase[i + 1].strip()
                self.testCase[input_value] = correct_output
            elif linha.startswith("-- GRADE:"):
                break
            elif start:
                input_value += linha.strip()
        print(self.testCase)

    def test(self):
        self.__removeTestCase()#metodo que faz a remoção dos casos de teste e salva em um self.testCase
        modelo_caso_teste = """
    def test_verificar_string_%d(self):
        valores_entrada = ["%s"]
        self.assertTrue(verificar_string("%s", valores_entrada, self.file))
    """

        preambulo = """
import unittest
import sys
import io
import os

def verificar_string(string1, valores_entrada,arquivo):
    # Abre o arquivo 'codigo.py' e lê o seu conteúdo
    with open(arquivo, 'r') as file:
        codigo = file.read()

    # Redireciona a saída padrão para um objeto io.StringIO
    stdout_backup = sys.stdout
    sys.stdout = io.StringIO()

    # Cria um iterador para fornecer os valores de entrada sequencialmente
    input_mock = iter(valores_entrada)

    # Função de input mockada para retornar os valores do iterador
    def input_mock_function(*args):
        return next(input_mock)

    try:
        # Executa o código lido do arquivo com o input mockado
        exec(codigo, {'input': input_mock_function})
        valor_impresso1 = sys.stdout.getvalue().strip()

    except Exception as e:
        print(f"Erro ao executar o código: {e}")
        return False
    finally:
        # Restaura a saída padrão
        sys.stdout = stdout_backup

    # Verifica se os valores impressos são iguais às strings fornecidas
    return string1 == valor_impresso1
    
class TestStringVerification(unittest.TestCase):
        """

        main = """
def runTest(nameLLm, prompt, language, outDir, id):
    import xmlrunner as r
    import glob

    file = glob.glob(f"{outDir}/**/{nameLLm}{prompt}{language}.py", recursive=True)
    TestStringVerification.file = file[0]
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStringVerification)
    outDir = outDir +"/XML"
    if not(os.path.exists(outDir)):
        os.makedirs(outDir,exist_ok=True)
    runner = r.XMLTestRunner(output=outDir, outsuffix=f"{prompt}resultado_{id}") #prompt, id
    runner.run(suite)
        
    del(glob)
    del(r)
        """
        caseStudy =[]
        i=1
        for key, value in self.testCase.items():
            caseStudy.append(modelo_caso_teste % (i, key, value))
            i += 1
        conteudo = preambulo + "".join(str(caso_de_teste) for caso_de_teste in caseStudy) + main
        namespace = {}
        exec(conteudo, namespace)
        namespace['runTest'](self.nameLLM, self.partPrompt[0], self.language, self.output_dirctory, self.nameproblem)   
        
    def runTestCase(self,):
    #fazer a busca com o nome do exercico e usar o import module 
        path = glob.glob(f'{self.input_dirctory}/**/{self.nameproblem}*/**/test.py', recursive=True)
        if(len(path) == 0):
            self.test()
        else:
            test = module_from_file("test", path[0])
            test.runTest(self.nameLLM, self.partPrompt[0], self.language, self.output_dirctory)
            del(test)
    