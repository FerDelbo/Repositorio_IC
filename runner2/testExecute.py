# import importlib.util
# import glob
# import os

# class TestExecute:
#     def __init__(self, path, session, path_excel):
#         self.path_code_test = path # Aqui está o caminho do código
#         self.session = session # A sessão que está sendo executada
#         self.path_excel = path_excel
        
    
#     def module_from_file(self, module_name, file_path):
#         spec = importlib.util.spec_from_file_location(module_name, file_path)
#         module = importlib.util.module_from_spec(spec)
#         spec.loader.exec_module(module)
#         return module

#     def create_test(self):
#         test_case = self.session.exercise.getTestCase()
#         modelo_caso_teste = """
#     def test_verificar_string_%d(self):
#         valores_entrada = ["%s"]
#         resultado = verificar_string("%s", valores_entrada, self.file, test_id=%d)
#         self.assertTrue(resultado[2], msg=f"String1 = {resultado[1]} resultado obtido = {resultado[0]}")
#     """
#         modelo_caso_teste2 = """
#     def test_verificar_string_%d(self):
#         valores_entrada = ["%s"]
#         resultado = verificar_string_tolerante("%s", valores_entrada, self.file, test_id=%d)
#         self.assertTrue(resultado[2], msg=f"String1 = {resultado[1]} resultado obtido = {resultado[0]}")
#     """

#         preambulo = """
# import unittest
# import sys
# import io
# import os

# test_results = {}


# def verificar_string(string1, valores_entrada,arquivo, test_id):
#     results = []
#     results.append(string1)
#     # Abre o arquivo 'codigo.py' e lê o seu conteúdo
#     with open(arquivo, 'r') as file:
#         codigo = file.read()

#     # Redireciona a saída padrão para um objeto io.StringIO
#     stdout_backup = sys.stdout
#     sys.stdout = io.StringIO()

#     # Cria um iterador para fornecer os valores de entrada sequencialmente
#     input_mock = iter(valores_entrada)

#     # Função de input mockada para retornar os valores do iterador
#     def input_mock_function(*args):
#         return next(input_mock)

#     try:
#         # Executa o código lido do arquivo com o input mockado
#         exec(codigo, {'input': input_mock_function})
#         valor_impresso1 = sys.stdout.getvalue().strip()#colocar na planilha

#     except Exception as e:
#         print(f"Erro ao executar o código: {e}")
#         results.append("")
#         results.append(False)
#         return results
#     finally:
#         # Restaura a saída padrão
#         sys.stdout = stdout_backup

#     # Verifica se os valores impressos são iguais às strings fornecidas
#     # results.append(string1)
#     results.append(valor_impresso1)
#     results.append(string1 == valor_impresso1)
    
#     test_results[test_id] = {
#         'esperado': string1,
#         'obtido': valor_impresso1,
#     }
#     return results#colocar string1 planilha
    
# def verificar_string_tolerante(string1, valores_entrada,arquivo, test_id):
#     results = []
#     results.append(string1)
#     # Abre o arquivo 'codigo.py' e lê o seu conteúdo
#     with open(arquivo, 'r') as file:
#         codigo = file.read()

#     # Redireciona a saída padrão para um objeto io.StringIO
#     stdout_backup = sys.stdout
#     sys.stdout = io.StringIO()

#     # Cria um iterador para fornecer os valores de entrada sequencialmente
#     input_mock = iter(valores_entrada)

#     # Função de input mockada para retornar os valores do iterador
#     def input_mock_function(*args):
#         return next(input_mock)

#     try:
#         # Executa o código lido do arquivo com o input mockado
#         exec(codigo, {'input': input_mock_function})
#         valor_impresso1 = sys.stdout.getvalue().strip()#colocar na planilha

#     except Exception as e:
#         print(f"Erro ao executar o código: {e}")
#         results.append("")
#         results.append(False)
#         return results
#     finally:
#         # Restaura a saída padrão
#         sys.stdout = stdout_backup

