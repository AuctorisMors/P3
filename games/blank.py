from support.game import *

class Numbers(Game):
    # Define out startup func
    def main(funds):
        # Load up params from inheritance
        lang_c = Settings.lang_c
        lang = Settings.lang.numbers_game
        # Run it
        Text.print(lang['intro'], Game.game_para.Style, Game.game_para.Width)
        # Our game logic
        def logic():
            print("")
        # Loop our game logic using the game class manager
        Game.loop(Game, logic, lang, lang_c)
