import sys

from cx_Freeze import Executable, setup

ENTRYPOINT = 'main.py'

NAME = 'PyWebview Boilerplate'
DESCRIPTION = 'PyWebview Boilerplate'
ICON = 'src/frontend/static/assets/icon.ico'
VERSION = '1.0'

HIDE_TERMINAL = True

build_exe_options = {
    'include_files': [
        (
            'src/frontend',
            'src/frontend',
        ),
    ],
}


base = None

if sys.platform == 'win32' and HIDE_TERMINAL:
    base = 'Win32GUI'

executables = [
    Executable(
        ENTRYPOINT,
        base=base,
        icon=ICON,
        shortcut_name=NAME,
        shortcut_dir='DesktopFolder',
    )
]

setup(
    name=NAME,
    version=VERSION,
    options={'build_exe': build_exe_options},
    executables=executables,
)
