# Description: This is a simple Python program created to learn python.
import games.slots
from support.funds import Funds
from support.text import Text
import support.language as Lang
import games

# Params
basic_para = Text.Paragraph("#", 128, "box")
funds = Funds(1000)

# Main Func
def main():
    # Start
    lang = language_choice(basic_para)
    Text.print(lang['intro'] + f"{funds.get()}", basic_para.Style, basic_para.Width)
    input()
    main_menu(basic_para, lang)


# Menu Functions
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
        0 : [lang['menu1'], games.slots.Slots.main], 1 : [lang['menu2'], games.slots.Slots.main], 2 : [lang['menu1'], games.slots.Slots.main],
        3 : [lang['menu1'], games.slots.Slots.main], 4 : [lang['menu1'], games.slots.Slots.main], 5 : [lang['menu1'], games.slots.Slots.main],
        6 : [lang['menu1'], games.slots.Slots.main], 7 : [lang['menu2'], games.slots.Slots.main], 8 : [lang['menu2'], games.slots.Slots.main]
    }
    ## Print out menu
    for x in menu.keys():
        if x % 3 == 0 or x == 1:
            temp = str(x) + ' - ' + menu[x][0] + ' '
            try:
                temp1 = str(x+1) + ' - ' + menu[x+1][0] + ' '
            except:
                pass
            try:
                temp2 = str(x+2) + ' - ' + menu[x+2][0] + ' '
            except:
                pass
            print('% ' + temp.center(int(p.Width / 3)) + temp1.center(int(p.Width / 3) - 1) + temp2.center(int(p.Width / 3))+ '%')
    print('%' * p.Width)
    ## Request the player pick an option, convert out keys to str for compat with the request func but back to int for key usage lol
    _choice = int(Text.request(str(menu.keys()), lang))
    menu[_choice][1](funds, lang)
# Run the main function
if __name__ == "__main__":
    main()