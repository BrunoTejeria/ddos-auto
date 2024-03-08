from selenium import webdriver

import logging
from typing import Union
import json

from utils.schemas import Schemas

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
    def logs(self) -> dict:
        return self.config["logs"]


    # NOTE: no se si poner que se guarde como diccionario o lista
    def proxies(self) -> Union[list, dict]:
        return self.config["selenium"]["proxies"]
    
    def drivers(self) -> dict:
        return self.config["selenium"]["drivers"]
    
    def headless(self) -> dict:
        return self.config["selenium"]["headless"]


a = Config()


class Selenium():
    from selenium.webdriver import (
        ChromeService,
        FirefoxService,
        EdgeService
    )


    def __init__(self, driver: webdriver) -> None:
        self.config = Config()
        self.services = {
            "chrome": self.ChromeService(executable_path=self.config.drivers["chrome"], log_output=self.config.logs["selenium"]),
            "firefox": self.FirefoxService(executable_path=self.config.drivers["firefox"], log_output=self.config.logs["selenium"])
        }

    def set_log(logger: logging.getLogger) -> str:
        logger = logging.getLogger('selenium')
        logger.setLevel(logging.DEBUG)
        handler = logging.FileHandler("./debug.log")
        logger.addHandler(handler)

    def set_proxies() -> bool: ...
    def toggle_headless() -> bool: ...



