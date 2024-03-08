from utils.schemas.Selenium import (
    LogSettings,
    ProxiesSettings
)



class Schemas:
    class Config:
        class Selenium:
            log_settings: LogSettings
            proxies_settings: ProxiesSettings