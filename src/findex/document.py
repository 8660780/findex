from pathlib import Path
import typing as t


def iter_documents(corpus_dir: str | Path) -> t.Generator[tuple[str, str], None, None]:
    """
    Генератор, що читає текстові файли з директорії по одному.
    Повертає кортеж (назва_файлу, текст).
    """
    corpus_path = Path(corpus_dir)

    if not corpus_path.exists() or not corpus_path.is_dir():
        raise FileNotFoundError(f"Директорія {corpus_dir} не знайдена.")

    for filepath in corpus_path.rglob("*.txt"):
        # Відкриваємо файл, читаємо, віддаємо через yield і одразу звільняємо пам'ять
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            yield filepath.name, f.read()