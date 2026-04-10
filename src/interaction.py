import readchar
import rich
from rich.panel import Panel
from models import Item, SortMode

item_colour = "#A5D6FF"
pivot_colour = {SortMode.ROUGH: "#FF7B72", SortMode.TOP: "#D2A8FF"}


def display(item: Item, colour: str) -> str:
    return f"[{colour}]{item.entry}[/]"

def compare(item: Item, pivot: Item, above: bool, mode: SortMode) -> bool:
    """Ask user to compare pair of displayed items"""

    colour = pivot_colour[mode]

    if above:
        rich.print(Panel(display(item, item_colour) + "\n\n" + display(pivot, colour), border_style="dim"))
    else:
        rich.print(Panel(display(pivot, colour) + "\n\n" + display(item, item_colour), border_style="dim"))

    while True:
        key = readchar.readkey()
        if key == readchar.key.UP:
            return True
        elif key == readchar.key.DOWN:
            return False
        else:
            rich.print("Invalid key. Press UP or DOWN.")


if __name__ == "__main__":
    a = Item("Buy groceries", False)
    b = Item("Call dentist", False)
    result = compare(a, b, above=True, mode=SortMode.ROUGH)
    print(result)