#     # Verifica se os valores impressos são iguais às strings fornecidas
#     # results.append(string1)
#     results.append(valor_impresso1)
#     results.append(string1 in valor_impresso1)
    
#     test_results[test_id] = {
#         'esperado': string1,
#         'obtido': valor_impresso1,
#     }
#     return results#colocar string1 planilha
    
# class TestStringVerification(unittest.TestCase):
#         """

#         main = """
# def runTest(nameLLm, prompt, language, outDir, id, k):
#     import xmlrunner as r
#     import glob

#     file = glob.glob(f"{outDir}/**/{nameLLm}{prompt}{language}.py", recursive=True)
#     TestStringVerification.file = file[0]
#     suite = unittest.TestLoader().loadTestsFromTestCase(TestStringVerification)
#     outDir = outDir +"/XML"
#     if not(os.path.exists(outDir)):
#         os.makedirs(outDir,exist_ok=True)
#     runner = r.XMLTestRunner(output=outDir, outsuffix=f"{prompt}resultado_{id}_{k}") #prompt, id
#     runner.run(suite)
        
#     del(glob)
#     del(r)
#     return test_results
#         """
#         caseStudy =[]
#         i=1
#         j=4
#         if len(test_case) == 0: #dicionario vazio, sem casos de testes
#             return
#         else:
#             for key, value in test_case.items():
#                 caseStudy.append(modelo_caso_teste % (i, key, value, i))
#                 caseStudy.append(modelo_caso_teste2 % (j, key, value, j))
#                 i += 1
#                 j += 1
#             conteudo = preambulo + "".join(str(caso_de_teste) for caso_de_teste in caseStudy) + main
#             #criar um arquivo chamdo test.py para deixar no formato adequado
#             path_test = self.session.session.getInputDirectory() + f"/problemas codebanch/{self.session.exercise.getId()}/Testes/test.py"
#             os.makedirs(f"{self.session.session.getInputDirectory()}/problemas codebanch/{self.session.exercise.getId()}/Testes/",exist_ok=True)
#             open(path_test, "w").write(conteudo)
#             return path_test 

#     def search_test_case(self):
#         path_test = glob.glob(f"{self.session.session.getInputDirectory()}/**/{self.session.exercise.getId()}/Testes/test.py", recursive=True)
#         if len(path_test) == 0:
#             return None
#         return path_test[0]
    
#     def runTestCase(self):
#     #fazer a busca com o nome do exercico e usar o import module 
#         path_test = self.search_test_case()
#         # if path_test is None:
#         #     path_test = self.create_test()
#         test = self.module_from_file("test", path_test)
#         self.row_table_save = test.runTest(self, self.path_excel)
    
#     def get_path_code_test(self):
#         return self.path_code_test

import importlib.util
import glob
import os

