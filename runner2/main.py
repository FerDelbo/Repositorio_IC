from session import SessionManager

s = SessionManager('/home/fernando/Área de trabalho/Projeto/enunciadosCodeBench.xlsx')
path = s.create(base_directory='/home/fernando/Área de trabalho/Projeto/Repositorio_IC/IC',
               output_directory='/home/fernando/Área de trabalho/Projeto/solucaos')
print(s)
# Teste se a session esta sendo ocorrida
print(path)
print(s.session.session_id)

# Teste se a classe exercicio esta sendo criada
exe = s.listExercise('1287', 'pt')
print(exe.name)
print(exe)

# Teste configurar LLM
llm = s.settingLLM('GPT4o', 0.7)
llm.generate()
print(llm.getContent())

# Teste salvar aquivo
s.saveContent()