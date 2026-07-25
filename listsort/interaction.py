import readchar
import rich
from rich.console import Group
from rich.panel import Panel
from rich.live import Live
from listsort.models import Item, Record, SortMode

item_colour = "#A5D6FF"
pivot_colour = {SortMode.ROUGH: "#FF7B72", SortMode.TOP: "#D2A8FF"}
# displayed_choices = 5


def displayed_item(item: Item, colour: str) -> str:
    return f"[{colour}]{item.entry}[/]"


def choices_panels(log: list[Record], n: int = 5) -> list[Panel]:
    choices = []
    for record in log[-n:]:                 # TODO refactor: code is cluttered, and recomputing all 5 panels every time is inefficient. 
        colour = pivot_colour[record.mode]
        if record.above:
            if record.key == readchar.key.UP:
                choices.append(Panel(displayed_item(record.item, item_colour) + " ✅\n\n" + displayed_item(record.pivot, colour) + "\n\n", border_style="dim"))
            elif record.key == readchar.key.DOWN:
                choices.append(Panel("\n\n" + displayed_item(record.pivot, colour) + "\n\n" + displayed_item(record.item, item_colour) + " ❌", border_style="dim"))
            elif record.key == readchar.key.BACKSPACE:
                choices.append(Panel(f"[strike]{displayed_item(record.item, item_colour)}[/strike]" + "\n\n" + displayed_item(record.pivot, colour) + "\n\n", border_style="dim"))
        else:
            if record.key == readchar.key.UP:
                choices.append(Panel(displayed_item(record.item, item_colour) + " ❌\n\n" + displayed_item(record.pivot, colour) + "\n\n", border_style="dim"))
            elif record.key == readchar.key.DOWN:
                choices.append(Panel("\n\n" + displayed_item(record.pivot, colour) + "\n\n" + displayed_item(record.item, item_colour) + " ✅", border_style="dim"))
            elif record.key == readchar.key.BACKSPACE:
                choices.append(Panel( "\n\n" + displayed_item(record.pivot, colour) + "\n\n" + f"[strike]{displayed_item(record.item, item_colour)}[/strike]", border_style="dim"))
            # elif record.key == readchar.key.BACKSPACE:
            #     text = "\n\n" + displayed_item(record.pivot, colour) + "\n\n" + f"[strike]{displayed_item(record.item, item_colour)}[/strike]"
            #     with open("/tmp/listsort_debug.log", "a") as f:
            #         f.write(repr(text) + "\n")
            #         choices.append(Panel(text, border_style="dim"))

    return choices

def comparison_panel(item: Item, pivot: Item, above: bool, mode: SortMode) -> Panel:

    colour = pivot_colour[mode]

    if above:
        return Panel(displayed_item(item, item_colour) + "\n\n" + displayed_item(pivot, colour) + "\n\n", border_style="dim")
    else:
        return Panel("\n\n" + displayed_item(pivot, colour) + "\n\n" + displayed_item(item, item_colour), border_style="dim")


def display_output(comparison_panel_evaluated: Panel, choices_panels_evaluated: list[Panel], live: Live):
    merged_panels = choices_panels_evaluated + [comparison_panel_evaluated]
    group_panels = Group(*merged_panels)
    live.update(group_panels)


def compare(item: Item, pivot: Item, above: bool, mode: SortMode, live: Live, log: list[Record]) -> tuple[bool | None, Record]:
    """Ask user to compare pair of displayed items"""

    comparison_panel_evaluated = comparison_panel(item, pivot, above, mode)

    choices_panels_evaluated = choices_panels(log)

    display_output(comparison_panel_evaluated, choices_panels_evaluated, live)

    

    while True:
        key = readchar.readkey()
        if key == readchar.key.UP:
            return True, Record(key, mode, above, pivot, item)
        elif key == readchar.key.DOWN:
            return False, Record(key, mode, above, pivot, item)
        elif key == readchar.key.BACKSPACE:
            return None, Record(key, mode, above, pivot, item)
        else:
            rich.print("Invalid key. Press UP, DOWN, or delete.")


def report_duplicates(duplicates: set[str]):
    if duplicates: 
        rich.print(f"[#e5ba7d]Found {len(duplicates)} duplicate{'s' if len(duplicates) > 1 else ''}:[/#e5ba7d] \n{'\n'.join(sorted(duplicates))}")


#For testing `compare`
if __name__ == "__main__":
    a = Item("Buy groceries", False)
    b = Item("Call dentist", False)
    result = compare(a, b, above=True, mode=SortMode.ROUGH)
    print(result)