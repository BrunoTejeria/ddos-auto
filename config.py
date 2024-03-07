from selenium import webdriver

from typing import Union
import json


class Config:
    def __init__(self, *args, **kwds) -> None:
        with open("./config.json", "r") as f:
            self.config = json.load(f)

        self.accounts = self.accounts()
        self.cookies = self.cookies()
        self.proxies = self.proxies()
        self.drivers = self.drivers()
        self.headless = self.headless()


    def accounts(self) -> dict:
        return self.config["accounts"]

    def cookies(self) -> dict:
        return self.config["cookies"]


    # NOTE: no se si poner que se guarde como diccionario o lista
    def proxies(self) -> Union[list, dict]:
        return self.config["selenium"]["proxies"]
    
    def drivers(self) -> dict:
        return self.config["selenium"]["drivers"]
    
    def headless(self) -> dict:
        return self.config["selenium"]["headless"]


a = Config()

class Selenium():
    def __init__(self, driver: webdriver) -> None:
        self.config = Config()
    
    def set_proxies() -> bool: ...
    def toggle_headless() -> bool: ...

