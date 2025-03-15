import pyperclip

from src.api.common.base import BaseAPI
from src.core.utils import handle_api_errors


@handle_api_errors
class ClipboardAPI(BaseAPI):
    """API for clipboard functions"""

    def get(self):
        return pyperclip.paste()

    def set(self, value):
        pyperclip.copy(value)
