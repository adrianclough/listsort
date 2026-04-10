import readchar

def is_sorted(test_list: list[int]):
    for a, b in zip(test_list, test_list[1:]):
        if a > b:
            return False

    return True


def bubble_sort(test_list: list[int]):
    while not is_sorted(test_list):
        for i in range(len(test_list) - 1):
            print(test_list[i], test_list[i+1])
            while True:
                key = readchar.readkey()
                if key == readchar.key.DOWN:
                     test_list[i], test_list[i+1] = test_list[i+1], test_list[i]
                     break
                elif key == readchar.key.UP:
                    break
                else:
                    print("Invalid key. Press UP or DOWN.")
            print(test_list)          
    return test_list


if __name__ == "__main__":
    print(bubble_sort([3, 1, 4, 1, 5, 9, 2, 6]))