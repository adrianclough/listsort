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

    for entry in arr[:pivot_index]:
        if compare(entry, arr[pivot_index], False, SortMode.TOP):
            top_bottom.append(entry)
        else:
            bottom_bottom.append(entry)

    for entry in arr[pivot_index + 1:]:
        if compare(entry, arr[pivot_index], True, SortMode.TOP):
            top_top.append(entry)
        else:
            bottom_top.append(entry)

    return top_sort(bottom_bottom + bottom_top) + [arr[pivot_index]] + top_sort(top_bottom + top_top)

def sort(top: list[Item], n: int = 10) -> tuple[list[Item], list[Item]]:
    """Sort todo list according to Adrian's algorithm."""

    if len(top) < n:
        return top_sort(top), []
    
    else:
        top_top = []
        top_bottom = []
        bottom_top = []
        bottom_bottom = []

        pivot_index = len(top)//2

        for entry in top[:pivot_index]:
            if compare(entry, top[pivot_index], False, SortMode.TOP):
                top_bottom.append(entry)
            else:
                bottom_bottom.append(entry)

        for entry in top[pivot_index + 1:]:
            if compare(entry, top[pivot_index], True, SortMode.TOP):
                top_top.append(entry)
            else:
                bottom_top.append(entry)
        
        recursed_top, recursed_bottom = sort(top_top + top_bottom, n)

        return recursed_top, recursed_bottom + [top[pivot_index]] + bottom_top + bottom_bottom