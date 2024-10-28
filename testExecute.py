from utils import testV # Responsavel pelos casos de teste do exercico de Veículos trafegando em alta velocidade
from utils import testM # Responsavel pelos casos de teste do exercico de Média ponderada
from utils import testD # Responsavel pelos casos de teste do exercico de Data por extenso

class testExecute:
    def __init__(self, nameLLM, partPrompt, language, session):
        self.session = session
        self.nameLLM = nameLLM
        self.partPrompt = partPrompt
        self.language = language
    
    def runTestCase(self, exercise):
        if nameExercise == "Veiculos":
            testV.runTest(self.nameLLM, self.partPrompt, self.language, self.session)
            
        elif nameExercise == "Média":
            testM.runTest(self.nameLLM, self.partPrompt, self.language, self.session)
            
        elif nameExercise == "Data":
            testD.runTest(self.nameLLM, self.partPrompt, self.language, self.session)
           
     