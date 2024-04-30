# Description: This is a simple Python program that prints "Hello, World!" to the console, for now.
import random
import sys

# Take a string and print it to the console in a block-text format using an added character as a border, keeping the width of the box to 80 characters
def print_paragraphs(n,char):
    width = 80 # Set the width of the box to 80 characters
    n = str(n) # Convert the input to a string
    lineCount = 0 # Initialize the line count to 0
    charCount = 0 # Initialize the character count to 0
    paragraphs = n.split(" ") # Split the string n into a list of strings
    num_strings = len(paragraphs)  # Count the number of entries in the list
    # Init blank var to use in the loop
    line = [""] # Initialize the line variable as an empty list
    dummyString = "" # Initialize the dummyString variable as an empty string
    
    print() # Print a blank new line to the console
    print(char * width) # Print the top border (char) to the console
    
    for i in range(len(paragraphs)): # Iterate through the list of strings
        if charCount + len(paragraphs[i]) <= width: # If the character count plus the length of the current string is less than or equal to the width, add it to the new line
            charCount += len(paragraphs[i]) + 1 # Add the length of the current string to the character count
            # load the string entry from line and insert the current string to the end of the dummy string for reinsertion once the loop is done
            dummyString += line[lineCount] + paragraphs[i] + " "
            line.insert(lineCount, dummyString) # Add the current string to the line
        elif charCount + len(paragraphs[i]) > width: # If the character count plus the length of the current string is greater than the width, increase line count and reset character count, push the current string to the next line
            lineCount += 1 
            charCount = 0
            i -= 1
            
    # Print the lines to the console
    for i in range(len(line)):
        print(char + line[i] + char)
    print(char * width) # Print the bottom border (char) to the console

            
    
print_paragraphs("test test2 test3 test4 test5 test6 test7 test8 test9 test10 test11 test12 test13 test14 test15", "*")