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
        if compare(entry, arr[pivot_index], False, SortMode.TOP):
            top_top.append(entry)
        else:
            bottom_top.append(entry)

    for entry in reversed(arr[:pivot_index]):
        if compare(entry, arr[pivot_index], True, SortMode.TOP):
            top_bottom.append(entry)
        else:
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
            if compare(entry, arr[pivot_index], False, SortMode.ROUGH):
                top_top.append(entry)
            else:
                bottom_top.append(entry)

        for entry in reversed(arr[:pivot_index]):
            if compare(entry, arr[pivot_index], True, SortMode.ROUGH):
                top_bottom.append(entry)
            else:
                bottom_bottom.append(entry)

        top_top = list(reversed(top_top))
        top_bottom = list(reversed(top_bottom))
        bottom_top = list(reversed(bottom_top))
        bottom_bottom = list(reversed(bottom_bottom))
        
        recursed_top, recursed_bottom = sort(top_top + top_bottom, n)

        return recursed_top, recursed_bottom + [arr[pivot_index]] + bottom_top + bottom_bottom