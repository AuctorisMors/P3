# This is the master class for each game object
from support.settings import *
import random

class Game:
    #param
    game_para = Text.Paragraph("@", 128, "box")
    game_alert = Text.Paragraph("!", game_para.Width, game_para.Type)
    randomInt = random.randint
    #loop manager
    def loop(self, func):
        while True:
            func()
            Text.print(Settings.lang_c['ending'], self.game_para.Style, self.game_para.Width)
            if not Text.prompt():break
