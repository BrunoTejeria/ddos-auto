from selenium import webdriver
from selenium.webdriver import ChromeService, FirefoxService, EdgeService
from selenium.webdriver import ChromeOptions, FirefoxOptions, EdgeOptions

import logging
from typing import Union, Literal
import json


class Config:
    def __init__(self, *args, **kwargs) -> None:
        with open("./config.json", "r") as f:
            self.config = json.load(f)

        self.attack = self.attack()
        self.account = self.account()
        self.cookies = self.cookies()
        self.proxies = self.proxies()
        self.drivers = self.drivers()
        self.driver = self.driver()
        self.user_agents = self.user_agents()
        self.selenium_logs = self.selenium_logs()
        self.presets = self.presets()
        self.logs = self.logs()
        self.port = None # Función de llamar atributo deshabilitada, llama a el método port()

    def attack(self) -> dict:
        return self.config["attack"]
    def account(self) -> dict:
        return self.config["account"]

    def cookies(self) -> dict:
        return self.cookies()
    def logs(self) -> dict:
        return self.config["logs"]


    def presets(self) -> dict:
        return self.config["selenium"]["presets"]

    def proxies(self) -> Union[list, dict]:
        return self.config["selenium"]["proxies"]

    def drivers(self) -> dict:
        return self.config["selenium"]["driversPath"]

    def driver(self) -> str:
        return self.config["selenium"]["driver"]

    def selenium_logs(self) -> dict:
        return self.config["selenium"]["logs"]

    def port(self, preset: str) -> int:
        return self.config[preset]["port"]

    def user_agents(self) -> list:
        with open("./user-agents.json", "r", encoding="utf-8") as f:
            file = f.read()
            return json.loads(file)

    def cookies(self) -> dict:
        with open("./cookies.json", "r") as f:
            return json.load(f)









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

config = Config()

class SetSeleniumLogger:

    def __init_subclass__(cls) -> None:
        cls.logger: logging
        # Configurar logger para selenium
        cls.logger = logging.getLogger('selenium')

        # Handler para agregar archivo de output
        handler = logging.FileHandler(config.logs["selenium"])
        cls.logger.addHandler(handler)
    #------------------------------------------
    # Funciones para setear nivel de logger
    #------------------------------------------
    #
    def log_critical(self) ->  None: self.logger.setLevel(logging.CRITICAL) # Set critical
    def log_error(self)    ->  None: self.logger.setLevel(logging.ERROR) # Set error
    def log_warning(self)  ->  None: self.logger.setLevel(logging.WARNING) # Set warning
    def log_info(self)     ->  None: self.logger.setLevel(logging.INFO) # Set info
    def log_debug(self)    ->  None: self.logger.setLevel(logging.DEBUG) # Set debug
    def log_notset(self)   ->  None: self.logger.setLevel(logging.NOTSET) # Set notset