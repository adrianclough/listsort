from enum import Enum


class Item:
    def __init__(self, entry: str, underlined: bool):
        self.entry = entry
        self.underlined = underlined


class SortMode(Enum):
    ROUGH = "rough"
    TOP = "top"