""" File: count_items.py
    Author: Elizabeth McAllister
    Purpose: Sorts words and count gathered from an inputted file
    Class: Csc 120 Summer 2024
"""
def count():
    """This function prints out steps and ultimately a sorted
       version of the lines of the file
       Arguments:none
       Return Value: none
       Pre-condition: there are only a string and an integer
                        on each line

       Note: 
    """
    filename = input("File to scan: ")
    filename = filename.strip()
    infile = open(filename, "r")
    info = {}
    lst_of_tup = []
    print("STEP 1: THE ORIGINAL DICTONARY")
    for line in infile:
        # ignores any line that is empty or has a #
        if line[0] != "#" and len(line) > 1:
            line = line.strip().split()
            if line[0] in info:
                info[line[0]] = int(info[line[0]]) + int(line[1])
            else:
                info[line[0]] = int(line[1])
        key_list = list(info.keys())
        key_list.sort()
    # sorts by keys
    for i in range(len(key_list)):
        print("Key: " + key_list[i] + " Value: " + str(info[key_list[i]]))

    print("STEP 2: A LIST OF VALUE -> KEY TUPLES")
    for i in range(len(key_list)):
        lst_of_tup.append((info[key_list[i]],key_list[i]))
    print(lst_of_tup)

    print("STEP 3: AFTER SORTING")
    # sorts the tuple
    lst_of_tup.sort()
    print(lst_of_tup)
    
    print("STEP 4: THE ACTUAL OUTPUT")
    for key,value in lst_of_tup:
        print(value + " " + str(key))

def main():
    count()
main()