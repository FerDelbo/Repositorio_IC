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

def runTest(arg1, arg2, arg3):
    import xmlrunner as r
    import glob 
    #Maneira 1 -> faz a busca pelo qual foi passado pelo termianl + geral
    #base_path = '/home/fernando/Área de Trabalho/Projeto/Repositorio_IC/'
    #file = glob.glob(f"{base_path}**/{sys.argv[1]}*/**/{sys.argv[2]}*{sys.argv[3]}*{sys.argv[4]}.py", recursive=True)
    
    #Maneira 2 -> faz a busca por parametro de terminal mas já dentro do diretorio Veículos Trafegando em Alta Velocidade + seguro
    file = glob.glob(f"/home/fernando/Área de Trabalho/Projeto/Repositorio_IC/**/Veículos*/**/{arg1}{arg2}{arg3}.py", recursive=True)
    #print(file)
    TestStringVerification.file = file[0]
    unittest.main(argv=sys.argv[:1], testRunner=r.XMLTestRunner(output='testeVeiculo', outsuffix="Veiculos"))
    #outsuffix = time.strftime("%Y%m%d%H%M%S")

if __name__ == '__main__':
    runTest(arg1=sys.argv[1], arg2=sys.argv[2], arg3=sys.argv[3])
   
    