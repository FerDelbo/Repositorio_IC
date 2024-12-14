
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
        
    def test_verificar_string_1(self):
        valores_entrada = ["[186070,341000,741570,1368195]"]
        self.assertTrue(verificar_string("titica: 9875.0\nbarro no balde: 3215.0\nbestrume: 1236.0\ncaca de vaca: 7415.0\nbestrume", valores_entrada, self.file))
    
    def test_verificar_string_2(self):
        valores_entrada = ["[12849,62280,94710,77025]"]
        self.assertTrue(verificar_string("titica: 321.0\nbarro no balde: 654.0\nbestrume: 987.0\ncaca de vaca: 159.0\ncaca de vaca", valores_entrada, self.file))
    
    def test_verificar_string_3(self):
        valores_entrada = ["[12111,51660,75450,52995]"]
        self.assertTrue(verificar_string("titica: 123.0\nbarro no balde: 456.0\nbestrume: 789.0\ncaca de vaca: 321.0\ntitica", valores_entrada, self.file))
    
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
        
