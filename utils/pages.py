from selenium import webdriver

class Pages:
    def __init__(self) -> None:
        self.driver: webdriver

    def index_page(self) -> None:
        self.driver.get("https://www.stressthem.se")

    def login_page(self) -> None:
        self.driver.get("https://www.stressthem.se/login")

    def DDoS_page(self) -> None:
        self.driver.get("https://www.stressthem.se/hub")