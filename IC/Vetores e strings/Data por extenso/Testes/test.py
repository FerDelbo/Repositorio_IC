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
        with open('/home/fernando/Área de Trabalho/Projeto/returnTestCase.txt', 'w') as f:
            f.write("\nExecusão do caso de teste data\n")
            f.write(valor_impresso1)

    except Exception as e:
        print(f"Erro ao executar o código: {e}")
        return False
    finally:
        # Restaura a saída padrão
        sys.stdout = stdout_backup

    # Verifica se os valores impressos são iguais às strings fornecidas
    return string1 == valor_impresso1


class TestStringVerification(unittest.TestCase):
    #file = 'codigo.py'
    def test_verificar_string_1(self):
        valores_entrada = ["01092023"]
        self.assertTrue(verificar_string("01 de setembro de 2023", valores_entrada,self.file))

    def test_verificar_string_2(self):
        valores_entrada = ["17031909"]
        self.assertTrue(verificar_string("17 de marco de 1909", valores_entrada,self.file))

    def test_verificar_string_3(self):
        valores_entrada = ["31021031"]
        self.assertTrue(verificar_string("31 de fevereiro de 1031", valores_entrada,self.file))

def runTest(nameLLm, prompt, language, outDir, nameProblem, k):
    import xmlrunner as r
    import glob

    file = glob.glob(f"{outDir}/**/{nameLLm}{prompt}{language}.py", recursive=True)
    TestStringVerification.file = file[0]
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStringVerification)
    outDir = outDir +"/XML"
    if not(os.path.exists(outDir)):
        os.makedirs(outDir,exist_ok=True)
    #runner = r.XMLTestRunner(output=outDir, outsuffix=f"{prompt}resultado_Data")
    runner = r.XMLTestRunner(output=outDir, outsuffix=f"{prompt}resultado_{nameProblem}")
    runner.run(suite)
    
    del(glob)
    del(r)

if __name__ == '__main__':
    #parametros que devem ser passados:
    #arg1 -> nome LLM
    #arg2 -> qual parte do prompt
    #arg3 ->idioma (pt, eng, eng2)  
    runTest(arg1=sys.argv[1], arg2=sys.argv[2], arg3=sys.argv[3])