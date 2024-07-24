import pytest

from nemli.nlp.messages import clean_up_stopwords

import nltk


def setup_nltk():
    try:
        nltk.data.find("corpora/stopwords")
    except LookupError:
        nltk.download("stopwords")
    try:
        nltk.data.find("tokenizers/punkt")
    except LookupError:
        nltk.download("punkt")


setup_nltk()


@pytest.mark.parametrize(
    "message,expected",
    [
        (
            "Voce sabe o que eh um pequeno texto",
            "Voce sabe que eh pequeno texto",
        ),
        (
            "O que não provoca minha morte faz com que eu fique mais forte.",
            "que não provoca morte faz que eu fique forte .",
        ),
        (
            "A vantagem de ter péssima memória é divertir-se muitas vezes com as mesmas coisas boas como se fosse a primeira vez.",
            "vantagem ter péssima memória divertir-se muitas vezes mesmas coisas boas primeira vez .",
        ),
    ],
)
def test_clean_up_stopwords(message: str, expected: str):
    assert clean_up_stopwords(message) == expected
