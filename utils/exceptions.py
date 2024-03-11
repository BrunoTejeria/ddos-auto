from typing import Any


class Value(ValueError):
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print(type(self))    # la clase de excepción
        print(self.args)     # argumentos almacenados en .args
        print(self)
        return super().__call__(*args, **kwds)

class Error(Exception):
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print(self.args)
        print(self)
        return super().__call__(*args, **kwds)