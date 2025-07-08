import pytest
from unittest.mock import patch, MagicMock
from generatorCode import LLM

# Classe mockada para simular um exercício
class FakeExercise:
    def __init__(self, content):
        self.content = content

@pytest.mark.parametrize("llm_name,model_class", [
    ("Gemini", "generatorCode.ChatGoogleGenerativeAI"),
    ("GPT4o-mini", "generatorCode.ChatOpenAI"),
    ("GPT4o", "generatorCode.ChatOpenAI"),
    ("HuggingChat", "generatorCode.ChatMistralAI"),
])
@patch("generatorCode.ChatPromptTemplate")
def test_llm_generate(mock_prompt_template, llm_name, model_class):
    fake_exercise = FakeExercise("Implemente uma função soma(a, b)")
    fake_chain = MagicMock()
    fake_response = MagicMock()
    fake_response.content = "```python\ndef soma(a, b):\n    return a + b\n```"
    fake_chain.invoke.return_value = fake_response

    mock_prompt = MagicMock()
    mock_prompt.__or__.return_value = fake_chain
    mock_prompt_template.from_template.return_value = mock_prompt

    with patch(model_class) as mock_model:
        instance = LLM(nameLlm=llm_name, exercise=fake_exercise, temperature=0.3)
        instance.generate()

        # Verificações
        assert "return a + b" in instance.getContent()
        assert instance.getExercise() == fake_exercise
        assert instance.getName() == llm_name
        assert instance.getTemperature() == 0.3

        # Garantir que o model foi criado com a temperatura
        mock_model.assert_called()
        fake_chain.invoke.assert_called_once()
