from support.game import Game

class Slots(Game):
    # Load up params from inheritance
    p = Game.game_para
    a = Game.game_alert
    random = Game.randomInt
    Text = Game.text

    # Parameters for the slot machine
    symbols = ["Ⅻ", "♚", "✪", "♛", "♜", "♝", "♝", "♞", "♞", "♠", "♠", "♣", "♣", "♥", "♥", "♦", "♦", "⚊", "⚊", "⚊", "⛛", "⛛", "⛛", "⛛"]
    symbolsCount = len(symbols)
    slotCount = 3

    # Main game
    def main(funds, lang, p = p, a = a, Text = Text):
        lang = lang.copy
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
            active = Text.prompt(lang)
        return funds
    # Pull that lever!
    # Get our symbols, see who much we won
    def pullLever(_bet, p = p, a = a, random = random, Text = Text):
        ## Pull the lever
        # Get the random symbols
        randomSymbols = ["","",""]
        for i in range(3):
            for j in range(Slots.slotCount):
                randomSymbols[i] += Slots.symbols[random(0, Slots.symbolsCount - 1)] + " "
        printedSymbols = randomSymbols[0] + randomSymbols[1] + randomSymbols[2]
        # Check if the user won
        _castOut = 0
        for i in range(len(printedSymbols)): # Check for which symbols match across the slots and calculate the cash out. Check only odd entries and set.
            if i % 2 == 0:
                matching_symbols = set() # Use a set to avoid duplicates
                for j in range(i, len(printedSymbols), 2): # Check the other symbols in the same slot
                    if printedSymbols[i] == printedSymbols[j]: # If the symbols match, add them to the set
                        matching_symbols.add(j) # Add the index of the matching symbol
                # check for diagonal matches and add them to the set
                if i == 0 and printedSymbols[0] == printedSymbols[4] == printedSymbols[8]:
                    matching_symbols.add(4)
                    matching_symbols.add(8)
                # check for the other diagonal match and add them to the set
                if i == 2 and printedSymbols[2] == printedSymbols[4] == printedSymbols[6]:
                    matching_symbols.add(4)
                    matching_symbols.add(6)
                if len(matching_symbols) >= 3: # If there are at least 3 matching symbols, the user wins an amount based on the symbol
                    for x in printedSymbols[i]:
                        if "⚊": # If the symbol is a blank, the user wins nothing
                            break
                        elif "⛛":
                            _castOut += _bet * 1.05
                        elif "♦":
                            _castOut += _bet * 1.10
                        elif "♥":
                            _castOut += _bet * 1.15
                        elif "♣":
                            _castOut += _bet * 1.20
                        elif "♠":
                            _castOut += _bet * 1.25
                        elif "♞":
                            _castOut += _bet * 1.30
                        elif "♝":
                            _castOut += _bet * 1.35
                        elif "♜":
                            _castOut += _bet * 1.40
                        elif "♛":
                            _castOut += _bet * 1.45
                        elif "✪":
                            _castOut += _bet * 1.50
                        elif "♚":
                            _castOut += _bet * 1.55
                        elif "Ⅻ":
                            _castOut += _bet * 1.60
                        else:
                            _castOut += _bet * 0
                    # user also gets some money for the number of matching symbols in total
                    _castOut += _bet * (len(matching_symbols) - 1) / 2
        # Deduct taxes to keep the game fair
        _castOut = _castOut * 0.9
        _castOut = round(_castOut)
        # Print the slot machine
        Text.print("Slot Machine", p.Style, p.Width, p.Type)
        Text.print(printedSymbols, p.Style, p.Width, "3col")
        Text.print(f"You won {_castOut}!", a.Style, p.Width, p.Type)
        return _castOut