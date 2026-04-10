import readchar
from main import Item, read_txt, write_txt

def open_underline(underlined: bool):
    if underlined:
        return "\033[4m"
    else:
        return ""
    
def close_underline(underlined: bool):
    if underlined:
        return "\033[0m"
    else:
        return ""

def bubble_sort(test_list: list[Item]):
    switch = True
    while switch:
        switch = False
        for i in range(len(test_list) - 1):
            print(open_underline(test_list[i].underlined) + test_list[i].entry + close_underline(test_list[i].underlined) + " < " + open_underline(test_list[i+1].underlined) + test_list[i+1].entry + close_underline(test_list[i+1].underlined))
            while True:
                key = readchar.readkey()
                if key == readchar.key.DOWN:
                     switch = True
                     test_list[i], test_list[i+1] = test_list[i+1], test_list[i]
                     break
                elif key == readchar.key.UP:
                    break
                else:
                    print("Invalid key. Press UP or DOWN.")
            print([item.entry for item in test_list])          
    return test_list


if __name__ == "__main__":

    items = read_txt("data/test.txt")

    bubble_sort(items)

    write_txt(items, "data/test_output.txt")