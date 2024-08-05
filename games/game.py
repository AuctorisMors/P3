# This is the master class for each game object
from support.text import Text
import random
class Game:
    #param
    game_para = Text.Paragraph("@", 128, "box")
    game_alert = Text.Paragraph("!", game_para.Width, game_para.Type)
