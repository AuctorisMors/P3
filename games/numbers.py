from support.game import *

class Numbers(Game):
    # Define our startup func
    def main():
        lang = Settings.lang.numbers_game
        # Run it
        Text.print(lang['intro'], Game.console.Style, Game.console.Width)
        # Our game logic
        def logic():
            Text.print(lang['input'], Game.console.Style, Game.console.Width)
            n1, n2 = 1, 10000
            number = int(Text.request(f"Enter a number between {n1} and {n2}: "))
            num_guess = (n1 + n2) // 2
            guesses = 0
            Text.print(lang['bet'], Game.console.Style, Game.console.Width)
            bet = Settings.funds.bet()
            while number != num_guess:
                Text.print(lang['guess'] + f'{num_guess}?', Game.console.Style, Game.console.Width)
                _ans = ""
                while not _ans:
                    _ans = input('$>').strip().lower()
                    if _ans in ['h', 'high', 'higher']:
                        n1 = num_guess + 1
                    elif _ans in ['l', 'low', 'lower']:
                        n2 = num_guess - 1
                    else:
                        Text.print(Settings.lang_c['not-valid'], Game.console.Style, Game.console.Width)
                        _ans = ""
                num_guess = (n1 + n2) // 2
                guesses += 1
            Text.print(lang['win'] + f'{num_guess}!! ' + lang['guesses'] + f'{guesses}!', Game.console.Style, Game.console.Width)
            Settings.funds.edit(int(guesses * (bet * 0.05)), 'add')
        # Loop our game logic using the game class manager
        Game.loop(Game, logic)