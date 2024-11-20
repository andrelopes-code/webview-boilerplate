from src.backend.api.common.clipboard import ClipboardAPI
from src.backend.api.common.system import SystemAPI
from src.backend.api.common.window import WindowAPI


class API:
    def start(self, window):
        self.system = SystemAPI(window)
        self.window = WindowAPI(window)
        self.clipboard = ClipboardAPI()
