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
t.