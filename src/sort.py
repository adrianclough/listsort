from math import floor
from models import Item, SortMode
from interaction import compare

def top_sort(arr: list[Item]):
    if len(arr) < 2: 
        return arr
    
    top_top = []
    top_bottom = []
    bottom_top = []
    bottom_bottom = []

    pivot_index = floor(len(arr)/2)

    for entry in arr[:pivot_index]:
        if compare(entry, arr[pivot_index], 0, SortMode.TOP):
            top_bottom.append(entry)
        else:
            bottom_bottom.append(entry)

    for entry in arr[pivot_index + 1:]:
        if compare(entry, arr[pivot_index], 1, SortMode.TOP):
            top_top.append(entry)
        else:
            bottom_top.append(entry)

    return top_sort(bottom_bottom + bottom_top) + [arr[pivot_index]] + top_sort(top_bottom + top_top)
