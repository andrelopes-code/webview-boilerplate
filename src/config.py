from pathlib import Path

import webview

from src.core.utils import is_frozen, resource_path

webview.settings['OPEN_DEVTOOLS_IN_DEBUG'] = True

STATIC_DIR = Path(resource_path('src/frontend')) / 'static'
TEMPLATES_DIR = Path(resource_path('src/frontend')) / 'templates'


class CONFIG:
    """Application configuration"""

    title = 'PyWebView Boilerplate App'
    width = 800
    height = 600
    resizable = True
    frameless = True
    min_size = 800, 600
    templates_dir = TEMPLATES_DIR
    static_dir = STATIC_DIR
    debug = False if is_frozen() else True
    watch = True

    # Background color of the window. This
    # color blinks when the window starts.
    background_color = '#f0f2f2'

    BASE_CONTEXT = {
        'resizable': resizable,
        'title': title,
    }
