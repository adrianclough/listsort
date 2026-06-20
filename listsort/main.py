import argparse
from pathlib import Path
import sys
from listsort.file_io import read, write
from listsort.formats import parsers_serializers
from listsort.interaction import report_duplicates
from listsort.sort import sort, dedupe


def main(filepath: str | Path, write_path: str | Path):
    """Orchestrate application of sort to todo list"""

    file_format = Path(filepath).suffix[1:]

    if not file_format in parsers_serializers:
        print("File extension not supported.")
        return

    unsorted_list_as_text = read(filepath)

    parse, serialize = parsers_serializers[file_format]

    unsorted_list = parse(unsorted_list_as_text)

    if len(unsorted_list) == 0:
        print("Congratulations, your todo list ist empty!")
        return
    
    unsorted_list, duplicates = dedupe(unsorted_list)

    report_duplicates(duplicates)

    sorted_top, rest = sort(unsorted_list)

    sorted_list_as_text = serialize(sorted_top, rest)

    write(write_path, sorted_list_as_text)


def main_cli() -> None:
    if not sys.stdin.isatty():  # temporary copy paste functionality
        pass

    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("-o", "--output")
    args = parser.parse_args()

    if not args.output:
        p = Path(args.input)
        args.output = p.parent / (p.stem + '_sorted' + '.txt')

    main(args.input, args.output)


if __name__ == "__main__":
    main_cli()


#filepath = "data/test_numbers.txt" for testing