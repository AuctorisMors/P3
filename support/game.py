# This is the master class for each game object
from support.settings import *
import random

class Game:
    #param
    console = Text.Paragraph("@", 128, "box")
    game_alert = Text.Paragraph("!", console.Width, console.Type)
    randomInt = random.randint
    #loop manager
    def loop(self, func):
        while True:
            func()
            Text.print(Settings.lang_c['ending'], self.console.Style, self.console.Width)
            if not Text.prompt():break
