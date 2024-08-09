from support.game import *

class Numbers(Game):
    # Define out startup func
    def main():
        lang = Settings.lang.numbers_game
        # Run it
        Text.print(lang['intro'], Game.console.Style, Game.console.Width)
        # Our game logic
        def logic():
            print("")
        # Loop our game logic using the game class manager
        Game.loop(Game, logic)