import importlib
import inspect
import logging
import os

from src.core import alert
from src.core.utils import handle_api_errors

logger = logging.getLogger()


APIS_DIRECTORY = 'src\\api'
_API_CLASSES_REGISTRY = {}


def register(name):
    """Decorator to register an API class"""

    def decorator(api_class):
        # Check if this API name
        # is already registered.
        if name in _API_CLASSES_REGISTRY:
            raise ValueError(f'API with name {name} already registered')

        api_class = handle_api_errors(api_class)
        _API_CLASSES_REGISTRY[name] = api_class

        return api_class

    return decorator


class API:
    def __init__(self):
        self._window = None

    def _start(self, window):
        self._import_all_api_modules()

        for api_name, api_class in _API_CLASSES_REGISTRY.items():
            init_signature = inspect.signature(api_class.__init__)
            init_parameters = init_signature.parameters
            expect_window = 'window' in init_parameters

            self._window = window

            if expect_window:
                api_instance = api_class(window=window)

            else:
                api_instance = api_class()

            # Inject the window object
            # into the API instance after
            # the constructor is called.
            api_instance._window = window

            setattr(self, api_name, api_instance)

    def _import_all_api_modules(self):
        base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        api_path = os.path.join(base_path, APIS_DIRECTORY)

        for root, dirs, files in os.walk(api_path):
            for file in files:
                if file.endswith('.py') and not file.startswith('__'):
                    rel_path = os.path.relpath(os.path.join(root, file), base_path)
                    module_path = rel_path.replace(os.sep, '.').removesuffix('.py')

                    try:
                        importlib.import_module(module_path)

                    except ImportError as e:
                        logger.exception(f'Error importing {module_path}')
                        raise e


class AlertsMixin:
    def info(self, message, title='Info'):
        alert.info(self._window, message, title)

    def success(self, message, title='Sucesso'):
        alert.success(self._window, message, title)

    def warning(self, message, title='Aviso'):
        alert.warning(self._window, message, title)

    def error(self, message, title='Erro'):
        alert.error(self._window, message, title)
