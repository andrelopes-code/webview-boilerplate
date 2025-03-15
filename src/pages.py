from src.core.template import render


class Pages:
    # The initial page that base.html
    # will load when the window is created.
    INITIAL_PAGE_NAME = 'index'

    def index(self, context=None):
        return render('pages/index.html', context)


pages = Pages()
