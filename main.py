import os
import webview
import atexit
from src.backend import static
from src.backend.utils import is_freezed
from src.backend.api import API
from src.config import CONFIG
from src.backend.templating import render


static_thread = static.serve()
atexit.register(static_thread.cleanup)


def main():
    api = API()

    window = webview.create_window(
        title=CONFIG.title,
        js_api=api,
        width=CONFIG.width,
        height=CONFIG.height,
        resizable=CONFIG.resizable,
        min_size=CONFIG.min_size,
        html=render('index.html', pwd=os.getcwd()),
    )

    api.set_window(window)

    webview.start(
        debug=False if is_freezed() else CONFIG.debug,
        http_port=CONFIG.port,
    )


if __name__ == '__main__':
    main()
