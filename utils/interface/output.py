from typing import Any
from config import Config

from utils.validate import ipv4


def attack_status_output(
    count: int,
    #attack_host: ipv4 | None = None,
    config: Config = Config(),
    eject_time: float | None = None,
    *args: Any,
    **kwargs: Any
) -> None:
    #TODO: MEJORAR ESTO QUE ES UNA MRDA
    print(f'-----------------\nexecution: {count}\naccount: {config.account["username"]}\nHost: {config.attack["ip"]}\nPort: {config.attack["port"]}\nMethod: {config.attack["method"]}\nAttack time: {config.attack["time"]}\nRemaining Time: {...}\n-----------------')
