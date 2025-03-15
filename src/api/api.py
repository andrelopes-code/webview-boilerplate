from src.api.common.clipboard import ClipboardAPI
from src.api.common.system import SystemAPI
from src.api.common.window import WindowAPI


class API:
    def start_internal_apis(self, window):
        self.system = SystemAPI(window)
        self.window = WindowAPI(window)
        self.clipboard = ClipboardAPI(window)

    def start(self, window):
        # Internal APIs used by the frontend.
        self.start_internal_apis(window)

        # your APIs here.
        # self.foo = FooAPI(window)
