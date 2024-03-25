from selenium import webdriver

import logging
import json

from bot import Bot
from config import Config
from utils.presets import Presets



config = Config()

main_logger = logging.getLogger()
main_logger.addHandler(logging.FileHandler(config.logs["main"]))
main_logger.setLevel(logging.DEBUG)

presets = Presets(driver_type=config.driver)
service, options = presets.default()

driver = webdriver.Chrome(service=service, options=options)
bot = Bot(
    driver=driver,
    main_logger=main_logger,
    username=config.account["username"],
    password=config.account["password"]
    )

bot.login_form()
bot.DDoS_page()
bot.close_button()

cookies = bot.get_cookies()
# NOTE: No se si guardarlos en config.json o en cookies.json
with open("cookies.json", "w", encoding="utf-8") as f:
    f.write(cookies)

