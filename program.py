# Description: This is a simple Python program created to learn python.
from support.settings import *

# Params
basic_para = Text.Paragraph("#", 128, "box")
funds = Funds(1000)

# Main Func
def main():
    # Start
    lang = Settings.language_choice(basic_para)
    Text.print(lang.copy['intro'] + f"{funds.get()}", basic_para.Style, basic_para.Width)
    input()
    Settings.set_language(Settings, lang)
    Settings.set_Language_copy(Settings, lang)
    main_menu(basic_para)

# Menu Functions
## Define out main menu
def main_menu(p):
    lang_copy = Settings.lang_c
    lang = Settings.lang
    Text.print(lang_copy['main-menu'], p.Style, p.Width)
    menu = {
        0 : [lang_copy['menu1'], Gl.Slots.main], 1 : [lang_copy['menu2'], Gl.Numbers.main], 2 : [lang_copy['menu1'], Gl.Slots.main],
        3 : [lang_copy['menu1'], Gl.Slots.main], 4 : [lang_copy['menu1'], Gl.Slots.main], 5 : [lang_copy['menu1'], Gl.Slots.main],
        6 : [lang_copy['menu1'], Gl.Slots.main], 7 : [lang_copy['menu2'], Gl.Slots.main], 8 : [lang_copy['menu2'], Gl.Slots.main]
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
    _choice = int(Text.request(str(menu.keys())))
    menu[_choice][1](funds)
# Run the main function
if __name__ == "__main__":
    main()