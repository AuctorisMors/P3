# Description: This is a simple Python program created to learn python.
import random
from collections import namedtuple
from support.funds import Funds
from support.text import Text
import support.language as Lang
from games.slots import Slots

# Setup
Paragraph = namedtuple("Paragraph", ["Style", "Width", "Type"])
# Params
basic_para = Paragraph("#", 32, "box")
funds = Funds(1000)

## Main Func
def main():
    # Start
    lang = language_choice(basic_para)
    Text.print(lang['intro'] + f"{funds.get()}", basic_para.Style, basic_para.Width)
    input()
    main_menu(basic_para, lang)
## Get our game language
def language_choice(p):
    choices = ['eng','esp','ukr']
    _lang = Lang.Eng.copy #default to eng so this works
    Text.print('Language: Eng, Esp, Ukr?', p.Style, p.Width)
    _lang = Text.request(choices, _lang)
    if _lang == 'eng':
        return Lang.Eng.copy
    elif _lang == 'esp':
        return Lang.Esp.copy
    else:
        return Lang.Ukr.copy
## Define out main menu
def main_menu(p,lang):
    Text.print(lang['main-menu'], p.Style, p.Width)
    menu = {
        '1' : ['3 Lane Slots', Slots.main],
        '2' : ['3 Lane Slots', Slots.main]
    }
    menu['1'][1](funds,lang)
    print(f'{funds.get()}')
# Run the main function
if __name__ == "__main__":
    main()