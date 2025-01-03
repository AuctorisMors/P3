# our global settings file
import support.language as Lang
from support.funds import *
from support.text import *

class Settings:
    funds = Funds(1000)
    lang = None
    lang_c = None
    ## Get our game language
    def language_choice(p):
        choices = ['eng', 'esp', 'ukr']
        Text.print('Language: Eng, Esp, Ukr?', p.Style, p.Width)
        _lang = Text.request(choices)
        return getattr(Lang, _lang.capitalize(), Lang.Eng)
    # Set global language
    def set_language(self, lang):
        self.lang = lang
    # Set global copy
    def set_Language_copy(self, lang):
        self.lang_c = lang.copy
        Text.set_lang(Text, lang.copy)