class TestExecute:
    def __init__(self, path, session, path_excel):
        self.path_code_test = path
        self.session = session
        self.path_excel = path_excel

    def module_from_file(self, module_name, file_path):
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def create_test(self):
        test_case = self.session.exercise.getTestCase()

        preambulo = """
import unittest
import sys
import io
from sheet import Sheet

test_results = {}

def verificar_string(string1, valores_entrada, arquivo, test_id):
    results = [string1]

    try:
        with open(arquivo, 'r') as file:
            codigo = file.read()
    except Exception as e:
        print(f"Erro ao abrir o arquivo: {e}")
        test_results[test_id] = {'esperado': string1, 'obtido': f"Erro: {e}"}
        return [string1, "", False]

    stdout_backup = sys.stdout
    sys.stdout = io.StringIO()

    input_mock = iter(valores_entrada)
    def input_mock_function(*args): return next(input_mock)

    try:
        exec(codigo, {'input': input_mock_function})
        valor_impresso1 = sys.stdout.getvalue().strip()
    except Exception as e:
        valor_impresso1 = f"Erro ao executar o código: {e}"
        resultado = False
    else:
        resultado = string1 == valor_impresso1
    finally:
        sys.stdout = stdout_backup

    test_results[test_id] = {
        'esperado': string1,
        'obtido': valor_impresso1
    }

    return [string1, valor_impresso1, resultado]

def verificar_string_tolerante(string1, valores_entrada, arquivo, test_id):
    results = [string1]

    try:
        with open(arquivo, 'r') as file:
            codigo = file.read()
    except Exception as e:
        print(f"Erro ao abrir o arquivo: {e}")
        test_results[test_id] = {'esperado': string1, 'obtido': f"Erro: {e}"}
        return [string1, "", False]

    stdout_backup = sys.stdout
    sys.stdout = io.StringIO()

    input_mock = iter(valores_entrada)
    def input_mock_function(*args): return next(input_mock)

    try:
        exec(codigo, {'input': input_mock_function})
        valor_impresso1 = sys.stdout.getvalue().strip()
    except Exception as e:
        valor_impresso1 = f"Erro ao executar o código: {e}"
        resultado = False
    else:
        resultado = string1 in valor_impresso1
    finally:
        sys.stdout = stdout_backup

    test_results[test_id] = {
        'esperado': string1,
        'obtido': valor_impresso1
    }

    return [string1, valor_impresso1, resultado]


class TestStringVerification(unittest.TestCase):
"""

        modelo_caso_teste = """
    def test_verificar_string_%d(self):
        valores = [%r]
        result = verificar_string(%r, valores, self.file, %d)
        self.assertTrue(result[2])
"""
        modelo_caso_teste2 = """
    def test_verificar_string_%d(self):
        valores = [%r]
        result = verificar_string_tolerante(%r, valores, self.file, %d)
        self.assertTrue(result[2])
"""

        custom_result_class = """
class CustomTestResult(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.passed = []
        self.failed = []

    def addSuccess(self, test):
        super().addSuccess(test)
        self.passed.append(str(test))

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.failed.append(str(test))

    def addError(self, test, err):
        super().addError(test, err)
        self.failed.append(str(test))


def runTest(test, path_excel):
    path = test.get_path_code_test()
    TestStringVerification.file = path

    suite = unittest.TestLoader().loadTestsFromTestCase(TestStringVerification)
    runner = unittest.TextTestRunner(resultclass=CustomTestResult, verbosity=0)
    result = runner.run(suite)

    dict_test_results = {
        "total": result.testsRun,
        "passed": len(result.passed),
        "failed": len(result.failed),
        "passed_names": result.passed,
        "failed_names": result.failed,
        "esperado_e_obtido": test_results
    }

    row = Sheet(test.session.exercise, test.session.llm, path_excel, dict_test_results)
    return row
"""

        if not test_case:
            return None

        caseStudy = []
        i, j = 1, len(test_case) + 1

        for key, value in test_case.items():
            caseStudy.append(modelo_caso_teste % (i, key, value, i))
            caseStudy.append(modelo_caso_teste2 % (j, key, value, j))
            i += 1
            j += 1

        conteudo = preambulo + "".join(caseStudy) + "\n" + custom_result_class
        path_test = os.path.join(
            self.session.session.getInputDirectory(),
            f"problemas codebanch/{self.session.exercise.getId()}/Testes/test.py"
        )
        os.makedirs(os.path.dirname(path_test), exist_ok=True)
        with open(path_test, "w") as f:
            f.write(conteudo)

        return path_test

    def search_test_case(self):
        path_test = glob.glob(
            f"{self.session.session.getInputDirectory()}/**/{self.session.exercise.getId()}/Testes/test.py",
            recursive=True
        )
        return path_test[0] if path_test else None

    def runTestCase(self):
        path_test = self.search_test_case()
        if path_test is None:
            path_test = self.create_test()
            path_test = self.search_test_case()
        test = self.module_from_file("test", path_test)
        self.row_table_save = test.runTest(self, self.path_excel)

    def get_path_code_test(self):
        return self.path_code_test
