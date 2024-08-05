# This is the master class for each game object
from support.text import Text
import random

class Game:
    #param
    game_para = Text.Paragraph("@", 128, "box")
    game_alert = Text.Paragraph("!", game_para.Width, game_para.Type)
    randomInt = random.randint
    console = Text
    lang_c = None
    #loop manager
    def loop(self, func, lang, lang_c):
        while True:
            func()
            Text.print(lang['ending'], self.game_para.Style, self.game_para.Width)
            if not Text.prompt(lang_c):break
