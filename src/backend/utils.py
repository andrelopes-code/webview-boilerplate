import atexit
import sys
from pathlib import Path


def is_frozen():
    """Check if app is frozen"""

    return True if getattr(sys, '_MEIPASS', None) else False


def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""

    bundler_dir = Path(getattr(sys, '_MEIPASS', Path(__file__).parent.parent))
    return bundler_dir / relative_path


def setup_cleanup_functions(*functions):
    """Function to register cleanup functions"""

    for function in functions:
        atexit.register(function)
