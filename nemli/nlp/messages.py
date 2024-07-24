from functools import lru_cache
from typing import Optional

from nltk import word_tokenize
from nltk.corpus import stopwords


@lru_cache(maxsize=1024)
def clean_up_stopwords(message: Optional[str] = None) -> str:
    if not (message and isinstance(message, str)):
        return ""

    stop_words = set(stopwords.words("portuguese")) - set(["que", "não", "eu", "ele", "ela"])
    tokens = word_tokenize(message)
    return " ".join(token for token in tokens if token.lower() not in stop_words).strip()
