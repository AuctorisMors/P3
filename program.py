# Description: This is a simple Python program that simulates a small slot machine and its support functions for a basic console interface
import random
import support

# Parameters for the slot machine
symbols = ["Ⅻ", "♚", "✪", "♛", "♜", "♝", "♝", "♞", "♞", "♠", "♠", "♣", "♣", "♥", "♥", "♦", "♦", "⚊", "⚊", "⚊", "⛛", "⛛", "⛛", "⛛"]
symbolsCount = len(symbols)
slotCount = 3

def main():
    active = True
    while active:
        # Print the welcome message
        support.print_paragraphs("Welcome to the Slot Machine! Press Enter to pull the lever and win some coins!", "#", 32, "box")
        input() # Wait for the user to press Enter
        #takeBets() # Take the user's bets
        pullLever() # Pull the lever
    
def pullLever():
    ## Pull the lever
    # Get the random symbols
    randomSymbols = ["","",""]
    for i in range(3):
        for j in range(slotCount):
            randomSymbols[i] += str(symbols[random.randint(0, symbolsCount - 1)]) + " "
    printedSymbols = randomSymbols[0] + randomSymbols[1] + randomSymbols[2]
    
    # Print the slot machine
    support.print_paragraphs("Slot Machine", "#", 32, "box")
    support.print_paragraphs(printedSymbols, "#", 32, "3col")
    
# Run the main function
if __name__ == "__main__":
    main()