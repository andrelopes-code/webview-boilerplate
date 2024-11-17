import webview

from src.backend.api.base import BaseAPI


class FilesAPI(BaseAPI):
    """API for file related functions"""

    def select_directory(self):
        result = self._window.create_file_dialog(webview.FOLDER_DIALOG, directory='.')
        return result[0] if result else None
