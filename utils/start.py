import os


class CheckInit:
    def __call__(self, *args, **kwds) -> None:
        if os.path.exists("./logs/selenium/"):
            pass
        else:
            os.makedirs("./logs/selenium/")
