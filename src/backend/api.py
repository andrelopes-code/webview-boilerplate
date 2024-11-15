from typing import Optional
from webview import Window


class API:
    def __init__(self):
        self._window: Optional[Window] = None

    def set_window(self, window):
        self._window = window

    def hello(self):
        self._window.load_html('<h1>Hello from python!</h1>')
