
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
        valores_entrada = ["[8.0,6.0,3.0,2.0], [8.0,4.0,5.0,10.0]"]
        self.assertTrue(verificar_string("[ 16.  10.   8.  12.]2", valores_entrada, self.file))
    
    def test_verificar_string_2(self):
        valores_entrada = ["[2.0,4.0,10.0,10.0], [10.0,8.0,5.0,6.0]"]
        self.assertTrue(verificar_string("[ 12.  12.  15.  16.]4", valores_entrada, self.file))
    
    def test_verificar_string_3(self):
        valores_entrada = ["[5.2,8.2,7.6,8.7], [9.2,8.7,7.6,4.9]"]
        self.assertTrue(verificar_string("[ 14.4  16.9  15.2  13.6]4", valores_entrada, self.file))
    
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
        