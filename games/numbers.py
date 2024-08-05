from support.game import Game

class Numbers(Game):
    # Define out startup func
    def main(funds, lang):
        # Load up params from inheritance
        p = Game.game_para
        a = Game.game_alert
        random = Game.randomInt
        Text = Game.text
        lang_c = lang.copy
        lang = lang.numbers_game
        # Run it
        Text.print(lang['intro'], p.Style, p.Width)
        # Our game logic
        def logic():
            print("")
        # Loop our game logic using the game class manager
        Game.loop(Game, logic, lang, lang_c)
