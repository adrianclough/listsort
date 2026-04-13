import readchar
from math import floor


def quick_sort(arr: list[int]):
    if len(arr) < 2:
        return arr
    
    top_top = []
    top_bottom = []
    bottom_top = []
    bottom_bottom = []

    pivot = floor(len(arr)/2)

    for entry in arr[pivot + 1:]:
        print(f"{entry}" + " t " + f"{arr[pivot]}")
        while True:
            key = readchar.readkey()
            if key == readchar.key.UP:
                top_top.append(entry)
                break
            elif key == readchar.key.DOWN:
                bottom_top.append(entry)
                break
            else:
                print("Invalid key. Press UP or DOWN.")
                
   
    for entry in arr[:pivot]:
        print(f"{entry}" + " b " + f"{arr[pivot]}")
        while True:
            key = readchar.readkey()
            if key == readchar.key.UP:
                top_bottom.append(entry)
                break
            elif key == readchar.key.DOWN:
                bottom_bottom.append(entry)
                break
            else:
                print("Invalid key. Press UP or DOWN.")
                
   

    return quick_sort(bottom_bottom + bottom_top) + [arr[pivot]] + quick_sort(top_bottom + top_top)


if __name__ == "__main__":
    print(quick_sort([3, 1, 4, 1, 5, 9, 2, 6]))