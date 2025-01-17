# our global settings file
import support.language as Lang
from support.funds import *
from support.text import *
import json
import os

class Settings:
    settings_file = 'settings.json'
    funds = None
    lang = None
    lang_c = None

    @classmethod
    def load_settings(cls):
        if os.path.exists(cls.settings_file):
            with open(cls.settings_file, 'r') as file:
                data = json.load(file)
                cls.funds = Funds(data.get('funds', 1000))
                lang_name = data.get('lang', 'Eng')
                cls.lang = getattr(Lang, lang_name, Lang.Eng)
                cls.lang_c = cls.lang.copy
                Text.set_lang(Text, cls.lang_c)
        else:
            cls.funds = Funds(1000)
            cls.lang = Lang.Eng
            cls.lang_c = Lang.Eng.copy

    @classmethod
    def save_settings(cls):
        data = {
            'funds': cls.funds.get(),
            'lang': cls.lang.__class__.__name__
        }
        with open(cls.settings_file, 'w') as file:
            json.dump(data, file)

    funds = Funds(1000)
    lang = None
    lang_c = None
    ## Get our game language
    @classmethod
    def language_choice(cls, p):
        choices = ['eng', 'esp', 'ukr']
        Text.print('Language: Eng, Esp, Ukr?', p.Style, p.Width)
        _lang = Text.request(choices)
        cls.lang = getattr(Lang, _lang.capitalize(), Lang.Eng)
        cls.lang_c = cls.lang.copy
        Text.set_lang(Text, cls.lang_c)
        return cls.lang
    # Set global language
    def set_language(self, lang):
        self.lang = lang
    # Set global copy
    def set_Language_copy(self, lang):
        self.lang_c = lang.copy
        Text.set_lang(Text, lang.copy)