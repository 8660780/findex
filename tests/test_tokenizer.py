# tests/test_tokenizer.py
from findex.tokenizer import tokenize

def test_tokenize_basic():
    text = "Привіт, світе! Це тест №1."
    assert list(tokenize(text)) == ["привіт", "світе", "це", "тест", "no1"]

def test_tokenize_apostrophe_and_hyphen():
    text = "М'ясо коштує 150.50 грн. It's a state-of-the-art model!"
    expected = ["м'ясо", "коштує", "150.50", "грн", "it's", "a", "state-of-the-art", "model"]
    assert list(tokenize(text)) == expected

def test_unicode_normalization():
    # 'café' з літерою 'e' та комбінованим акцентом
    text1 = "cafe\u0301"
    text2 = "café"
    assert list(tokenize(text1)) == list(tokenize(text2))