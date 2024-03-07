import json


class Config:
    def __init__(self, *args, **kwds) -> None:
        with open("./config.json", "r") as f:
            self.config = json.load(f)


    def accounts(self) -> dict:
        return self.config["accounts"]
