""" File: strings_and_input.py
    Author: Elizabeth McAllister
    Purpose: prints various information about strings
            such as length, second character, etc. as well
            as multiplies two inputted integers together
    Class: Csc 120 Summer 2024
"""
def string_information():
    """This function prints out information about a string
       Arguments:none
       Return Value: none
       Pre-condition: the input is a string
    """
    # read in an input string
    string = input("input string: ")

    # length of string
    print(len(string))

    # second character in the string
    print(string[1])
    
    # the first 10 char of the string or less if string < 10 (use slicing)
    print(string[0:10])

    # last 5 char in the string
    print(string[len(string) - 5:])

    # the entire string where lowercase char are now upper
    print(string.upper())

    # classify the first char of the string (see specs)
    first_char = string[0]
    if first_char.lower() in "qwerty":
        print("QWERTY")
    elif first_char in "uiop":
        print("UIOP")
    elif first_char.isnumeric():
        print("DIGIT")
    elif first_char.isalpha():
        print("LETTER")
    else:
        print("OTHER")

def multiply_nums():
    """This function multiplies two inputted integers together
       Arguments:none
       Return Value: none
       Pre-condition: the input is an integer
    """
    num1 = int(input())
    num2 = int(input())
    print(num1 * num2)


def main():
    string_information()
    multiply_nums()
main()