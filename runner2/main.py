from session import SessionManager
from testExecute import TestExecute
import sheet

s = SessionManager('/home/fernando/Área de trabalho/Projeto/enunciadosCodeBench.xlsx')
path = s.create(base_directory='/home/fernando/Área de trabalho/Projeto/Repositorio_IC/IC',
               output_directory='/home/fernando/Área de trabalho/Projeto/solucaos')
# print(s.outDirectory)
# Teste se a session esta sendo ocorrida
print(path)
print(s.session.session_id)

# Teste se a classe exercicio esta sendo criada
exe = s.listExercise('1293', 'pt')
# print(exe.name)
# print(exe)
print(exe.getTestCase())

# Teste configurar LLM
llm = s.settingLLM('Gemini', 0.7)
llm.generate()
print(llm.getContent())

# Teste salvar aquivo
s.saveContent()
print(s.path_code)


# # Teste para executar os casos de teste e criar uma linha da planilha
t = TestExecute(
    path=s.path_code, 
    session=s,
    path_excel='/home/fernando/Área de trabalho/Projeto/solucoesLLM.xlsx')
# t = TestExecute(path='/home/fernando/Área de trabalho/Projeto/solucaos/2025-09-15/1293/Gemini/sed - teatro amazonas _<session.Session object at 0x71e9fd19b0e0>.py',
#  session=s, path_excel='/home/fernando/Área de trabalho/Projeto/solucoesLLM.xlsx')
t.runTestCase()
row = t.row_table_save
print("=======TESTES===========")
print("Total de testes: ", row.total_test)
print("Total de testes que passou: ", row.passed_test)
print("Total de testes falho: ", row.failed_test)
print("Nome dos testes que passaram: ", row.passed_test_names)
print("Nome dos testes que falharam: ", row.failed_test_names)
print("Saidas obtidas e saidas esperadas: ",row.expected_and_obtained)

row.saveExcel()