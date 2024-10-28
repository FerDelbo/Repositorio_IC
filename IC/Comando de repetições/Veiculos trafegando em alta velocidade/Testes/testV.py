import unittest
import sys
import io
import os


def verificar_string(valores_esperados, valores_entrada,arquivo):
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
        valor_impresso = sys.stdout.getvalue().strip()
        # partes = valor_impresso.split('\n')
        # saida1 = partes[0]
        # saida2 = partes[1]
        # saida3 = partes[2]

    except Exception as e:
        print(f"Erro ao executar o código: {e}")
        return False
    finally:
        # Restaura a saída padrão
        sys.stdout = stdout_backup

    # Verifica se os valores impressos são iguais às strings fornecidas
    if(valores_esperados == valor_impresso):
        return True
    else:
        return False


class TestStringVerification(unittest.TestCase):
    #file = 'codigo.py'
    def test_verificar_string_1(self):
        valores_entrada = ["[60.0, 73.9, 22.9, 72.1, 72.0, 100.6]"] 
        self.assertTrue(verificar_string("1\n3\n2", valores_entrada,self.file))
        
    def test_verificar_string_2(self):
        valores_entrada = ["[11.6, 60.6, 16.6, 11.35]"]
        self.assertTrue(verificar_string("2\n1", valores_entrada,self.file))

    def test_verificar_string_3(self):
        valores_entrada = ["[72.9, 29.1, 7.29, 90.7, 66.6]"]
        self.assertTrue(verificar_string("3\n1", valores_entrada,self.file))

def runTest(arg1, arg2, arg3, arg4):
    import xmlrunner as r
    import glob 
       
    file = glob.glob(f"/home/**/Repositorio_IC/**/Veiculos*/**/{arg4}/{arg1}{arg2}{arg3}.py", recursive=True)
    print(file)
    TestStringVerification.file = file[0]
    # #unittest.main(argv=[''], testRunner=r.XMLTestRunner(output='testeVeiculo', outsuffix="Veiculos"))
    # suite = unittest.TestLoader().loadTestsFromTestCase(TestStringVerification)
    # unittest.TextTestRunner().run(suite)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStringVerification)
    runner = r.XMLTestRunner(output='testeVeiculo', outsuffix="resultado_Veiculos")
    runner.run(suite)

    #outsuffix = time.strftime("%Y%m%d%H%M%S")

if __name__ == '__main__':
    #parametros que devem ser passados:
    #arg1 -> nome LLM
    #arg2 -> qual parte do prompt
    #arg3 ->idioma (pt, eng, eng2)
    runTest(arg1=sys.argv[1], arg2=sys.argv[2], arg3=sys.argv[3])
   
    