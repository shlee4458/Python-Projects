'''
CS5001, Spring 2023
HW05 - Text Editor
Lee Seunghan

This is the main function for the text_editor program.
'''
from text_editor import *

def main():
    OPTIONS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    current_text = "" # Initialized current text to an empty string

    while True: # Loop until the user quits
        
        # Print options
        print("a. Start with blank text.")
        print("b. Append to current text")
        print("c. Add text to current text at a specified position.")
        print("d. Substitute a word with another.")
        print("e. Scramble current text.")
        print("f. Unscramble current text.")
        print("g. Print current text.")
        print("h. Quit")
        
        # Ask for user input until the input is in the options
        while True: 
            user_input = input("Type the option: a - h: ")
            if user_input in OPTIONS: 
                break # Break from the loop only when the input is in the options
        
        # Quit the program, if user input is 'h'
        if user_input == 'h': 
            return
    
        # If user input is g, print the text and continue
        if user_input == 'g': 
            print(current_text)
            continue # Go back to the option selection

        # For other input, process the input
        current_text = process_input(user_input, current_text)

def process_input(user_input, current_text):
    '''
    This function processes user input, case-by-case.
    @Param str user_input: user input
    @Param str current_text: text to modify according to user input
    @Return str: string returned according to user's request
    '''
    if user_input == 'a': # If user requests to start with a blank
        return ""

    if user_input == 'b': # If user requests to append
        new_text = input("Enter text to append: ")
        return append(current_text, new_text)

    if user_input == 'c': # If user requests to insert
        new_text = input("Enter text to insert: ")
        start = int(input("Enter the starting index: "))
        return add(current_text, new_text, start)
    
    if user_input == 'd': # If user requests to substitute
        word = input("Enter a word to be replaced: ")
        new_word = input("Enter a word to replace with: ")
        return substitute(current_text, word, new_word)
    
    if user_input == 'e': # If user requests to scramble
        return scramble(current_text)
    
    if user_input == 'f': # If user requests to unscramble
        return unscramble(current_text)
    
if __name__ == "__main__":
    main()