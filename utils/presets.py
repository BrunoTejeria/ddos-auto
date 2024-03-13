from selenium.webdriver import ChromeService, FirefoxService, EdgeService
from selenium.webdriver import ChromeOptions, FirefoxOptions, EdgeOptions

from typing import Any, Literal, Union, Tuple
import logging

from config import Config
from utils import exceptions
from config import Selenium


class Presets(Selenium):
	def __init__(
		self,
		driver_type: Literal["chrome", "firefox", "edge"]
	) -> None:
		self.config = Config()
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

	def test_preset(
		self,
		**kwargs
	) -> Union[
			Tuple[ChromeService, ChromeOptions],
			Tuple[FirefoxService, FirefoxOptions],
			Tuple[EdgeService, EdgeOptions]
		]:
		self.mode = self.test_preset.__name__

		# Configuración de Service
		try:
			...
		except Exception as e:
			raise e

		# Configuración de Options
		try:
			...
		except Exception as e:
			raise e

		self.logger = logging.getLogger('selenium')
		self.logger.setLevel(logging.DEBUG)
		self.handler = logging.FileHandler(self.config.logs["selenium"])

		return self.Service, self.Options

	def default(
		self,
		**kwargs
	) -> Any:
		self.mode = self.default.__name__

		# Configuración de Service
		try:
			self.Service.port = self.config.port
			...
		except Exception as e:
			raise e

		# Configuración de Options
		try:
			self.headless()
		except Exception as e:
			raise e

		return self.Service, self.Options

	def debug(
		self,
		**kwargs
	) -> Union[
			Tuple[ChromeService, ChromeOptions],
			Tuple[FirefoxService, FirefoxOptions],
			Tuple[EdgeService, EdgeOptions]
		]:
		self.mode = self.debug.__name__
		# Configuración de Service
		try:
			...
		except Exception as e:
			raise e

		# Configuración de Options
		try:
			self.change_port()
			self.Options.set_capability(self.capability["logging"], {"browser": "ALL", "performance": "ALL"})
			self.Options.set_capability(self.capability["options"], {"perfLoggingPrefs": {"traceCategories": self.config.selenium_logs["options"]}})
			...
		except Exception as e:
			raise e

		return self.Service, self.Options
