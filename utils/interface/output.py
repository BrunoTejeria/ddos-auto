from typing import Any
from rich.console import Console
from rich.table import Table
import datetime

from config import Config
from utils.validate import ipv4, port


def attack_status_output(
    count: int,
    attack_host: ipv4 | None = None,
    attack_port: port | None = None,
    config: Config = Config(),
    console: Console = Console(),
    eject_time: float | None = datetime.datetime.now(),
    *args: Any,
    **kwargs: Any
) -> None:
    table = Table(show_header=False, min_width=32, show_lines=True, caption_justify="center")
    table.add_column()
    table.add_column()

    table.add_row("Execution Number", str(count))
    table.add_row("Account", str(config.account["username"]))
    table.add_row("Host", str(attack_host))
    table.add_row("Port", str(attack_port))
    table.add_row("Method", str(config.attack["method"]))
    table.add_row("Attack Time", str(config.attack["time"]))
    table.add_row("Execution Time", str(eject_time))
    console.print(table)
