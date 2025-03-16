import webview

from src.api import API, register
from src.config import CONFIG
from src.core.template import render
from src.core.watcher import WatchData, watcher
from src.pages import pages


def create_window(
    *,
    initial_page_name='index',
    context=None,
    title=None,
    width=None,
    height=None,
    resizable=None,
    frameless=None,
    min_size=None,
    background_color=None,
    api=None,
):
    """
    Creates a new PyWebView window with the given parameters.
    It uses the parameters provided or the ones from the config.
    """

    if api is None:
        api = API()

    if not hasattr(pages, initial_page_name):
        raise ValueError(f'Page {initial_page_name} does not exist.')

    context = {'initial_page_name': initial_page_name, **(context or {})}
    base_page = lambda ctx=None: render('base.html', ctx or context)  # noqa: E731

    window = webview.create_window(
        title=title or CONFIG.title,
        width=width or CONFIG.width,
        height=height or CONFIG.height,
        resizable=resizable or CONFIG.resizable,
        frameless=frameless or CONFIG.frameless,
        min_size=min_size or CONFIG.min_size,
        background_color=background_color or CONFIG.background_color,
        html=base_page(),
        js_api=api,
    )

    api._start(window)

    watcher.add_window(
        WatchData(
            window.uid,
            window.title,
            base_page,
            context,
            window,
        )
    )

    return window


@register('window')
class WindowAPI:
    """API for window related functions"""

    def __init__(self, window):
        self.children = {window.uid: []}
        self.maximized = False

    def minimize(self):
        self._window.minimize()

    def toggle_maximize(self):
        if self.maximized:
            self._window.restore()
            self.maximized = False
        else:
            self._window.maximize()
            self.maximized = True

        return self.maximized

    def destroy(self):
        for child in self.children.get(self._window.uid, []):
            child.destroy()

        self._window.destroy()

    def size(self):
        return {
            'width': self._window.width,
            'height': self._window.height,
        }

    def position(self):
        return {
            'x': self._window.x,
            'y': self._window.y,
        }

    def resize(self, width, height, x, y):
        self._window.move(x, y)
        self._window.resize(
            width,
            height,
        )

    def min_size(self):
        return {
            'width': self._window.min_size[0],
            'height': self._window.min_size[1],
        }

    def navigate(self, page_name, context=None):
        if page := getattr(pages, page_name, None):
            self._window.evaluate_js(
                # Update the page content by replacing the root element innerHTML.
                f'document.getElementById("root").innerHTML = `{page(context)}`;'
            )

    def new(self, page_name, kwargs=None):
        window = create_window(initial_page_name=page_name, **(kwargs or {}))

        if self.children.get(self._window.uid):
            self.children[self._window.uid].append(window)
        else:
            self.children[self._window.uid] = [window]
