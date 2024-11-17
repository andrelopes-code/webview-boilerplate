import webview

from src.backend.api.base import BaseAPI


class FilesAPI(BaseAPI):
    """API for file related functions"""

    def select_directory(self):
        result = self._window.create_file_dialog(webview.FOLDER_DIALOG, directory='.')
        return result[0] if result else None

    def select_file(self):
        result = self._window.create_file_dialog(
            webview.OPEN_DIALOG,
            directory='.',
            file_types=('Word Document (*.docx)',),
        )
        return result[0] if result else None
