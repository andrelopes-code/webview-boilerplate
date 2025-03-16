import pyperclip

from src.api import register


@register('clipboard')
class ClipboardAPI:
    """API for clipboard functions"""

    def get(self):
        """
        Get the content stored
        in the clipboard.
        """

        return pyperclip.paste()

    def set(self, value):
        """
        set the value passed
        to the clipboard.
        """

        pyperclip.copy(value)
