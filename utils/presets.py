from selenium.webdriver import ChromeService, FirefoxService, EdgeService
from selenium.webdriver import ChromeOptions, FirefoxOptions, EdgeOptions

from typing import Any, Literal, Union, Tuple
import logging
import traceback

from config import Config
from utils import exceptions
from config import Selenium, SetSeleniumLogger


class Presets(Selenium, SetSeleniumLogger):
	def __init__(
		self,
		driver_type: Literal["chrome", "firefox", "edge"]
	) -> None:
		self.config = Config()
		self.log_path = self.config.logs["selenium"]
		self.driver_type = driver_type

		if driver_type == "chrome":
			self.Service = ChromeService()
			self.Options = ChromeOptions()
			self.capability = {
				"logging": "goog:loggingPrefs",
				"options": "goog:chromeOptions"
			}

		elif driver_type == "firefox":
			self.Service = FirefoxService()
			self.Options = FirefoxOptions()
			self.capability = {
				"logging": "moz:logging",
				"options": "moz:firefoxOptions"
			}

		elif driver_type == "edge":
			self.Service = EdgeService()
			self.Options = EdgeOptions()
			self.capability = {
				"logging": "ms:logging",
				"options": "ms:edgeOptions"
			}

		else:
			raise exceptions.Value(f"driver type solo puede ser 'chrome', 'firefox' o 'edge' driver type: {driver_type}")

		return

	def set(
		self,
		preset: str = "default",
		**kwargs
	) -> Union[
			Tuple[ChromeService, ChromeOptions],
			Tuple[FirefoxService, FirefoxOptions],
			Tuple[EdgeService, EdgeOptions]
		]:


		self.mode = preset


		self._cookies: Union[True, False, None] = ...
		self._debug: Union[True, False, None] = self.config.presets[preset]["debug"]
		self._headless: Union[True, False, None] = self.config.presets[preset]["headless"]
		self._logs: Union[True, False, None] = self.config.presets[preset]["logs"]
		self._port: Union[int, None] = self.config.presets[preset]["port"]
		self._port_switch: Union[True, False, None] = self.config.presets[preset]["portSwitch"]


		try:
			if self._headless == True:
				self.headless()

			if self._logs == True:
				if self._debug:
					self.log_debug()
					self.Options.set_capability(self.capability["logging"], {"browser": "ALL", "performance": "ALL"})
					self.Options.set_capability(self.capability["options"], {"perfLoggingPrefs": {"traceCategories": self.config.selenium_logs["options"]}})
				elif self._debug == False:
					self.log_info()

			if self._port_switch == True:
				self.Service.port = self.config.presets[preset]["port"]

		finally:
			return self.Service, self.Options

	
