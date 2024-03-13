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
    #------------------------------------------
    # Funciones para cambiar configuraciones de selenium
    #------------------------------------------
    #
    # Desactivar abrir ventana de navegador
    def headless(self) -> Union[bool, None]: self.Options.add_argument("--headless")
    # Cambiar puerto que se una en selenium
    def change_port(self) -> Union[bool, None]: self.Service.port = self.config.presets[self.mode]["port"]


class SetSeleniumLogger:
    def __init__(self) -> None:
        self.logger: logging

        # Configurar logger para selenium
        self.logger.getLogger('selenium')

        # Handler para agregar archivo de output
        handler = logging.FileHandler("./logs/selenium/selenium.log")
        self.logger.addHandler(handler)

    #------------------------------------------
    # Funciones para setear nivel de logger
    #------------------------------------------
    #
    def critical(self) ->  None: self.logger.setLevel(logging.CRITICAL) # Set critical
    def error(self)    ->  None: self.logger.setLevel(logging.ERROR) # Set error
    def warning(self)  ->  None: self.logger.setLevel(logging.WARNING) # Set warning
    def info(self)     ->  None: self.logger.setLevel(logging.INFO) # Set info
    def debug(self)    ->  None: self.logger.setLevel(logging.DEBUG) # Set debug
    def notset(self)   ->  None: self.logger.setLevel(logging.NOTSET) # Set notset

