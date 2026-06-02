from models import Item, SortMode
from interaction import compare

def top_sort(arr: list[Item]) -> list[Item]:
    """Sort top N-1 entries of list exhaustively."""
    if len(arr) < 2: 
        return arr
    
    top_top = []
    top_bottom = []
    bottom_top = []
    bottom_bottom = []

    pivot_index = len(arr)//2

    for entry in reversed(arr[pivot_index + 1:]):
        result = compare(entry, arr[pivot_index], False, SortMode.TOP)
        if result is True:
            top_top.append(entry)
        elif result is False:
            bottom_top.append(entry)

    for entry in reversed(arr[:pivot_index]):
        result = compare(entry, arr[pivot_index], True, SortMode.TOP)
        if result is True:
            top_bottom.append(entry)
        elif result is False:
            bottom_bottom.append(entry)

    top_top = list(reversed(top_top))
    top_bottom = list(reversed(top_bottom))
    bottom_top = list(reversed(bottom_top))
    bottom_bottom = list(reversed(bottom_bottom))


    return top_sort(top_top + top_bottom) + [arr[pivot_index]] + top_sort(bottom_top + bottom_bottom)

def sort(arr: list[Item], n: int = 10) -> tuple[list[Item], list[Item]]:
    """Sort todo list according to Adrian's algorithm."""

    if len(arr) < n:
        return top_sort(arr), []
    
    else:
        top_top = []
        top_bottom = []
        bottom_top = []
        bottom_bottom = []

        pivot_index = len(arr)//2

        for entry in reversed(arr[pivot_index + 1:]):
            result = compare(entry, arr[pivot_index], False, SortMode.ROUGH)
            if result is True:
                top_top.append(entry)
            elif result is False:
                bottom_top.append(entry)

        for entry in reversed(arr[:pivot_index]):
            result = compare(entry, arr[pivot_index], True, SortMode.ROUGH) 
            if result is True:
                top_bottom.append(entry)
            elif result is False:
                bottom_bottom.append(entry)

        top_top = list(reversed(top_top))
        top_bottom = list(reversed(top_bottom))
        bottom_top = list(reversed(bottom_top))
        bottom_bottom = list(reversed(bottom_bottom))
        
        recursed_top, recursed_bottom = sort(top_top + top_bottom, n)

        return recursed_top, recursed_bottom + [arr[pivot_index]] + bottom_top + bottom_bottom
    


def dedupe(items: list[Item]) ->  tuple[list[Item], set[str]]:
    dedupe_items = {}
    duplicates = set()
    for item in items:
        entry = item.entry.strip()
        if entry not in dedupe_items:
            dedupe_items[entry] = item
        else: 
            duplicates.add(entry)
            if item.underlined: 
                dedupe_items[entry].underlined = True
            
    return list(dedupe_items.values()), duplicates
