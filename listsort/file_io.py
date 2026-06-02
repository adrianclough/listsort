from models import Item
from pathlib import Path


def read_txt(filepath: str | Path) -> list[Item]: 
    with open(filepath, encoding="utf-8") as l:
        unsorted_list_as_text = l.read()

    items = []

    for entry in unsorted_list_as_text.splitlines():
        if entry.strip() == "": continue
        if entry[0] == "▮":
            new_item = Item(entry[1:], True)
        else:
            new_item = Item(entry, False)
        items.append(new_item)  

    return items


def _add_tombstone(item: Item) -> str:
    if item.underlined:
        return f"▮{item.entry}"
    else:
        return item.entry
        


def write_txt(sorted_top: list[Item],rest: list[Item], filepath: str):
    """Write sorted list in expected format"""

    sorted_list = [_add_tombstone(item) for item in sorted_top] + [""] + [_add_tombstone(item) for item in rest]

    sorted_list_as_text = "\n".join(sorted_list)   

    with open(filepath, "w", encoding="utf-8") as l:
        l.write(sorted_list_as_text)
