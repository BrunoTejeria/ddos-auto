from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import os



# Poner env vars si quiere login por formulario
username = os.getenv("username")
password = os.getenv("password")


# Poner cookies si quiere login por cookies
cookies = [
    {
        "test": "test"
    }
]


webdriver.FirefoxService(log_output="./output.log")
driver = webdriver.Firefox()


class Main():
    def __init__(self, driver: webdriver.Chrome) -> None:
        driver.get("https://www.stressthem.se")
        driver.implicitly_wait(0.5)
        
        
        print(driver.page_source)
        try:
            self.ip_form = driver.find_element(By.ID, "host")
            self.port_form = driver.find_element(By.ID, "port")
            self.time_form = driver.find_element(By.ID, "time")
            self.method_form = driver.find_element(By.ID, "method")
        except:
            pass

    def login_form(self) -> any:
        driver.get("https://www.stressthem.se/login")
        username_form = driver.find_element(By.ID, "username")
        username_form.send_keys(username)
        password_form = driver.find_element(By.ID, "password")
        password_form.send_keys(password)
        driver.implicitly_wait(0.5)
        driver.find_element(By.CLASS_NAME, "btn").click()

    def login_cookies(self) -> any:
        for cookie in cookies:
            driver.add_cookie(cookie)

    def DDoS_page(self) -> any:
        driver.get("https://www.stressthem.se/hub")

    def driver_quit(self) -> any:
        driver.quit()



main = Main(driver=driver)
main.login_form()



def test():

    button_element = driver.find_element(By.ID, "id_del_boton")  # Reemplaza con el ID real del botón
    button_element.click()

    # Espera a que la página se cargue después de hacer clic en el botón (puedes ajustar el tiempo según sea necesario)
    wait = WebDriverWait(driver, 10)
    element_after_click = wait.until(EC.presence_of_element_located((By.ID, "id_del_elemento_despues_del_clic")))

    # Puedes realizar más acciones después de hacer clic en el botón

    # Cierra el navegador al finalizar
    driver.quit()