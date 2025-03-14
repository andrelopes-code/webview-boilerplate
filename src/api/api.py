from src.api.common.clipboard import ClipboardAPI
from src.api.common.system import SystemAPI
from src.api.common.window import WindowAPI


class API:
    def start(self, window):
        self._window = window

        self.system = SystemAPI(window)
        self.window = WindowAPI(window)
        self.clipboard = ClipboardAPI()
