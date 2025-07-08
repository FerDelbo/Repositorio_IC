from session import SessionManager
from testExecute import TestExecute

s = SessionManager('/home/fernando/Área de trabalho/Projeto/enunciadosCodeBench.xlsx')
path = s.create(base_directory='/home/fernando/Área de trabalho/Projeto/Repositorio_IC/IC',
               output_directory='/home/fernando/Área de trabalho/Projeto/solucaos')
# print(s.outDirectory)
# Teste se a session esta sendo ocorrida
# print(path)
# print(s.session.session_id)

# Teste se a classe exercicio esta sendo criada
exe = s.listExercise('1289', 'pt')
# print(exe.name)
# print(exe)
# print(exe.getTestCase())

# Teste configurar LLM
llm = s.settingLLM('GPT4o', 0.7)
# llm.generate()
# print(llm.getContent())

# # Teste salvar aquivo
# s.saveContent()

# Teste para executar os casos de teste e criar uma linha da planilha
t = TestExecute(path='/home/fernando/Área de trabalho/Projeto/Repositorio_IC/IC/problemas codebanch/1289/Testes/test.py', session=s, path_excel='/home/fernando/Área de trabalho/Projeto/solucoesLLM.xlsx')
t.runTestCase()
row = t.row_table_save
print("=======TESTES===========")
print("Total de testes: ", row.total_test)
print("Total de testes que passou: ", row.passed_test)
print("Total de testes falho: ", row.failed_test)
print("Nome dos testes que passaram: ", row.passed_test_names)
print("Nome dos testes que falharam: ", row.failed_test_names)
print("Saidas obtidas e saidas esperadas: ",row.expected_and_obtained)