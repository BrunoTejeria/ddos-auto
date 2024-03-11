from typing import Any, Literal, Union, Tuple

from selenium import webdriver
from selenium.webdriver import ChromeService, FirefoxService, EdgeService
from selenium.webdriver import ChromeOptions, FirefoxOptions, EdgeOptions

from config import Config
from utils import exceptions

config = Config()
selenium_config = ...


class Presets():
	def __init__(
		self,
		driver_type: Literal["chrome", "firefox", "edge"]
	) -> None:
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

	def test_preset(
		self,
		**kwargs
	) -> Union[
			Tuple[ChromeService, ChromeOptions],
			Tuple[FirefoxService, FirefoxOptions],
			Tuple[EdgeService, EdgeOptions]
		]:
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

		return self.Service, self.Options

	def default(
		self,
		**kwargs
	) -> Any:

		# Configuración de Service
		try:
			self.Service.log_output = config.selenium_logs["service"]
			self.Service.port = config.port
			...
		except Exception as e:
			raise e

		# Configuración de Options
		try:
			self.Options.add_argument("--headless")
			...
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
		# Configuración de Service
		try:
			self.Service.log_output = config.selenium_logs["service"]
		except Exception as e:
			raise e

		# Configuración de Options
		try:
			self.Options.set_capability(self.capability["logging"], {"browser": "ALL", "performance": "ALL"})
			self.Options.set_capability(self.capability["options"], {"perfLoggingPrefs": {"traceCategories": config.selenium_logs["options"]}})
			...
		except Exception as e:
			raise e

		return self.Service, self.Options
