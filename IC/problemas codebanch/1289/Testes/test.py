
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
        
#     def test_verificar_string_1(self):
#         valores_entrada = ["[6407.0,4872.0,10619.0,8319.5]"]
#         resultado = verificar_string("caminhada: 164.0corrida: 207.0bicicleta: 3198.0natacao: 2820.0bicicleta", valores_entrada, self.file, test_id=1)
#         self.assertTrue(resultado[2], msg=f"String1 = {resultado[1]} resultado obtido = {resultado[0]}")
    
#     def test_verificar_string_4(self):
#         valores_entrada = ["[6407.0,4872.0,10619.0,8319.5]"]
#         resultado = verificar_string_tolerante("caminhada: 164.0corrida: 207.0bicicleta: 3198.0natacao: 2820.0bicicleta", valores_entrada, self.file, test_id=4)
#         self.assertTrue(resultado[2], msg=f"String1 = {resultado[1]} resultado obtido = {resultado[0]}")
    
#     def test_verificar_string_2(self):
#         valores_entrada = ["[6248.0,7068.0,8351.0,13344.5]"]
#         resultado = verificar_string("caminhada: 3050.0corrida: 195.0bicicleta: 2556.0natacao: 1020.0caminhada", valores_entrada, self.file, test_id=2)
#         self.assertTrue(resultado[2], msg=f"String1 = {resultado[1]} resultado obtido = {resultado[0]}")
    
#     def test_verificar_string_5(self):
#         valores_entrada = ["[6248.0,7068.0,8351.0,13344.5]"]
#         resultado = verificar_string_tolerante("caminhada: 3050.0corrida: 195.0bicicleta: 2556.0natacao: 1020.0caminhada", valores_entrada, self.file, test_id=5)
#         self.assertTrue(resultado[2], msg=f"String1 = {resultado[1]} resultado obtido = {resultado[0]}")
    
#     def test_verificar_string_3(self):
#         valores_entrada = ["[9902.0,6825.5,15785.0,5539.0]"]
#         resultado = verificar_string("caminhada: 195.0corrida: 325.0bicicleta: 1020.0natacao: 5698.0natacao", valores_entrada, self.file, test_id=3)
#         self.assertTrue(resultado[2], msg=f"String1 = {resultado[1]} resultado obtido = {resultado[0]}")
    
#     def test_verificar_string_6(self):
#         valores_entrada = ["[9902.0,6825.5,15785.0,5539.0]"]
#         resultado = verificar_string_tolerante("caminhada: 195.0corrida: 325.0bicicleta: 1020.0natacao: 5698.0natacao", valores_entrada, self.file, test_id=6)
#         self.assertTrue(resultado[2], msg=f"String1 = {resultado[1]} resultado obtido = {resultado[0]}")
    
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
        
import unittest
import sys
import io
from sheet import Sheet

test_results = {}


def verificar_string(string1, valores_entrada,arquivo, test_id):
    results = []
    results.append(string1)
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
        valor_impresso1 = sys.stdout.getvalue().strip()#colocar na planilha

    except Exception as e:
        print(f"Erro ao executar o código: {e}")
        results.append("")
        results.append(False)
        return results
    finally:
        # Restaura a saída padrão
        sys.stdout = stdout_backup

    # Verifica se os valores impressos são iguais às strings fornecidas
    # results.append(string1)
    results.append(valor_impresso1)
    results.append(string1 == valor_impresso1)
    
    test_results[test_id] = {
        'esperado': string1,
        'obtido': valor_impresso1,
    }
    return results#colocar string1 planilha
    
def verificar_string_tolerante(string1, valores_entrada,arquivo, test_id):
    results = []
    results.append(string1)
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
        valor_impresso1 = sys.stdout.getvalue().strip()#colocar na planilha

    except Exception as e:
        print(f"Erro ao executar o código: {e}")
        results.append("")
        results.append(False)
        return results
    finally:
        # Restaura a saída padrão
        sys.stdout = stdout_backup

    # Verifica se os valores impressos são iguais às strings fornecidas
    # results.append(string1)
    results.append(valor_impresso1)
    results.append(string1 in valor_impresso1)
    
    test_results[test_id] = {
        'esperado': string1,
        'obtido': valor_impresso1,
    }
    return results#colocar string1 planilha


class TestStringVerification(unittest.TestCase):
    def test_verificar_string_1(self):
        valores = ["[6407.0,4872.0,10619.0,8319.5]"]
        self.assertTrue(verificar_string("caminhada: 164.0corrida: 207.0bicicleta: 3198.0natacao: 2820.0bicicleta", valores, self.file, 1))

    def test_verificar_string_2(self):
        valores = ["[6248.0,7068.0,8351.0,13344.5]"]
        self.assertTrue(verificar_string("caminhada: 3050.0corrida: 195.0bicicleta: 2556.0natacao: 1020.0caminhada", valores, self.file, 2))

    def test_verificar_string_3(self):
        valores = ["[9902.0,6825.5,15785.0,5539.0]"]
        self.assertTrue(verificar_string("caminhada: 195.0corrida: 325.0bicicleta: 1020.0natacao: 5698.0natacao", valores, self.file, 3))

    def test_verificar_string_4(self):
        valores = ["[6407.0,4872.0,10619.0,8319.5]"]
        self.assertTrue(verificar_string_tolerante("caminhada: 164.0corrida: 207.0bicicleta: 3198.0natacao: 2820.0bicicleta", valores, self.file, 4))

    def test_verificar_string_5(self):
        valores = ["[6248.0,7068.0,8351.0,13344.5]"]
        self.assertTrue(verificar_string_tolerante("caminhada: 3050.0corrida: 195.0bicicleta: 2556.0natacao: 1020.0caminhada", valores, self.file, 5))

    def test_verificar_string_6(self):
        valores = ["[9902.0,6825.5,15785.0,5539.0]"]
        self.assertTrue(verificar_string_tolerante("caminhada: 195.0corrida: 325.0bicicleta: 1020.0natacao: 5698.0natacao", valores, self.file, 6))


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

    row = Sheet(test.session.exercise, test.session.llm, path_excel, dict_test_results) # O path não deve ser a planilha
    return row