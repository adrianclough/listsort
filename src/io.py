from models import Item


def read_txt(filepath: str) -> list[Item]: 
    with open(filepath, encoding="utf-8") as l:
        unsorted_list_as_text = l.read()

    items = []

    for entry in unsorted_list_as_text.splitlines():
        if entry == "": continue
        if entry[0] == "▮":
            new_item = Item(entry[1:], True)
        else:
            new_item = Item(entry, False)
        items.append(new_item)  

    return items



def write_txt(items: list[Item], filepath: str):
    lines = []
    for item in items:
        if item.underlined:
            lines.append(f"▮{item.entry}")
        else:
            lines.append(item.entry)
    sorted_list_as_text = "\n".join(lines)

    with open(filepath, "w", encoding="utf-8") as l:
        l.write(sorted_list_as_text)
