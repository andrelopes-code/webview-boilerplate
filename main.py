import webview

from src.backend.api import API
from src.backend.api.common.window import WindowAPI
from src.backend.static import static_server
from src.backend.utils import is_frozen, setup_cleanup_functions
from src.backend.watcher import Watcher
from src.config import CONFIG
from src.pages import pages


class App:
    """Application class to start the application"""

    def start(self):
        try:
            api = API()
            watcher = Watcher()

            setup_cleanup_functions(
                watcher.stop,
                static_server.stop,
            )

            window = WindowAPI.create('index', api=api)
            api.start(window)

            if CONFIG.debug and CONFIG.watch:
                watcher.start(
                    dir_to_watch=CONFIG.templates_dir,
                    callback=lambda: window.load_html(pages.index()),
                )

            webview.start(
                debug=False if is_frozen() else CONFIG.debug, http_server=True
            )

        except Exception:
            import traceback

            traceback.print_exc()


if __name__ == '__main__':
    app = App()
    app.start()
