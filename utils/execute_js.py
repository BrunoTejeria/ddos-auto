
from typing import Any


class ExecuteJs:
    def __init__(self) -> None:
        pass

    def run_js(self, script_name):
        path = "./utils/js/"
        with open(
            file=path+script_name,
            mode="r",
            encoding="utf-8"
        ) as f:
            return f.read()