from math import floor


def quick_sort(test_list: list[int]):
    if len(test_list) < 2:
        return test_list
    
    top_top = []
    top_bottom = []
    bottom_top = []
    bottom_bottom = []

    for entry in test_list[floor(len(test_list)/2) + 1:]:
        if entry > test_list[floor(len(test_list)/2)]:
            top_top.append(entry)
        else:
            bottom_top.append(entry)

    for entry in test_list[:floor(len(test_list)/2)]:
        if entry > test_list[floor(len(test_list)/2)]:
            top_bottom.append(entry)
        else:
            bottom_bottom.append(entry)

    return quick_sort(bottom_bottom + bottom_top) + [test_list[floor(len(test_list)/2)]] + quick_sort(top_bottom + top_top)


if __name__ == "__main__":
    print(quick_sort([3, 1, 4, 1, 5, 9, 2, 6]))