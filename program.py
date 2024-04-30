# Description: This is a simple Python program that prints "Hello, World!" to the console, for now.
import random
import sys

def print_paragraphs(n):
    n = str(n)
    paragraphs = n.split(" ")
    num_paragraphs = len(paragraphs)  # Count the number of entries in the list
    for i in range(num_paragraphs):
        print(f"Line {i+1}: {paragraphs[i]}")
    
print_paragraphs("test test2 test3 test4")