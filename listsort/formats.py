from listsort.models import Item

def parse_txt(unsorted_list_as_text: str) -> list[Item]:
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
    

def serialize_txt(sorted_top: list[Item],rest: list[Item]):
    sorted_list = [_add_tombstone(item) for item in sorted_top] + [""] + [_add_tombstone(item) for item in rest]

    return "\n".join(sorted_list)   


parsers_serializers = {
    "txt": (parse_txt, serialize_txt)
}