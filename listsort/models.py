from dataclasses import dataclass
from enum import Enum

@dataclass
class Item:
        entry: str
        underlined: bool
        

class SortMode(Enum):
    ROUGH = "rough"
    TOP = "top"


@dataclass(frozen=True)
class Record:
        key: str
        mode: SortMode
        above: bool
        pivot: Item
        item: Item
