from utils import keys
from keys import GEMINI_KEY
from keys import GPT_KEY
from keys import MISTRAL_KEY

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_mistralai import ChatMistralAI 
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

import re

class LLM:
    def __init__(self, nameLlm, exercise, temperature):
        self.name = nameLlm
        self.exercise = exercise # Quardar a classe exercicio
        self.temperature = temperature

    def generate(self):
        if self.name == "Gemini":
            modelLLM = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=GEMINI_KEY, temperature=self.temperature)
        elif self.name == "GPT4o-mini":
            modelLLM = ChatOpenAI(model="gpt-4o-mini", openai_api_key=GPT_KEY, temperature=self.temperature)
        elif self.name == "HuggingChat":
            modelLLM = ChatMistralAI(model="open-codestral-mamba", mistral_api_key=MISTRAL_KEY, temperature=self.temperature)
            #modelLLM = ChatMistralAI(model="codestral-latest", mistral_api_key=MISTRAL_KEY)
        elif self.name == "GPT4o":
            modelLLM = ChatOpenAI(model="gpt-4o", openai_api_key=GPT_KEY, temperature=self.temperature)

        prompt = ChatPromptTemplate.from_template(
            "Sou um estudante iniciante em programação em python." \
            "Gere um código para solução do exercício abaixo." \
            "Exercício: {exercise}"
        )
        #print(message)    
        chain = prompt | modelLLM
        response = chain.invoke({"exercise": self.exercise.content})
        # Tratamento da saida gerada pela API das LLM 
        # Utilizando expressões regulares e jutando em um unico formato de string
        code_result = re.findall(r"```(?:python)?\n(.*?)```", response.content, flags=re.DOTALL)
        self.content = "\n".join(code_result)
        
    def getContent(self):
        return self.content
    
    def getName(self):
        return self.name
    
    def getExercise(self):
        return self.exercise
    
    def getTemperature(self):
        return self.temperature
    
     