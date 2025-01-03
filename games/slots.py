from support.game import *

class Slots(Game):
    # Load up params from inheritance
    p = Game.console
    a = Game.game_alert
    random = Game.randomInt
    funds = Settings.funds

    # Parameters for the slot machine
    symbols = ["Ⅻ", "♚", "✪", "♛", "♜", "♝", "♝", "♞", "♞", "♠", "♠", "♣", "♣", "♥", "♥", "♦", "♦", "⚊", "⚊", "⚊", "⛛", "⛛", "⛛", "⛛"]
    symbolsCount = len(symbols)
    slotCount = 3

    # Main game
    def main(funds = funds, p = p, a = a):
        active = True
        # Print the welcome message
        Text.print("Welcome to the Slot Machine! Press Enter to pull the lever and win some coins!", p.Style, p.Width, p.Type)
        Text.print("Press enter to start", p.Style, p.Width, p.Type)
        input() # Wait for the user to press Enter
        while active:
            bet = funds.bet()
            castOut = Slots.pullLever(bet)
            # already deducted bet, so lets add winnings
            funds.edit(castOut, "add")
            # See if they want to play again.
            Text.print("Do you want to play again?", a.Style, p.Width, p.Type)
            active = Text.prompt()
        return funds
    # Pull that lever!
    # Get our symbols, see how much we won
    def pullLever(_bet, p = p, a = a, random = random):
        # Pull the lever
        randomSymbols = ["".join(Slots.symbols[random(0, Slots.symbolsCount - 1)] + " " for _ in range(Slots.slotCount)) for _ in range(3)]
        printedSymbols = "".join(randomSymbols)
        
        # Check if the user won
        _castOut = 0
        for i in range(0, len(printedSymbols), 2):  # Check for which symbols match across the slots and calculate the cash out
            matching_symbols = {i}
            for j in range(i + 2, len(printedSymbols), 2):
                if printedSymbols[i] == printedSymbols[j]:
                    matching_symbols.add(j)
            if i == 0 and printedSymbols[0] == printedSymbols[4] == printedSymbols[8]:
                matching_symbols.update([4, 8])
            if i == 2 and printedSymbols[2] == printedSymbols[4] == printedSymbols[6]:
                matching_symbols.update([4, 6])
            if len(matching_symbols) >= 3:
                symbol = printedSymbols[i]
                if symbol == "⚊":
                    break
                multiplier = {
                    "⛛": 1.05, "♦": 1.10, "♥": 1.15, "♣": 1.20, "♠": 1.25,
                    "♞": 1.30, "♝": 1.35, "♜": 1.40, "♛": 1.45, "✪": 1.50,
                    "♚": 1.55, "Ⅻ": 1.60
                }.get(symbol, 0)
                _castOut += _bet * multiplier
                _castOut += _bet * (len(matching_symbols) - 1) / 2

        # Deduct taxes to keep the game fair
        _castOut = round(_castOut * 0.9)
        
        # Print the slot machine
        Text.print("Slot Machine", p.Style, p.Width, p.Type)
        Text.print(printedSymbols, p.Style, p.Width, "3col")
        Text.print(f"You won {_castOut}!", a.Style, p.Width, p.Type)
        return _castOut