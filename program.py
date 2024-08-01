# Description: This is a simple Python program created to learn python.
import random
from collections import namedtuple
from support.funds import Funds
from support.text import Text
import support.language as Lang
from games.slots import Slots

## Main Func
def main():
    # Setup
    Paragraph = namedtuple("Paragraph", ["Style", "Width", "Type"])
    # Params
    basic_para = Paragraph("#", 32, "box")
    lang = language_choice(basic_para)
    funds = Funds(1000)
    balance_str = f"{funds.get()}"
    # Start
    Text.print(lang['intro'] + balance_str, basic_para.Style, basic_para.Width)
    input()
    main_menu(basic_para, lang, funds)
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
def main_menu(p,lang, funds):
    funds = Funds(funds)
    Text.print(lang['main-menu'], p.Style, p.Width)
    menu = {
        '1' : ['3 Lane Slots', Slots.main(funds.get)]
    }
    menu['1'][1]
    ## bet is broken??
# Run the main function
if __name__ == "__main__":
    main()