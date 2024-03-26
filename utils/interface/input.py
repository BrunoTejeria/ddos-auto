from typing import Union, Literal, List
from config import Config
from rich.console import Console
from rich.prompt import Prompt


from utils.validate import ipv4

console = Console()





def attack_info_input(
    config: Config = Config(),
    console: Console = Console(),
    *args,
    **kwargs
) -> list[str | int]:

    ip: ipv4 = console.input(f"Ingrese la dirección IP (por defecto: {config.attack['ip']}): ")

        #console.print(f"Formato de ip incorrecto tomando valor por defecto ({config.attack['ip']})", style="red")
    

    port: int = console.input(f"Ingrese el puerto (por defecto: {config.attack['port']}): ")
    if not port == "":
        if port <= 65535:
            pass
        else:
            console.print(f"Pon un puerto en el rango de [0 - 65535]. Tomando valor por defecto ({config.attack['port']})", style="red")

    return ip, port