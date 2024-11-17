import pyperclip


class ClipboardAPI:
    """API for clipboard functions"""

    def get(self):
        return pyperclip.paste()

    def set(self, value):
        pyperclip.copy(value)
