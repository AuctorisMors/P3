from support.game import *

class Numbers(Game):
    # Define out startup func
    def main():
        lang = Settings.lang.numbers_game
        # Run it
        Text.print(lang['intro'], Game.console.Style, Game.console.Width)
        # Our game logic
        def logic():
            Text.print(lang['input'], Game.console.Style, Game.console.Width)
            n1 = 1
            n2 = 10000
            numbers = []
            for i in range(n1, n2+1):
                numbers.append(i)
            number = int(Text.request(str(numbers)))
            num_guess = (n1+n2)//2
            guesses = 0
            Text.print(lang['bet'], Game.console.Style, Game.console.Width)
            bet = Settings.funds.bet()
            while number != num_guess:
                Text.print(lang['guess'] + f'{num_guess}?', Game.console.Style, Game.console.Width)
                _ans = ""
                while _ans == "":
                    try:
                        _ans = str(input( '$>'))
                    except:
                        print(Settings.lang_c['not-valid'])
                        _ans = ""
                    if _ans.lower() in ['h','high','higher']:
                        n1 = num_guess
                        num_guess = (n1+n2)//2
                        guesses+=1
                        break
                    elif _ans.lower() in ['l','low','lower']:
                        n2 = num_guess
                        num_guess = (n1+n2)//2
                        guesses+=1
                        break
                    else:
                        print(Settings.lang_c['not-valid'])
                        _ans = ""
            Text.print(lang['win'] + f'{num_guess}!! ' + lang['guesses'] + f'{guesses}!', Game.console.Style, Game.console.Width)
            Settings.funds.edit(int(guesses*(bet*0.05)), 'add')
        # Loop our game logic using the game class manager
        Game.loop(Game, logic)