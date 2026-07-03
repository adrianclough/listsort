"""Minimal rich.live example.

Shows a single Live region that gets updated repeatedly.
Each update replaces the entire content — nothing scrolls.
"""

from rich.live import Live
from rich.panel import Panel
import time

items = ["Buy groceries", "Call dentist", "Sort inbox", "Clean bedroom"]

with Live(refresh_per_second=10) as live:
    for i, item in enumerate(items):
        # Each call to live.update() replaces what's on screen
        live.update(
            Panel(f"Now showing item {i + 1} of {len(items)}:\n\n[bold]{item}[/bold]")
        )
        time.sleep(1.5)

    live.update(Panel("[green]Done![/green]"))
    time.sleep(1)