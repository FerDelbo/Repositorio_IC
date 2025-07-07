import session
import importlib.util
import glob
import os

class TestExecute:
    def __init__(self):
        pass
    
    def module_from_file(module_name, file_path):
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def runTestCase(self,):
    #fazer a busca com o nome do exercico e usar o import module 
        path = glob.glob(f'{self.input_dirctory}/**/{self.nameproblem}*/**/test.py', recursive=True)
        # if(len(path) == 0):
        #     self.createtest()
        #     path = glob.glob(f'{self.input_dirctory}/**/{self.nameproblem}*/**/test.py', recursive=True)
        test = self.module_from_file("test", path[0])
        test_results = test.runTest(self.nameLLM, self.partPrompt[0], self.language, self.output_dirctory, 
                     self.nameproblem, self.k)
        del(test)
        return test_results
