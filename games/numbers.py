from support.game import Game

class Numbers(Game):
    # Load up params from inheritance
    p = Game.game_para
    a = Game.game_alert
    random = Game.randomInt
    Text = Game.text
    game_text = 'numbers_game'

    def main(self, funds, lang):
        self.Text.print(lang['game_text'])