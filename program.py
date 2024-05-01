# Description: This is a simple Python program that takes a string and prints it to the console in a block-text format using an added character as a border, keeping the width of the box to 12 characters
import random

def print_paragraphs(n,char,width):
    # Init some parameters
    n = str(n) # Convert the input to a string
    paragraphs = n.split(" ") # Split the string n into a list of strings    
    # Init blank var to use in the loop
    line = [""] # Initialize the line variable as an empty list
    lineCount = 0 # Initialize the line count to 0
    charCount = 0 # Initialize the character count to 0
    
    # The Function to print the paragraphs
    print() # Print a blank new line to the console
    print(char * width) # Print the top border (char) to the console
    
    for i in range(len(paragraphs)): # Iterate through the list of strings
        if charCount + len(paragraphs[i]) < width - 3: # If the character count plus the length of the current string is less than or equal to the width, add it to the current line
            charCount += len(paragraphs[i]) + 1 # Add the length of the current string to the character count
            line[lineCount] += paragraphs[i] + " " # Add the current string to the line
        else: # If the character count plus the length of the current string is greater than the width, increase line count and reset character count, push the current string to the next line
            lineCount += 1 # Increase the line count by 1
            charCount = len(paragraphs[i]) + 1 # Reset the character count to the length of the current string
            line.append(paragraphs[i] + " ") # Add the current string to the next line
            
    # Print the lines to the console
    for i in range(lineCount + 1):
        print(char + " " + line[i].center(width - 3) + char) # Left justify the string and fill the remaining space with spaces to ensure that each line is the correct width
    print(char * width) # Print the bottom border (char) to the console    
    
# Test the function   
print_paragraphs("test1 test2 test3 test4 test5 test6 test7 test8 test9 test10 test11 test12 test13 test14 test15", "#", 32)