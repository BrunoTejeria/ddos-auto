import re

class ipv4:
    @staticmethod
    def __call__(cls, ip_address) -> bool:
        pattern = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
        if re.match(pattern, ip_address):
            components: int = ip_address.split(".")
            for component in components:
                if not 0 <= int(component) <= 255:
                    return False
            return True
        else:
            return False

class ipv6:
    @staticmethod
    def __call__(cls, ip_address) -> bool:
        pattern = r"^(?:[A-F0-9]{1,4}:){7}[A-F0-9]{1,4}$"
        if re.match(pattern, ip_address, re.IGNORECASE):
            return True
        else:
            return False

class port:
    @staticmethod
    def __call__(cls, port_number) -> bool:
        if 0 <= port_number <= 65535:
            return True
        else:
            return False
