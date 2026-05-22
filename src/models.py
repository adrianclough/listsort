from dataclasses import dataclass
from enum import Enum

@dataclass
class Item:
        entry : str
        underlined : bool


class SortMode(Enum):
    ROUGH = "rough"
    TOP = "top"