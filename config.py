from selenium import webdriver
from selenium.webdriver import ChromeService, FirefoxService, EdgeService
from selenium.webdriver import ChromeOptions, FirefoxOptions, EdgeOptions

import logging
from typing import Union, Literal
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
        self.driver = self.driver()
        self.user_agents = self.user_agents()
        self.selenium_logs = self.selenium_logs()
        self.presets = self.presets()

    def attack(self) -> dict:
        return self.config["attack"]
    def accounts(self) -> dict:
        return self.config["accounts"]

    def cookies(self) -> dict:
        return self.config["cookies"]
    def logs(self) -> dict:
        return self.config["logs"]


    # NOTE: no se si poner que se guarde como diccionario o lista
    def presets(self) -> dict:
        return self.config["selenium"]["presets"]

    def proxies(self) -> Union[list, dict]:
        return self.config["selenium"]["proxies"]

    def drivers(self) -> dict:
        return self.config["selenium"]["driversPath"]

    def driver(self) -> str:
        return self.config["selenium"]["driver"]

    def user_agents(self) -> list:
        with open("./user-agents.json", "r", encoding="utf-8") as f:
            file = f.read()
            return json.loads(file)

    def selenium_logs(self) -> dict:
        return self.config["selenium"]["logs"]





class Selenium():
    def __init__(self) -> None:
        self.config: Config
        self.driver_type: Literal["chrome", "firefox", "edge"]
        self.Service: Union[ChromeService, FirefoxService, EdgeService]
        self.Options: Union[ChromeOptions, FirefoxOptions, EdgeOptions]
        self.mode: str

    def headless(self) -> Union[bool, None]: self.Options.add_argument("--headless")
    
    def change_port(self) -> Union[bool, None]: 
        print(self.mode)
        self.Service.port = self.config.presets[self.mode]["port"]