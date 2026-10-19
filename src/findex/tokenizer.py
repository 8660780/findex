# src/findex/tokenizer.py
import re
import unicodedata
import typing as t

# Регулярний вираз:
# \w+                   - одна або більше літер/цифр (Unicode)
# (?:['’-]\w+)*        - необов'язкові групи з дефісом або апострофом всередині слова (напр. don't, state-of-the-art)
# (?:\.\d+)?            - необов'язкова дробова частина для чисел (напр. 3.14)
TOKEN_PATTERN = re.compile(r"\w+(?:['’-]\w+)*(?:\.\d+)?", re.UNICODE)


def tokenize(text: str) -> t.Generator[str, None, None]:
    """
    Потоковий токенізатор. Нормалізує текст та розбиває на токени.
    Правила:
    - Зберігає апострофи (п'ять, don't)
    - Зберігає дефіси (хто-зна, state-of-the-art)
    - Зберігає цілі та дробові числа (123, 3.14)
    """
    # 1. Нормалізація Unicode
    normalized_text = unicodedata.normalize('NFKC', text)
    # 2. Нижній регістр
    lowered_text = normalized_text.lower()

    # 3. Пошук токенів (yield як потокова віддача)
    for match in TOKEN_PATTERN.finditer(lowered_text):
        yield match.group()