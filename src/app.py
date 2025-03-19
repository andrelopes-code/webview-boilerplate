import logging

import webview

from src.api.internal.window import create_window
from src.api.manager import API
from src.config import CONFIG
from src.core.static import static_server
from src.core.utils import register_stop_functions
from src.core.watcher import watcher
from src.pages import pages

logger = logging.getLogger()


class App:
    """Application class to start the application"""

    def start(self):
        try:
            api = API()

            register_stop_functions(
                watcher.stop,
                static_server.stop,
            )

            # Create the main window, starting with the initial page content.
            window = create_window(initial_page_name=pages.INITIAL_PAGE_NAME, api=api)

            api._start(window)

            if CONFIG.debug and CONFIG.watch:
                # Watch for changes in the templates directory.
                watcher.start(dir_to_watch=CONFIG.templates_dir)

            webview.start(debug=CONFIG.debug, http_server=False)

        except Exception:
            logger.exception('Error starting the application')
