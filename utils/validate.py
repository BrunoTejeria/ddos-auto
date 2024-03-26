import re

class ipv4():
    def __new__(cls) -> bool:
        pattern = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"

        if re.match(pattern, cls):
            componentes = cls.split(".")

            for componente in componentes:
                if not 0 <= int(componente) <= 255:
                    return False
            return True
        else:
            return False

class ipv6:
    def __new__(cls) -> bool:
        ...