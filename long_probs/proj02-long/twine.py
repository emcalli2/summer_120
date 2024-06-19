""" 
    File: twine.py
    Author: Elizabeth McAllister
    Purpose: this program simulates walking in a forrest lost
            the user inputs directions to move and while
            they move, a string of twine is placed so that 
            steps can be retraced. The user can move n,w,s,e, and
            backwards. As well as can call functions such as range and
            crossings(the amount of times they have been in that spot before)
    Class: Csc 120 Summer 2024
"""
def commands(twine,move):
    """ 
        This function implements various commands such a n,w,s,e, and back
        as well as handles errors and empty lines.
        Arguments: twine (the list of tuples of coordinates)
        Return Value: twine
        Pre-condition: none
    """
    curr_pos = twine[len(twine)-1]
    if len(move.split()) > 1:
        print("ERROR: more than one word was given")
        return twine
    if len(move) == 0:
        print("You do nothing.")
        return twine
    if move in "back":
        if twine == [(0,0)]:
            print("Cannot move back, as you are at the start!")
            return twine
        twine.pop()
        print("You retrace your steps by one space")
        return twine
    # moves north
    if move in "n":
        lst = list(curr_pos)
        lst[1] += 1
        twine.append(tuple(lst))
        return twine
    # moves south
    if move in "s":
        lst = list(curr_pos)
        lst[1] -= 1
        twine.append(tuple(lst))
        return twine
    # moves east
    if move in "e":
        lst = list(curr_pos)
        lst[0] += 1
        twine.append(tuple(lst))
        return twine
    # moves west
    if move in "w":
        lst = list(curr_pos)
        lst[0] -= 1
        twine.append(tuple(lst))
        return twine
    else:
        print("ERROR: command not recognized")
        return twine

def path_map(twine,move):
    """ 
        This is an unfinished version of path_map which places "." where the 
        user has traveled based on the twine list, and a X where the user currently is
        Arguments: twine(list of tuple coordinates)
        Return Value: none
        Pre-condition: map has to be typed into the input for this function to be called
    """
    top_bottom = "+---------+"
    middle = []
    print(top_bottom)
    for i in range(5):
        middle.append(["|         |"])
    # adds a "*" to the coordinate (0,0)
    middle.append(["|    *    |"])
    for i in range(5):
        middle.append(["|         |"])
    # adds dots where the user has been
    for i in range(len(twine)-1):
        lst = list(twine[i+1])
        x = lst[0]
        y = lst[1]
        middle[5-y][0] = "|" + (" " * (x+4)) + "." + (" " * (x+4))+ "|"
    # prints the whole middle of the map
    for i in range(len(middle)):
        print(middle[i][0])
    print(top_bottom)

def crossing(twine):
    """ 
        This function determines how many times the user has previously
        been at their current location 
        Arguments: twine(list of tuple corrdinates)
        Return Value: none
        Pre-condition: user must type crossings to call function
    """
    curr_pos = twine[len(twine)-1]
    count = 0
    for i in range(len(twine)):
        if twine[i] == curr_pos:
            count += 1
    print("There have been " + str(count) + " times in the history when you were at this point.")

def ranges(twine):
    """ 
        This function determines the range of the path the user has taken
        Arguments: twine(list of tuple corrdinates)
        Return Value: none
        Pre-condition: user must input "range" to call this function
        Note: east is highest x value, west is the lowest x value, south
            is the lowest y value, north is the highest y value
    """
    east = None
    west = None
    south = None
    north = None
    lst = []
    for i in range(len(twine)):
        lst = list(twine[i])
        if east is None or lst[0] > east:
            east = lst[0]
        if north is None or lst[1] > north:
            north = lst[1]
        if west is None or lst[0] < west:
            west = lst[0]
        if south is None or lst[1] < south:
            south = lst[1]
    print("The furthest West your twine goes is " + str(west))
    print("The furthest East your twine goes is " + str(east))  
    print("The furthest South your twine goes is " + str(south))
    print("The furthest North your twine goes is " + str(north))

def main():
    print("Please give the name of the obstacles filename, or - for none:")
    input()
    twine = [(0,0)]
    while twine != []:
        try:
            curr_pos = twine[len(twine)-1]
            print("Current position: " + str(curr_pos))
            print("Your history:     " + str(twine))
            print("What is your next command?")
            move = input()
            if "map" in move:
                path_map(twine,move)
            elif "crossings" in move:
                crossing(twine)
            elif "range" in move:
                ranges(twine)
            else:
                commands(twine,move)
        except:
            break
        print()

main()