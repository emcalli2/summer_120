""" File: strings_and_input.py
    Author: Elizabeth McAllister
    Purpose: Sorts words and count gathered from an inputted file
    Class: Csc 120 Summer 2024
"""
def string_information():  
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
    #read in two numbers
    # convert numbers to integers (use int())
    num1 = int(input())
    num2 = int(input())
    # multiply them together
    # print result
    print(num1 * num2)


def main():
    string_information()
    multiply_nums()
main()