from support.game import *

class Numbers(Game):
    # Define out startup func
    def main():
        lang = Settings.lang.numbers_game
        # Run it
        Text.print(lang['intro'], Game.game_para.Style, Game.game_para.Width)
        # Our game logic
        def logic():
            Text.print(lang['input'], Game.game_para.Style, Game.game_para.Width)
            numbers = []
            for i in range(2, 10001):
                numbers.append(i)
            number = int(Text.request(str(numbers)))
        # Loop our game logic using the game class manager
        Game.loop(Game, logic)
