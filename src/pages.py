from src.backend.template import render


class Pages:
    INITIAL_PAGE_NAME = 'index'

    def base(self, context=None):
        return render('base.html', context)

    def index(self, context=None):
        return render('index.html', context)


pages = Pages()
