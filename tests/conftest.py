import pytest
from nltk import download as nltk_download


# This fixture insures that nltk is downloaded before running tests, avoiding setup errors
@pytest.fixture()
def setup_nltk_stopwords():
    nltk_download("punkt")
    nltk_download("stopwords")
