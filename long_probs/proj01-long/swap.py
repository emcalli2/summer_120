""" File: swap.py
    Author: Elizabeth McAllister
    Purpose: Sorts words and count gathered from an inputted file
    Class: Csc 120 Summer 2024
"""
def swap():
    """This function swaps the letters of a string at the halfway point
       Arguments:none
       Return Value: the swapped string
       Pre-condition: there is one string per line
    """
    line = input("Please give a string to swap:")
    line = line.strip()
    swapped = ""
    half = int(len(line)//2)
    # checks if the length is even
    if len(line) % 2 == 0:
        swapped = line[half:] + line[:half]
    else:
        # if the length is not even, the middle char stays the same
        swapped = line[half + 1:] + line[half] + line[:half]
    return swapped

def main():
    print(swap())
main()