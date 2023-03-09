'''
CS5001, Spring 2023
HW05 - Text Editor
Lee Seunghan

This program is a simple text editor that can be used to append, insert, 
substitute, scramble, scramble and unscramble. Please see each function's 
Docstring to find the details of each functions.
'''

def append(current_text: str, new_text: str) -> str:
    '''
    Appends the new text at the end of the current text with a space between,
    and return the new string.
    @Param current_text str: original string that comes before new text
    @Param new_text str: string that is to be appended 
    @Return str: a new concatenated string
    If the appended text has no words, the result is the original text.
    '''
    if not current_text or not new_text: # if either one is empty
        return current_text + new_text # return either one of the string
    curr_lst = current_text.split() # split the list by words
    curr_lst.append(new_text) # append the new text at the end of the list
    return " ".join(curr_lst) # if not return concatenated string

def add(current_text, new_text, start):
    '''
    Insert some text to current text, so that the first word of the new text
    is at a specified position in the return string.
    @Param current_text str: original text to where new text would be added
    @Param new_text str: new text to add to the original text
    @Param start int: starting index where the new text would be added to
    @Return str: string that has new text added to the current text from the
    start position.
    '''
    curr_lst = current_text.split() # Create a list of words from current_text
    if not current_text or not new_text: # If either of the text is empty
        return current_text or new_text # return the one that exists
    if start <= 0: # If start is equal or less than 0, insert new at front
        curr_lst = [new_text] + curr_lst[:]
    else: # Otherwise, insert at the given index or at the back of the list
        curr_lst = curr_lst[:start] + [new_text] + curr_lst[start:]
    return " ".join(curr_lst) # return the string joined with space

def substitute(current_text: str, word: str, new_word: str) -> str:
    '''
    Substitute all occurences of word in the current text with new word and
    return that string.
    @Param current_text str: original text from which to substitute some words 
    @Param word str: word to be replaced in the current text
    @Param new_word int: new word that will replace the specified word 
    @Return str: string that has specified word substituted with a new word
    If the word to be replaced is not found, then return the current text
    '''
    curr_lst = current_text.split() # Create a list of words from current_text
    for i in range(len(curr_lst)): # Loop over the list
        if curr_lst[i] == word: # If word in index i equals the word to replace
            curr_lst[i] = new_word # replace the word with the new word 
    return " ".join(curr_lst) # Return the string delimited with space

def scramble(current_text: str) -> str:
    '''
    Shift each letter by 2 places foward, leaving other characters unchanged.
    @Param current_text str: string that will be scrambled
    @Return str: a string whose letters are shifted each by 2 places
    For y and z, shifting by 2 places will wrap to a and b respectively.
    '''
    # If it is an alphabet
    new_str = ""
    for i in range(len(current_text)):
        c = current_text[i] # get the character in the index i
        new_str += shift(c, 2) # shift the character by 2
    return new_str

def unscramble(current_text: str) -> str:
    '''
    Shift each letter by 2 places backward, leaving other characters unchanged.
    @Param current_text str: string that will be unscrambled
    @Return str: a string whose letters are shifted each by 2 places backwards
    '''
    new_str = ""
    for i in range(len(current_text)):
        c = current_text[i] # get the character in the index i
        new_str += shift(c, -2) # shift the character by 2
    return new_str

def shift(c, shift_val):
    '''
    Helper function for scramble and unscramble function. This will shift
    the input character by 2 if it is either upper or lowercase alphabet.
    @Param char c: character to shift by 2
    @Param int shift_val: number of positions to shift
    @Return char c: character that was shifted by 2
    '''
    if c.isupper(): # if it is uppercase(ASCII value: 65~90)
        c = chr((ord(c) - 65 + shift_val) % 26 + 65) # return character
        # of the ascii value updated by shift_val, and wrap by taking mod of 26
    elif c.islower(): # If it is lowercase(ASCII value: 97~122)
        c = chr((ord(c) - 97 + shift_val) % 26 + 97)
    return c