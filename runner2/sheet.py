# import openpyxl
import pyexcel
import glob
import sys
from datetime import datetime
import git


class Sheet:
    def __init__(self, exercise, llm, path, dict_test_results):
        self.exercise = exercise #Pegar qual o nome e linguem usada
        self.llm = llm# Nome da LLM e temperatura
        self.path = path# Caminho da planilha salva
        self.total_test = dict_test_results['total']
        self.passed_test = dict_test_results['passed']
        self.failed_test = dict_test_results['failed']
        self.passed_test_names = dict_test_results['passed_names']
        self.failed_test_names = dict_test_results['failed_names']
        self.expected_and_obtained = dict_test_results['esperado_e_obtido']

    def saveExcel(self):
        repo = git.Repo(search_parent_directories=True)
        sha = repo.head.object.hexsha
        
        passed_tests_str = "\n".join(self.passed_test_names)
        failed_tests_str = "\n".join(self.failed_test_names)
        expected_obtained_str = "\n".join(map(str, self.expected_and_obtained))

        book = pyexcel.get_book(file_name=self.path)
        sheet = book[0]
        # Abrir a planilha
        sheet.row += [
            self.exercise.getName(),
            self.exercise.getId(),
            self.exercise.getLanguage(),
            self.llm.getName(),
            self.llm.getTemperature(),
            datetime.now(),
            self.total_test, 
            self.passed_test,
            self.failed_test,
            sha,
            passed_tests_str,
            failed_tests_str,
            expected_obtained_str
            ]
        book.save_as(self.path)