""" 
    File: annoying_recursion_long.py
    Author: Elizabeth McAllister
    Purpose: This program contains a single function; 
            annoying_fibonacci_sequence which uses recusion to 
            create a list of fibonacci numbers for a given number.
            This program only uses recursion, no loops are allowed.
    Class: Csc 120 Summer 2024
"""
def annoying_fibonacci_sequence(n):
    """
    This function returns a list of previous fibonacci numbers 
    all the way up to the nth given number.
    Parameters: n - an integer whos fibonacci numbers we want to know
    Returns: a list of all the fibonacci numbers leading up to and including n.
    Pre-condition: n must be an integer
    """
    # hard coded requirments for n <= 3
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0,1]
    if n == 3:
        return [0,1,1]

    # hard coded with recursion for 4 <= n <= 6
    if n == 4:
        return annoying_fibonacci_sequence(3) + [annoying_fibonacci_sequence(3)[-2] + annoying_fibonacci_sequence(3)[-1]]
    if n == 5:
        return annoying_fibonacci_sequence(4) + [annoying_fibonacci_sequence(4)[-2] + annoying_fibonacci_sequence(4)[-1]]
    if n == 6:
        return annoying_fibonacci_sequence(5) + [annoying_fibonacci_sequence(5)[-2] + annoying_fibonacci_sequence(5)[-1]]

    # all other cases for n > 6 using recursion
    else:
        return annoying_fibonacci_sequence(n-1) + [annoying_fibonacci_sequence(n-1)[-2] + annoying_fibonacci_sequence(n-1)[-1]]


