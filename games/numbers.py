from support.game import *

class Numbers(Game):
    # Define out startup func
    def main(funds, lang = Settings.lang):
        # Run it
        Text.print(Settings.lang.numbers_game['intro'], Game.game_para.Style, Game.game_para.Width)
        # Our game logic
        def logic():
            Text.print(lang['input'], Game.game_para.Style, Game.game_para.Width)
            number = Text.request()
        # Loop our game logic using the game class manager
        Game.loop(Game, logic)
