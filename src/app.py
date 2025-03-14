import webview

from src.api.api import API
from src.api.common.window import create_window
from src.backend.static import static_server
from src.backend.utils import register_stop_functions
from src.backend.watcher import watcher
from src.config import CONFIG
from src.pages import pages


class App:
    """Application class to start the application"""

    def start(self):
        try:
            api = API()

            register_stop_functions(
                watcher.stop,
                static_server.stop,
            )

            window = create_window(
                'base',
                # Pass the initial page name to the base template.
                context={'initial_page_name': pages.INITIAL_PAGE_NAME},
                api=api,
            )

            api.start(window)

            if CONFIG.debug and CONFIG.watch:
                # Watch for changes in the templates directory.
                watcher.start(dir_to_watch=CONFIG.templates_dir)

            webview.start(debug=CONFIG.debug, http_server=True)

        except Exception:
            import traceback

            traceback.print_exc()
