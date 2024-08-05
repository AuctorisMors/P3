# our global settings file
import support.language as Lang
import support.game_list as Gl
from support.funds import *
from support.text import *

class Settings:
    lang = None
    lang_c = None
    ## Get our game language
    def language_choice(p):
        choices = ['eng','esp','ukr']
        _lang = Lang.Eng.copy #default to eng so this works
        Text.print('Language: Eng, Esp, Ukr?', p.Style, p.Width)
        _lang = Text.request(choices)
        if _lang == 'eng':
            return Lang.Eng
        elif _lang == 'esp':
            return Lang.Esp
        else:
            return Lang.Ukr
    # Set global language
    def set_language(self, lang):
        self.lang = lang
    # Set global copy
    def set_Language_copy(self, lang):
        self.lang_c = lang.copy
        Text.lang = lang.copy