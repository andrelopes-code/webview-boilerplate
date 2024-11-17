import webview

from src.backend.api import API
from src.backend.static import StaticServer
from src.backend.template import render
from src.backend.utils import is_frozen, setup_cleanup_functions
from src.backend.watcher import Watcher
from src.config import CONFIG


def initialize():
    """Main function to start the application"""

    try:
        api = API()
        watcher = Watcher()
        static_server = StaticServer()

        setup_cleanup_functions(
            watcher.cleanup,
            static_server.cleanup,
        )

        window = webview.create_window(
            title=CONFIG.title,
            width=CONFIG.width,
            height=CONFIG.height,
            resizable=CONFIG.resizable,
            frameless=CONFIG.frameless,
            min_size=CONFIG.min_size,
            background_color=CONFIG.background_color,
            html=render('index.html', **CONFIG.BASE_CONTEXT),
            js_api=api,
        )

        static_server.start()
        api.start(window)

        if CONFIG.debug and CONFIG.watch:
            watcher.start(
                dir_to_watch=CONFIG.templates_dir,
                callback=lambda: window.load_html(
                    render('index.html', **CONFIG.BASE_CONTEXT)
                ),
            )

        webview.start(debug=False if is_frozen() else CONFIG.debug)

    except Exception:
        import traceback

        traceback.print_exc()


if __name__ == '__main__':
    initialize()
