import argparse
from models import Item
from file_io import read_txt, write_txt
from pathlib import Path
from sort import sort


def main(filepath: str | Path, write_path: str | Path):
    """Orchstrate applicatoin of sort to todo list"""

    unsorted_list = read_txt(filepath)

    if len(unsorted_list) == 0:
        print("Congratulations, your todo list ist empty!")
        return

    sorted_top, rest = sort(unsorted_list)

    write_txt(sorted_top, rest, write_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("-o", "--output")
    args = parser.parse_args()

    if not args.output:
        p = Path(args.input)
        args.output = p.parent / (p.stem + '_sorted' + '.txt')

    main(args.input, args.output)

