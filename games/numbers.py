from support.game import Game

class Numbers(Game):
    # Define out startup func
    def main(funds, lang):
        # Load up params from inheritance
        lang_c = lang.copy
        lang = lang.numbers_game
        # Run it
        Game.console.print(lang['intro'], Game.game_para.Style, Game.game_para.Width)
        # Our game logic
        def logic():
            print("")
        # Loop our game logic using the game class manager
        Game.loop(Game, logic, lang, lang_c)
