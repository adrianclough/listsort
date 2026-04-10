import readchar
from math import floor


def quick_sort(test_list: list[int]):
    if len(test_list) < 2:
        return test_list
    
    top_top = []
    top_bottom = []
    bottom_top = []
    bottom_bottom = []

    pivot = floor(len(test_list)/2)

    for entry in test_list[pivot + 1:]:
        print(f"{entry}" + " t " + f"{test_list[pivot]}")
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
                
   
    for entry in test_list[:pivot]:
        print(f"{entry}" + " b " + f"{test_list[pivot]}")
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
                
   

    return quick_sort(bottom_bottom + bottom_top) + [test_list[pivot]] + quick_sort(top_bottom + top_top)


if __name__ == "__main__":
    print(quick_sort([3, 1, 4, 1, 5, 9, 2, 6]))