from pydantic import BaseModel
from typing import Literal

class LogSettings(BaseModel):
    log_level: Literal["info", "warning", "debug", "error"]

class ProxiesSettings(BaseModel):
    type: Literal["http", "sock4", "sock5"]