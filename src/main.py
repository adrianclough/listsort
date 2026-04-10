from items import Item
from io import read_txt, write_txt



if __name__ == "__main__":

    items = read_txt("data/test.txt")

    for item in items:
        print(f"[{item.entry}, {item.underlined}]")

    write_txt(items, "data/test_output.txt")