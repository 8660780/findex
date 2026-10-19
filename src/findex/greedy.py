import time
import tracemalloc
from collections import Counter
from pathlib import Path

from findex.tokenizer import tokenize


def run_greedy_stats(corpus_dir: str):
    """
    Жадібний підхід (Greedy):
    Завантажує весь корпус у списки в оперативну пам'ять одразу.
    """
    print("--- ЗАПУСК ЖАДІБНОГО ПІДХОДУ (GREEDY) ---")
    tracemalloc.start()
    start_time = time.time()

    # 1. Завантажуємо ВСІ тексти файлів у один список у пам'яті
    documents = []
    for filepath in Path(corpus_dir).rglob("*.txt"):
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            documents.append(f.read())

    # 2. Токенізуємо ВСЕ в один гігантський список токенів
    all_tokens = []
    for text in documents:
        all_tokens.extend(list(tokenize(text)))

    doc_count = len(documents)
    total_tokens = len(all_tokens)
    vocab = Counter(all_tokens)

    end_time = time.time()
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Документів: {doc_count}")
    print(f"Усього токенів: {total_tokens}")
    print(f"Розмір словника: {len(vocab)}")
    print(f"Час виконання: {end_time - start_time:.2f} сек")
    print(f"Пікова пам'ять: {peak / 1024 / 1024:.2f} MB\n")