import json
import os

from deep_translator import GoogleTranslator


class Translator:
    """Class to translate text using Google Translate API"""

    def __init__(self, locale: str = 'pt', cache_file: str = 'translations_cache.json'):
        self.locale = locale
        self.cache_file = cache_file
        self.translations = {'pt': {}, 'es': {}}
        self._load_cache()

    def _load_cache(self):
        if os.path.exists(self.cache_file):
            with open(self.cache_file, 'r', encoding='utf-8') as f:
                self.translations = json.load(f)

    def _save_cache(self):
        with open(self.cache_file, 'w', encoding='utf-8') as f:
            json.dump(self.translations, f, ensure_ascii=False, indent=2)

    def translate(self, text: str):
        if text in self.translations.get(self.locale, {}):
            return self.translations[self.locale][text]

        try:
            translator = GoogleTranslator(source='auto', target=self.locale)
            translation = translator.translate(text)

            if self.locale not in self.translations:
                self.translations[self.locale] = {}
            self.translations[self.locale][text] = translation
            self._save_cache()

            return translation

        except Exception as e:
            print(f'translation error: {e}')
            return text

    def add_translation(self, locale: str, text: str, translation: str):
        if locale not in self.translations:
            self.translations[locale] = {}
        self.translations[locale][text] = translation
        self._save_cache()

    def set_locale(self, locale: str):
        self.locale = locale

    def __call__(self, text: str):
        return self.translate(text)


t = Translator()
