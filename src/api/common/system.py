import webview

from src.api.common.base import BaseAPI
from src.backend.utils import handle_api_errors


@handle_api_errors
class SystemAPI(BaseAPI):
    """API for system related functions"""

    def select_directory(self, multiple=False):
        result = self._window.create_file_dialog(
            webview.FOLDER_DIALOG,
            directory='.',
            allow_multiple=multiple,
        )
        return result[0] if result else None

    def select_file(self, file_types=None, multiple=False):
        result = self._window.create_file_dialog(
            webview.OPEN_DIALOG,
            directory='.',
            allow_multiple=multiple,
            file_types=file_types or tuple(),
        )
        return result[0] if result else None
