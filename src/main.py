from models import Item
from file_io import read_txt, write_txt
from sort import sort

def main(filepath: str = "data/unsorted_todo.txt", write_path: str = "data/sorted_todo.txt"):
    """Orchstrate applicatoin of sort to todo list"""

    unsorted_list = read_txt(filepath)

    if len(unsorted_list) == 0:
        print("Congratulations, your todo list ist empty!")
        return

    sorted_top, rest = sort(unsorted_list)

    write_txt(sorted_top, rest, write_path)


if __name__ == "__main__":
    main(filepath = "data/test_numbers.txt")