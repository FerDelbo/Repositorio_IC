
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

    def test_verificar_string_1(self):
        valores = ["[27740,26598,15468]"]
        result = verificar_string("plateia: 5123.0 camarotes inferiores: 1208.0 camarotes superiores: 987.0 plateia", valores, self.file, 1)
        self.assertTrue(result[2])

    def test_verificar_string_4(self):
        valores = ["[27740,26598,15468]"]
        result = verificar_string_tolerante("plateia: 5123.0
camarotes inferiores: 1208.0
camarotes superiores: 987.0
plateia", valores, self.file, 4)
        self.assertTrue(result[2])

    def test_verificar_string_2(self):
        valores = ["[47612,78142,60342]"]
        result = verificar_string("plateia: 1322.0
camarotes inferiores: 7054.0
camarotes superiores: 3265.0
camarotes inferiores", valores, self.file, 2)
        self.assertTrue(result[2])

    def test_verificar_string_5(self):
        valores = ["[47612,78142,60342]"]
        result = verificar_string_tolerante("plateia: 1322.0
camarotes inferiores: 7054.0
camarotes superiores: 3265.0
camarotes inferiores", valores, self.file, 5)
        self.assertTrue(result[2])

    def test_verificar_string_3(self):
        valores = ["[2164,9042,10890]"]
        result = verificar_string("plateia: 16.0
camarotes inferiores: 350.0
camarotes superiores: 820.0
camarotes superiores", valores, self.file, 3)
        self.assertTrue(result[2])

    def test_verificar_string_6(self):
        valores = ["[2164,9042,10890]"]
        result = verificar_string_tolerante("plateia: 16.0
camarotes inferiores: 350.0
camarotes superiores: 820.0
camarotes superiores", valores, self.file, 6)
        self.assertTrue(result[2])


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
