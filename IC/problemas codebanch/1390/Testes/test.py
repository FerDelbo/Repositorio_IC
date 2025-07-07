
import unittest
import sys
import io
import os

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
        valores_entrada = ["50"]
        resultado = verificar_string("60.0", valores_entrada, self.file, test_id=1)
        self.assertTrue(resultado[2], msg=f"String1 = {resultado[1]} resultado obtido = {resultado[0]}")
    
    def test_verificar_string_4(self):
        valores_entrada = ["50"]
        resultado = verificar_string_tolerante("60.0", valores_entrada, self.file, test_id=4)
        self.assertTrue(resultado[2], msg=f"String1 = {resultado[1]} resultado obtido = {resultado[0]}")
    
    def test_verificar_string_2(self):
        valores_entrada = ["120"]
        resultado = verificar_string("193.0", valores_entrada, self.file, test_id=2)
        self.assertTrue(resultado[2], msg=f"String1 = {resultado[1]} resultado obtido = {resultado[0]}")
    
    def test_verificar_string_5(self):
        valores_entrada = ["120"]
        resultado = verificar_string_tolerante("193.0", valores_entrada, self.file, test_id=5)
        self.assertTrue(resultado[2], msg=f"String1 = {resultado[1]} resultado obtido = {resultado[0]}")
    
    def test_verificar_string_3(self):
        valores_entrada = ["199, "]
        resultado = verificar_string("303.6", valores_entrada, self.file, test_id=3)
        self.assertTrue(resultado[2], msg=f"String1 = {resultado[1]} resultado obtido = {resultado[0]}")
    
    def test_verificar_string_6(self):
        valores_entrada = ["199, "]
        resultado = verificar_string_tolerante("303.6", valores_entrada, self.file, test_id=6)
        self.assertTrue(resultado[2], msg=f"String1 = {resultado[1]} resultado obtido = {resultado[0]}")
    
def runTest(nameLLm, prompt, language, outDir, id, k):
    import xmlrunner as r
    import glob

    file = glob.glob(f"{outDir}/**/{nameLLm}{prompt}{language}.py", recursive=True)
    TestStringVerification.file = file[0]
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStringVerification)
    outDir = outDir +"/XML"
    if not(os.path.exists(outDir)):
        os.makedirs(outDir,exist_ok=True)
    runner = r.XMLTestRunner(output=outDir, outsuffix=f"{prompt}resultado_{id}_{k}") #prompt, id
    re = runner.run(suite)
    print(re)
        
    del(glob)
    del(r)
    return test_results
        