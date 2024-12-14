
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
        valores_entrada = ["1700.00", "302.36", "405.69", "506.89", "403.65"]
        self.assertTrue(verificar_string("1618.59\nDentro do limite", valores_entrada, self.file))
    
    def test_verificar_string_2(self):
        valores_entrada = ["3100.00", "899.99", "789.98", "845.98", "635.28"]
        self.assertTrue(verificar_string("3171.23\nEstourou o limite", valores_entrada, self.file))
    
    def test_verificar_string_3(self):
        valores_entrada = ["850.00", "174.63", "243.27", "242.12", "189.98"]
        self.assertTrue(verificar_string("850.0\nDentro do limite", valores_entrada, self.file))
    
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
        
