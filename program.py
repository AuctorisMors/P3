# Description: This is a simple Python program created to learn python.
import random
from collections import namedtuple
from funds import Funds
from support import Support
from text import Eng

def main():
    # Setup
    Paragraph = namedtuple("Paragraph", ["Style", "Width", "Type"])
    # Params
    basicPara = Paragraph("#", 32, "box")
    language = Eng.copy
    # Start
    Support.print(language["intro"], basicPara.Style, basicPara.Width, basicPara.Type)
    input()
    
# Run the main function
if __name__ == "__main__":
    main()