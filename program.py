# Description: This is a simple Python program that prints "Hello, World!" to the console, for now.
import random
import sys

# Take a string and print it to the console in a block-text format using an added character as a border, keeping the width of the box to 80 characters
def print_paragraphs(n,char):
    width = 80 # Set the width of the box to 80 characters
    n = str(n) # Convert the input to a string
    paragraphs = n.split(" ") # Split the string n into a list of strings
    num_strings = len(paragraphs)  # Count the number of entries in the list
    
    print(char * width) # Print the top border (char) to the console
    
    for i in range(num_strings): # Loop through the list
        char_count = 0 # Initialize the character count
        line = "" # Initialize the line

        for j in range(len(paragraphs[i])): # Loop through the characters in the string
            char_count += 1 # Increment the character count
            line = line + paragraphs[i] # Add the character to the line
            if char_count == width: # If the character count is equal to the width, break to a new line
                print(line)
                i -= 1
                break
        print(char, " ") # Print the right border (char) to the console and return to the next line
            
    print(char * width) # Print the bottom border (char) to the console

            
    
print_paragraphs("test test2 test3 test4", "*")