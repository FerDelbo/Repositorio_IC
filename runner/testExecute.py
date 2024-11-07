import importlib.util
import glob

def module_from_file(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestExecute:
    def __init__(self, nameLLM, partPrompt, language, session, outputDir, inputDir):
        self.input_dirctory = inputDir
        self.output_dirctory = outputDir
        self.nameLLM = nameLLM
        self.partPrompt = partPrompt
        self.language = language
        self.session = session
    
    def runTestCase(self, nameProblem):
    #fazer a busca com o nome do exercico e usar o import module 
        path = glob.glob(f'{self.input_dirctory}/**/{nameProblem}*/**/test.py', recursive=True)
        test = module_from_file("test", path[0])
        test.runTest(self.nameLLM, self.partPrompt[0], self.language, self.output_dirctory)
        del(test)
    