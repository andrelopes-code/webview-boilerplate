import atexit
import functools
import logging
import sys
from pathlib import Path

from src.core import alert

logger = logging.getLogger()


def is_frozen():
    """Check if app is frozen"""

    return True if getattr(sys, '_MEIPASS', None) else False


def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""

    project_dir = Path(__file__).parent.parent.parent
    bundler_dir = Path(getattr(sys, '_MEIPASS', project_dir))
    return str(bundler_dir / relative_path)


def register_stop_functions(*functions):
    """
    Function to register cleanup/stop functions using atexit.
    These functions will be called when the app is closed.
    """

    for function in functions:
        atexit.register(function)


def handle_api_errors(cls):
    """
    Decorator that handles uncaught errors in the api
    methods and sends an alert to the frontend.
    """

    for name, method in cls.__dict__.items():
        if callable(method) and not name.startswith('_'):

            @functools.wraps(method)
            def wrapper(self, *args, method=method, **kwargs):
                try:
                    return method(self, *args, **kwargs)

                except Exception as e:
                    logger.exception(e)

                    if window := getattr(self, '_window', None):
                        alert.error(
                            window,
                            str(e),
                            f'Erro em: {self.__class__.__name__}.{method.__name__}',
                        )
                    else:
                        raise

            setattr(cls, name, wrapper)

    return cls
