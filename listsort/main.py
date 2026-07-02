import argparse
from pathlib import Path
import sys
from listsort.file_io import read, write
from listsort.formats import parsers_serializers
from listsort.interaction import report_duplicates
from listsort.sort import sort, dedupe
from rich.live import Live
from rich.panel import Panel
import time


def main(unsorted_list_as_text: str, file_extension: str) -> str: 
    """Orchestrate application of sort to todo list"""

    if not file_extension in parsers_serializers:
        print("File extension not supported.")
        return

    parse, serialize = parsers_serializers[file_extension]

    unsorted_list = parse(unsorted_list_as_text)

    if len(unsorted_list) == 0:
        print("Congratulations, your todo list ist empty!")
        return
    
    unsorted_list, duplicates = dedupe(unsorted_list)

    report_duplicates(duplicates)

    # TODO initialise `log`

    with Live(refresh_per_second=10) as live:
        sorted_top, rest = sort(unsorted_list, live)
        live.update(Panel("[green]Done![/green]")) # TODO change hew of green
        time.sleep(1)

    return serialize(sorted_top, rest)



def main_cli() -> None:
    """Handle input from cli and pass to main()"""
    if not sys.stdin.isatty():  # temporary copy paste functionality
        unsorted_list_as_text = sys.stdin.read()
        pipe_out = sys.stdout
        sys.stdin = open('/dev/tty')
        sys.stdout = open('/dev/tty', 'w')
        sorted_list_as_text = main(unsorted_list_as_text, 'txt')
        if sorted_list_as_text: 
            pipe_out.write(sorted_list_as_text)
        return

    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("-o", "--output")
    args = parser.parse_args()

    if not args.output:
        p = Path(args.input)
        args.output = p.parent / (p.stem + '_sorted' + '.txt')

    unsorted_list_as_text = read(args.input)

    file_extension = Path(args.input).suffix[1:]

    sorted_list_as_text = main(unsorted_list_as_text, file_extension)

    if sorted_list_as_text:
        write(args.output, sorted_list_as_text)

if __name__ == "__main__":
    main_cli()
