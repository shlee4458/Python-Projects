'''
CS5001, Spring 2023
HW05 - Text Editor
Lee Seunghan

This program tests functions in the text_editor file.
'''
from text_editor import *

def test_append(current_text, new_text, expected):
    '''
    This function tests append function in the text_editor file.
    @Param str current_text: original text before modification
    @Param str new_text: new_text to be appended
    @Param str expected: expected value of the function
    '''
    actual = append(current_text, new_text)
    print(f"Actual: {actual}, Expected: {expected}, {actual == expected}")
    
def test_add(current_text, new_text, start, expected):
    '''
    This function tests add function in the text_editor file.
    @Param str current_text: original text before modification
    @Param str new_text: new text to be inserted in the start index
    @Param int start: index where to add the new_text
    @Param str expected: expected value of the function
    '''
    actual = add(current_text, new_text, start)
    print(f"Actual: {actual}, Expected:{expected}, {actual == expected}")

def test_substitute(current_text, word, new_word, expected):
    '''
    This function tests substitute function in the text_editor file.
    @Param str current_text: original text before modification
    @Param str word: word to be replaced with the new word
    @Param str new_word: new word to replace the original word
    @Param str expected: expected value of the function
    '''
    actual = substitute(current_text, word, new_word)
    print(f"Actual: {actual}, Expected:{expected}, {actual == expected}")

def test_scramble(current_text, expected):
    '''
    This function tests scramble function in the text_editor file.
    @Param str current_text: original text before modification
    @Param str expected: expected value of the function
    '''
    actual = scramble(current_text)
    print(f"Actual: {actual}, Expected:{expected}, {actual == expected}")

def test_unscramble(current_text, expected):
    '''
    This function tests unscramble function in the text_editor file.
    @Param str current_text: original text before modification
    @Param str expected: expected value of the function
    '''
    actual = unscramble(current_text)
    print(f"Actual: {actual}, Expected:{expected}, {actual == expected}")

def test_substitute_implement():
    '''
    This function is an test implementation of substitute function.
    This will print out each example cases. 
    '''
    # Test if the replacing word is found
    sub_cur_one = "I want to eat sushi"
    sub_word_one = "sushi"
    sub_new_one = "omakase"
    test_substitute(sub_cur_one, sub_word_one, sub_new_one,
                    "I want to eat omakase")

    # Test if the replacing word is not found
    sub_cur_two = "No more pizza please"
    sub_word_two = "sushi"
    sub_new_two = "roll"
    test_substitute(sub_cur_two, sub_word_two, sub_new_two,
                    "No more pizza please")

    # Test if only capitalized word of the new word is in the text
    sub_cur_three = "Are these tests necessary"
    sub_word_three = "Necessary"
    sub_new_three = "fun"
    test_substitute(sub_cur_three, sub_word_three, sub_new_three,
                    "Are these tests necessary")

def test_scramble_implement():
    '''
    This function is an test implementation of scramble function.
    This will print out each example cases. 
    '''
    # Test if original text is scrambled properly -- not containing y/Y, z/Z
    scramble_one = "bCdToFu"
    test_scramble(scramble_one, "dEfVqHw")

    # Test if original text is wrapped properly -- containing y/Y, z/Z
    scramble_two = "bXyZxYz"
    test_scramble(scramble_two, "dZaBzAb")

    # Tests if punctuation are not affected
    scramble_three = "CS61A: Bach"
    test_scramble(scramble_three, "EU61C: Dcej")

def test_unscramble_implement():
    '''
    This function is an test implementation of unscramble function.
    This will print out each example cases. 
    '''
    # Test if original text is scrambled properly -- not containing y/Y, z/Z
    unscramble_one = "dEfVqHw"
    test_unscramble(unscramble_one, "bCdToFu")

    # Test if original text is wrapped properly -- containing y/Y, z/Z
    unscramble_two = "dZaBzAb"
    test_unscramble(unscramble_two, "bXyZxYz")

    # Tests if punctuation are not affected
    unscramble_three = "EU61C: Dcej"
    test_unscramble(unscramble_three, "CS61A: Bach")

def test_append_implement():
    '''
    This function is an test implementation of append function.
    This will print out each example cases. 
    '''
    # Test for punctuation/word preservation
    append_curr_one = "Please," 
    append_new_txt_one = "no point deduction."
    test_append(append_curr_one, append_new_txt_one,
                "Please, no point deduction.")
    
    # Test for the presence of space delimiter
    append_curr_two = "I would eat" 
    append_new_txt_two = "a horse"
    test_append(append_curr_two, append_new_txt_two, "I would eat a horse")

    # Test for the empty current_text
    append_curr_three = ""
    append_new_txt_three = "Hello Hi!"
    test_append(append_curr_three, append_new_txt_three, "Hello Hi!")

    # Test for the empty new_text
    append_curr_four = "Let's learn CS." 
    append_new_txt_four = ""
    test_append(append_curr_four, append_new_txt_four, "Let's learn CS.")

def test_add_implement():
    '''
    This function is an test implementation of add function.
    This will print out each example cases. 
    '''
    # Insert word between index of 0 to the length - 1 of the current text
    add_curr_one = "Is this THE CS course?"
    add_new_one = "BEST"
    add_start_one = 3
    test_add(add_curr_one, add_new_one, add_start_one,
             "Is this THE BEST CS course?")

    # Insert word at position before 0 index of the current text
    add_curr_two = "Hello, Hi!"
    add_new_two = "Emily!"
    add_start_two = -1
    test_add(add_curr_two, add_new_two, add_start_two,
             "Emily! Hello, Hi!")

    # Insert word at position bigger than length - 1 of the current text
    add_curr_three = "Bacon Lettuce"
    add_new_three = "Tomato"
    add_start_three = 6
    test_add(add_curr_three, add_new_three, add_start_three,
             "Bacon Lettuce Tomato")

    # Insert an empty string to the current text
    add_curr_four = ""
    add_new_four = "Bacon Tomato Lettuce"
    add_start_four = 5
    test_add(add_curr_four, add_new_four, add_start_four,
             "Bacon Tomato Lettuce")

    # Insert new string to an empty text
    add_curr_five = "Bacon Lettuce Kimchi"
    add_new_five = ""
    add_start_five = 2
    test_add(add_curr_five, add_new_five, add_start_five,
             "Bacon Lettuce Kimchi")

def main():
    print("-------------This is test for append function.-------------")
    test_append_implement() # Calls implementation of append function
    print("\n")

    print("-------------This is test for add function.-------------")
    test_add_implement() # Calls implementation of add function
    print("\n")

    print("-------------This is test for substitute function.-------------")
    test_substitute_implement() # Calls implementation of substitute function
    print("\n")
    print("-------------This is test for scramble function.-------------")
    test_scramble_implement() # Calls implementation of scramble function
    print("\n")

    print("-------------This is test for unscramble function.-------------")
    test_unscramble_implement() # Calls implementation of unscramble function
    print("\n")

if __name__ == "__main__":
    main()