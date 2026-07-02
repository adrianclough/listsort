from pathlib import Path


def read(filepath: str | Path) -> str: 
    with open(filepath, encoding="utf-8") as l:
        return l.read()


def write(filepath: str | Path, sorted_list_as_text: str):
    with open(filepath, "w", encoding="utf-8") as l:
        l.write(sorted_list_as_text)