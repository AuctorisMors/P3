from support.game import *

class Guess(Game):
    # Define out startup func
    def main():
        lang = Settings.lang.guess_game
        # Run it
        Text.print(lang['intro'], Game.console.Style, Game.console.Width)
        # Our game logic
        def logic():
            rnd = random.randint(1, 100)
            numbers = []
            for i in range(0, 101):
                numbers.append(i)
            guess = ''
            guess_count = 0
            Text.print(lang['bet'], Game.console.Style, Game.console.Width)
            bet = Settings.funds.bet()
            Text.print(lang['guess'], Game.console.Style, Game.console.Width)
            while guess != rnd:
                guess = int(Text.request(str(numbers)))
                if guess > rnd:
                    Text.print(lang['wrong_high'], Game.console.Style, Game.console.Width)
                    guess_count += 1
                elif guess < rnd:
                    Text.print(lang['wrong_low'], Game.console.Style, Game.console.Width)
                    guess_count += 1
                else: break
            Text.print(lang['win'] + ' ' + lang['guesses'] + f'{guess_count}!', Game.console.Style, Game.console.Width)
            Settings.funds.edit(int(bet - (guess_count * 15)), 'add')
        # Loop our game logic using the game class manager
        Game.loop(Game, logic)