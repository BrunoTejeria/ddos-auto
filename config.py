from selenium import webdriver

import logging
from typing import Union
import json

from utils.schemas import Schemas

class Config:
    def __init__(self, *args, **kwds) -> None:
        with open("./config.json", "r") as f:
            self.config = json.load(f)

        self.attack = self.attack()
        self.accounts = self.accounts()
        self.cookies = self.cookies()
        self.proxies = self.proxies()
        self.drivers = self.drivers()
        self.headless = self.headless()
        self.port = self.port()
        self.selenium_logs = self.selenium_logs()

    def attack(self) -> dict:
        return self.config["attack"]
    def accounts(self) -> dict:
        return self.config["accounts"]

    def cookies(self) -> dict:
        return self.config["cookies"]
    def logs(self) -> dict:
        return self.config["logs"]


    # NOTE: no se si poner que se guarde como diccionario o lista
    def proxies(self) -> Union[list, dict]:
        return self.config["selenium"]["proxies"]

    def drivers(self) -> dict:
        return self.config["selenium"]["drivers"]

    def headless(self) -> dict:
        return self.config["selenium"]["headless"]

    def port(self) -> dict:
        return self.config["selenium"]["port"]

    def selenium_logs(self) -> dict:
        return self.config["selenium"]["logs"]


a = Config()

@PendingDeprecationWarning
class Selenium():



    def __init__(self) -> None:
        self.config = Config()
        #self.services = {
        #    "chrome": self.ChromeService(executable_path=self.config.drivers["chrome"], log_output=self.config.logs["selenium"]),
        #    "firefox": self.FirefoxService(executable_path=self.config.drivers["firefox"], log_output=self.config.logs["selenium"])
        #}

    def toggle_headless() -> bool: ...
     






