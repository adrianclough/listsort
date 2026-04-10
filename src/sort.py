from math import floor
from items import Item
from interaction import compare

def top_sort(arr: list[Item]):
    if len(arr) < 2: 
        return arr
    
    top_top = []
    top_bottom = []
    bottom_top = []
    bottom_bottom = []

    pivot = floor(len(arr)/2)

    for entry in arr[:pivot]:

