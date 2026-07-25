from rich.live import Live
from rich.panel import Panel
from rich.console import Group
import time

panel = Panel("[strike][#A5D6FF]test[/][/strike]")
group = Group(panel)

with Live(refresh_per_second=10) as live:
    live.update(group)
    time.sleep(2)