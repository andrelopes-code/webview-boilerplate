from pathlib import Path
import sys


def is_freezed():
    return getattr(sys, '_MEIPASS', None)


def resource_path(relative_path):
    bundler_dir = Path(getattr(sys, '_MEIPASS', Path(__file__).parent.parent))
    return bundler_dir / relative_path


def load_static_file(filepath, templates_dir, type):
    opentag = ''
    closetag = ''

    try:
        if type == 'css':
            opentag = '<style>'
            closetag = '</style>'
            path = templates_dir / f'static/css/{filepath}'

        elif type == 'js':
            opentag = '<script>'
            closetag = '</script>'
            path = templates_dir / f'static/js/{filepath}'

        else:
            raise ValueError(f'unexpected type provided: {type}')

        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()

        return f'{opentag}\n{content}\n{closetag}'

    except Exception as e:
        print(f'error loading static file {path}: {e}')
        return ''
