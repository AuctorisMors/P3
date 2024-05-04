# Description: This is a simple Python program that simulates a small slot machine and its support functions for a basic console interface
import random
import support

# Parameters for the slot machine
symbols = ["Ⅻ", "♚", "✪", "♛", "♜", "♝", "♝", "♞", "♞", "♠", "♠", "♣", "♣", "♥", "♥", "♦", "♦", "⚊", "⚊", "⚊", "⛛", "⛛", "⛛", "⛛"]
symbolsCount = len(symbols)
slotCount = 3

def main():
    active = True
    debugCash = 1000
    while active:
        # Print the welcome message
        support.print_paragraphs("Welcome to the Slot Machine! Press Enter to pull the lever and win some coins!", "#", 32, "box")
        support.print_paragraphs("Press enter to start", "%", 32, "box")
        input() # Wait for the user to press Enter
        pullLever(takeBets(debugCash))
    
def takeBets(debugCash):
    ## Take the user's bets
    bet = 0
    while bet <= 0:
        try:
            support.print_paragraphs(f"You have: ${debugCash}", "%", 32, "box")
            bet = int(input("Enter your bet: "))
        except:
            print("Please enter a valid number.")
            bet = 0
        if bet > debugCash:
            print("You don't have enough money to bet that much.")
            bet = 0
    return bet

def pullLever(bet):
    ## Pull the lever
    # Get the random symbols
    randomSymbols = ["","",""]
    for i in range(3):
        for j in range(slotCount):
            randomSymbols[i] += symbols[random.randint(0, symbolsCount - 1)] + " "
    printedSymbols = randomSymbols[0] + randomSymbols[1] + randomSymbols[2]
    
    # Check if the user won
    cashOut = 0
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
                match printedSymbols[i]:
                    case "⚊": # If the symbol is a blank, the user wins nothing
                        break
                    case "⛛":
                        cashOut += bet * 1.05
                    case "♦":
                        cashOut += bet * 1.10
                    case  "♥":
                        cashOut += bet * 1.15
                    case "♣":
                        cashOut += bet * 1.20
                    case "♠":
                        cashOut += bet * 1.25
                    case "♞":
                        cashOut += bet * 1.30
                    case "♝":
                        cashOut += bet * 1.35
                    case "♜":
                        cashOut += bet * 1.40
                    case "♛":
                        cashOut += bet * 1.45
                    case "✪":
                        cashOut += bet * 1.50
                    case "♚":
                        cashOut += bet * 1.55
                    case "Ⅻ":
                        cashOut += bet * 1.60
                # user also gets some money for the number of matching symbols in total
                cashOut += bet * (len(matching_symbols) - 1) / 2
    # Deduct taxes to keep the game fair
    cashOut = cashOut * 0.9
    cashOut = round(cashOut)
    
    # Print the slot machine
    support.print_paragraphs("Slot Machine", "#", 32, "box")
    support.print_paragraphs(printedSymbols, "#", 32, "3col")
    print(f"You won {cashOut}!")
    
    return cashOut
    
# Run the main function
if __name__ == "__main__":
    main()