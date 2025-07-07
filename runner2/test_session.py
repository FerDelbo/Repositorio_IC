import pytest
import os
from unittest.mock import patch, MagicMock
from session import Session, SessionManager, Exercise

# -------------------------
# Testes para a classe Session
# -------------------------

def test_session_creation(tmp_path):
    input_dir = tmp_path / "input"
    output_dir = tmp_path / "output"
    input_dir.mkdir()
    output_dir.mkdir()

    session = Session(outDirectory=str(output_dir), inputDirectory=str(input_dir))
    new_path = session.createSession()

    assert os.path.exists(new_path)
    assert session.getInputDirectory() == str(input_dir)
    assert session.getOutputDirectory() == str(output_dir)

def test_set_session():
    session = Session(outDirectory="out", inputDirectory="in")
    session.setSession(7, "Julho")
    assert session.session == "7doJulho"

# -------------------------
# Testes para a classe Exercise
# -------------------------

def test_exercise_getters():
    ex = Exercise(
        id="001",
        name="Soma",
        language="Python",
        content="Faça a soma de dois números.",
        test_case="1 2 -> 3",
        solution="def soma(a, b): return a + b"
    )

    assert ex.getId() == "001"
    assert ex.getName() == "Soma"
    assert ex.getLanguage() == "Python"
    assert ex.getContent() == "Faça a soma de dois números."
    assert ex.getTestCase() == "1 2 -> 3"
    assert ex.getSolution() == "def soma(a, b): return a + b"

# -------------------------
# Testes para SessionManager
# -------------------------

@patch("session.pyexcel.get_records")
def test_list_exercise_found(mock_get_records):
    mock_get_records.return_value = [
        {
            'Problema ID': '001',
            'Nome do exercício': 'Soma',
            'Enunciado revisado': 'Some dois números',
            'Casos de teste': '1 2 -> 3',
            'Solução de referência': 'def soma(a, b): return a + b'
        }
    ]

    sm = SessionManager(file="fake.xlsx")
    exercise = sm.listExercise(problem_id='001', language='Python')

    assert isinstance(exercise, Exercise)
    assert exercise.getId() == '001'
    assert exercise.getLanguage() == 'Python'

@patch("session.pyexcel.get_records")
def test_list_exercise_not_found(mock_get_records):
    mock_get_records.return_value = []

    sm = SessionManager(file="fake.xlsx")
    exercise = sm.listExercise(problem_id='002', language='Python')

    assert exercise is None

@patch("session.LLM")
def test_setting_llm(mock_llm_class):
    mock_llm_instance = MagicMock()
    mock_llm_class.return_value = mock_llm_instance

    sm = SessionManager(file="fake.xlsx")
    sm.exercise = Exercise("001", "Soma", "Python", "desc", "test", "sol")

    llm = sm.settingLLM(name_llm="gpt", temperature=0.5)

    assert llm == mock_llm_instance
    mock_llm_class.assert_called_with("gpt", sm.exercise, 0.5)

@patch("session.LLM")
def test_save_content(mock_llm_class, tmp_path):
    mock_llm_instance = MagicMock()
    mock_llm_instance.getContent.return_value = "codigo gerado"
    mock_llm_instance.getName.return_value = "gpt"
    mock_llm_class.return_value = mock_llm_instance

    sm = SessionManager(file="fake.xlsx")
    sm.session = "7doJulho"
    sm.exercise = Exercise("001", "Soma", "Python", "desc", "test", "sol")
    sm.llm = mock_llm_instance

    out_dir = tmp_path
    sm.outDirectory = str(out_dir)

    file_path = sm.saveContent()

    assert os.path.exists(file_path)
    with open(file_path) as f:
        content = f.read()
        assert content == "codigo gerado"
