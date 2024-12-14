
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
        valores_entrada = ["[8956,2700,1628]"]
        self.assertTrue(verificar_string("centurion: 150.0\ntribune: 190.0\nsenator: 366.0\ncenturion", valores_entrada, self.file))
    
    def test_verificar_string_2(self):
        valores_entrada = ["[24642,7104,4218]"]
        self.assertTrue(verificar_string("centurion: 999.0\ntribune: 777.0\nsenator: 555.0\nsenator", valores_entrada, self.file))
    
    def test_verificar_string_3(self):
        valores_entrada = ["[19430,5548,3147]"]
        self.assertTrue(verificar_string("centurion: 1020.0\ntribune: 111.0\nsenator: 635.0\ntribune", valores_entrada, self.file))
    
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
        
