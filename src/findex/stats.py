import time
import tracemalloc
from collections import Counter

from findex.document import iter_documents
from findex.tokenizer import tokenize
from findex.greedy import run_greedy_stats  # Імпортуємо з нашого нового модуля


def run_streaming_stats(corpus_dir: str):
    """Потоковий підхід (Streaming з генераторами)"""
    print("--- ЗАПУСК ПОТОКОВОГО ПІДХОДУ (STREAMING) ---")
    tracemalloc.start()
    start_time = time.time()

    doc_count = 0
    total_tokens = 0
    vocab = Counter()

    for _, text in iter_documents(corpus_dir):
        doc_count += 1
        for token in tokenize(text):
            vocab[token] += 1
            total_tokens += 1

    end_time = time.time()
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Документів: {doc_count}")
    print(f"Усього токенів: {total_tokens}")
    print(f"Розмір словника (унікальних): {len(vocab)}")
    print(f"Топ-5 термів: {vocab.most_common(5)}")
    print(f"Час виконання: {end_time - start_time:.2f} сек")
    print(f"Пікова пам'ять: {peak / 1024 / 1024:.2f} MB\n")


if __name__ == "__main__":
    # Переконайтеся, що вказуєте папку, в якій є файли (corpus або corpus_split)
    CORPUS_DIR = "corpus"

    run_streaming_stats(CORPUS_DIR)
    run_greedy_stats(CORPUS_DIR)