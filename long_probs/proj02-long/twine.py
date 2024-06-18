
def commands(twine,move):
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
    if move in "n":
        lst = list(curr_pos)
        lst[1] += 1
        twine.append(tuple(lst))
        return twine
    if move in "s":
        lst = list(curr_pos)
        lst[1] -= 1
        twine.append(tuple(lst))
        return twine
    if move in "e":
        lst = list(curr_pos)
        lst[0] += 1
        twine.append(tuple(lst))
        return twine
    if move in "w":
        lst = list(curr_pos)
        lst[0] -= 1
        twine.append(tuple(lst))
        return twine
    else:
        print("ERROR: command not recognized")
        return twine

def path_map(twine,move):
    top_bottom = "+---------+"
    middle = []
    print(top_bottom)
    for i in range(5):
        middle.append(["|         |"])
    middle.append(["|    *    |"])
    for i in range(5):
        middle.append(["|         |"])
    for i in range(len(twine)-1):
        lst = list(twine[i+1])
        x = lst[0]
        y = lst[1]
        middle[5-y][0] = "|" + (" " * (x+4)) + "." + (" " * (x+4))+ "|"
    for i in range(len(middle)):
        print(middle[i][0])
    print(top_bottom)

def crossing(twine):
    curr_pos = twine[len(twine)-1]
    count = 0
    for i in range(len(twine)):
        if twine[i] == curr_pos:
            count += 1
    print("There have been " + str(count) + " times in the history when you were at this point.")

def ranges(twine):
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

