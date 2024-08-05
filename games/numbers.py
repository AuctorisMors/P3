from support.game import Game

class Numbers(Game):
    # Define out startup func
    def main(funds, lang):
        # Load up params from inheritance
        p = Game.game_para
        a = Game.game_alert
        random = Game.randomInt
        Text = Game.text
        lang = lang.numbers_game
        # Run it
        Text.print(lang['intro'], p.Style, p.Width)
        loop()

        # Our game play loop
        def loop(self):
            print()