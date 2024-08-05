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
        lang = lang.blank
        # Run it
        Text.print(lang['intro'], p.Style, p.Width)

        # Our game play loop
        while True:
            ###logic here###

            # Are we done here? if not, go again
            Text.print(lang['ending'], p.Style, p.Width)
            if not Text.prompt(lang_c):break
