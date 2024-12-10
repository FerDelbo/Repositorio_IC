
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
        valores_entrada = ["[64.58,77.85,45.96,55.55], [1.62,1.84,1.55,1.66]"]
        self.assertTrue(verificar_string("[ 24.61  22.99  19.13  20.16]O MAIOR IMC DA TURMA EH: 24.61PESO NORMAL", valores_entrada, self.file))
    
    def test_verificar_string_2(self):
        valores_entrada = ["[34.67,45.78,55.89], [1.98,1.88,1.79]"]
        self.assertTrue(verificar_string("[  8.84  12.95  17.44]O MAIOR IMC DA TURMA EH: 17.44ABAIXO DO PESO", valores_entrada, self.file))
    
    def test_verificar_string_3(self):
        valores_entrada = ["[102.89,99.87], [1.65,1.77]"]
        self.assertTrue(verificar_string("[ 37.79  31.88]O MAIOR IMC DA TURMA EH: 37.79OBESIDADE SEVERA", valores_entrada, self.file))
    
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
        