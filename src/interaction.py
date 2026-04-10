import readchar
import rich
from rich.panel import Panel
from items import Item

def display(item: Item, colour: str) -> str:
    return f"[{colour}]{item.entry}[/]"

def compare(item: Item, pivot: Item, above: bool, rough: bool) -> bool:
    """Ask user to compare pair of displayed items"""

    item_colour = "#A5D6FF"
    pivot_colour = ["#D2A8FF", "#FF7B72"]

    rich.print(Panel(display(item, item_colour) + "\n" + display(pivot, pivot_colour[rough])), border_style="dim")

    while True:
        key = readchar.readkey()
        if key == readchar.key.UP:
            return True
        elif key == readchar.key.DOWN:
            return False
        else:
            print("Invalid key. Press UP or DOWN.")

    

# def compare(item_a: Item, item_b: Item) -> bool:
#     """Ask user to compare two items."""
#     print(f"{compare(item_a)} v.s. {compare(item_b)}")
