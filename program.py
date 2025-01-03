# Description: This is a simple Python program created to learn python.
from support.settings import *
import support.game_list as Gl

# Params
basic_para = Text.Paragraph("#", 128, "box")

# Main Func
def main():
    # Start
    lang = Settings.language_choice(basic_para)
    Text.print(lang.copy['intro'] + f"{Settings.funds.get()}", basic_para.Style, basic_para.Width)
    input()
    Settings.set_language(Settings,lang)
    Settings.set_Language_copy(Settings,lang)
    main_menu(basic_para)

# Menu Functions
def main_menu(p):
    lang_copy = Settings.lang_c
    Text.print(lang_copy['main-menu'], p.Style, p.Width)
    menu = {
        0: [lang_copy['menu1'], Gl.Slots.main],
        1: [lang_copy['menu2'], Gl.Numbers.main],
        2: [lang_copy['menu3'], Gl.Guess.main],
        3: [lang_copy['menu1'], Gl.Slots.main],
        4: [lang_copy['menu1'], Gl.Slots.main],
        5: [lang_copy['menu1'], Gl.Slots.main],
        6: [lang_copy['menu1'], Gl.Slots.main],
        7: [lang_copy['about'], about],
        8: [lang_copy['exit'], exit]
    }
    print_menu(menu, p)
    handle_menu_choice(menu, p)

def print_menu(menu, p):
    for x in range(0, len(menu), 3):
        temp = f"{x} - {menu[x][0]} "
        temp1 = f"{x+1} - {menu.get(x+1, ['', ''])[0]} " if x+1 in menu else ''
        temp2 = f"{x+2} - {menu.get(x+2, ['', ''])[0]} " if x+2 in menu else ''
        print('% ' + temp.center(int(p.Width / 3)) + temp1.center(int(p.Width / 3) - 1) + temp2.center(int(p.Width / 3)) + '%')
    print('%' * p.Width)

def handle_menu_choice(menu, p):
    try:
        _choice = int(Text.request(str(list(menu.keys()))))
        menu[_choice][1]()
    except (ValueError, KeyError):
        print("Invalid choice, please try again.")
    main_menu(p)

# About this app
def about():
    Text.print(Settings.lang_c['about_contents'], basic_para.Style, basic_para.Width)
    input('%>')
    main_menu(basic_para)

# Run the main function
if __name__ == "__main__":
    main()