import webview

from src.api import register


@register('system')
class SystemAPI:
    """API for system related functions"""

    def select_directory(self, multiple=False):
        """
        Opens a dialog to select
        a system directory.
        """

        result = self._window.create_file_dialog(
            webview.FOLDER_DIALOG,
            directory='.',
            allow_multiple=multiple,
        )
        return result[0] if result else None

    def select_file(self, file_types=None, multiple=False):
        """
        Opens a dialog to select
        a system file.
        """

        result = self._window.create_file_dialog(
            webview.OPEN_DIALOG,
            directory='.',
            allow_multiple=multiple,
            file_types=file_types or tuple(),
        )
        return result[0] if result else None
