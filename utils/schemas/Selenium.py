from pydantic import BaseModel
from typing import Literal

@DeprecationWarning
class LogSettings(BaseModel):
    log_level: Literal["info", "warning", "debug", "error"]

@DeprecationWarning
class ProxiesSettings(BaseModel):
    type: Literal["http", "sock4", "sock5"]