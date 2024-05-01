def print_paragraphs(n,char,width,bType = None):
    # Init some parameters
    boxType = "box" if bType == None else bType # Set the box type to "box" if the type is None, otherwise set it to the type
    n = str(n) # Convert the input to a string
    paragraphs = n.split(" ") # Split the string n into a list of strings    
    # Init blank var to use in the loop
    line = [""] # Initialize the line variable as an empty list
    lineCount = 0 # Initialize the line count to 0
    charCount = 0 # Initialize the character count to 0
    
    # The Function to print the paragraphs
    print() # Print a blank new line to the console
    print(char * width) # Print the top border (char) to the console
    
    if boxType == "box": # If the box type is "box", print the box type
        for i in range(len(paragraphs)): # Iterate through the list of strings
            if charCount + len(paragraphs[i]) < width - 3: # If the character count plus the length of the current string is less than or equal to the width, add it to the current line
                charCount += len(paragraphs[i]) + 1 # Add the length of the current string to the character count
                line[lineCount] += paragraphs[i] + " " # Add the current string to the line
            else: # If the character count plus the length of the current string is greater than the width, increase line count and reset character count, push the current string to the next line
                lineCount += 1 # Increase the line count by 1
                charCount = len(paragraphs[i]) + 1 # Reset the character count to the length of the current string
                line.append(paragraphs[i] + " ") # Add the current string to the next line
    else: # If the box type is not "box", print out an error
        print("Error: Invalid box type")
    # Print the lines to the console
    for i in range(lineCount + 1):
        print(char + " " + line[i].center(width - 3) + char) # Left justify the string and fill the remaining space with spaces to ensure that each line is the correct width
    print(char * width) # Print the bottom border (char) to the console    