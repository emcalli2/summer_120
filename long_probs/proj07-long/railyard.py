""" 
    File: railyard.py
    Author: Elizabeth McAllister
    Purpose: This program deals with a train yard. It reads a 
        yard file and prints out a yard, then takes commands to 
        move the cars and when the cars are all going to the same 
        destination, the train departs. 
    Class: Csc 120 Summer 2024
"""
def rail_yard():
    """
    This function reads an inputted file and creates a rail 
    yard with each line of the file. 
    Parameters: None
    Returns: yard - a list of list of strings that represents the yard
    """
    yardfile = input("Please give the yard file: ")
    print("")
    infile = open(yardfile, 'r')
    yard = []
    num = 1
    loco = 0
    destination = 0
    for line in infile:
        line = line.strip()
        yard.append([line])
    print_yard(yard)
    return yard
def move_command(command,yard):
    """
    This function executes the move command, moving the number of 
    cars from the "from-track" to the "to-track"
    Parameters: command- the inputted command
                yard - a list of list of strings that make up the yard
    Returns: None
    """
    number = int(command[1]) + 1
    if command[1] == 1:
        number = int(command[1])
    if command[1] == 0:
        print_yard(yard)
        return
    from_track = int(command[2]) -1
    to_track = int(command[3]) -1
    length = len(yard[from_track][0]) - number
    cars = yard[from_track][0][-number:-1]
    yard[to_track][0] = yard[to_track][0][number:] + cars + "-"
    # ensures that the length is the same after the cars are removed
    yard[from_track][0] = ("-" * (number-1)) + yard[from_track][0][:length] + "-"
    print("The locomotive on track "+str(from_track+1)+" moved "+str(number -1)+" cars to track "+str(to_track+1)+".")
    print_yard(yard)

def debug_dump(yard):
    """
    This function "dumps" information about the current state of
    of the rail yard. Including contents, length, and track number.
    Parameters: yard - a list of list of strings that make up the yard
    Returns: None
    """
    print("DEBUG OUTPUT:")
    for i in range(len(yard)):
        content = []
        print("Track #" + str(i))
        print("  Length: " + str(len(yard[i][0])-2))
        for k in range(len(yard[i][0])):
            if yard[i][0][-k] != "-":
                content.append(yard[i][0][-k])
        print("  Contents: " + str(content))
    print_yard(yard)

def departing_train(yard):
    """
    This function departs trains that have all cars going to the 
    same location.
    Parameters: yard - a list of list of strings that make up the yard
    Returns: None
    """
    for i in range(len(yard)):
        departing = False
        cars = 0
        if "T" in yard[i][0]:
            for j in range(len(yard[i][0])-3):
                if "-" not in yard[i][0][j]:
                    if yard[i][0][j] == yard[i][0][j+1]:
                        cars += 1
                        departing = True
                    else: 
                        departing = False
                        break
        if departing == True:
            print("*** ALERT***  The train on track " + str(i + 1) + ", which had " + str(cars+1) +
            " cars, departs for destination " + str(yard[i][0][j]) +  ".")
            yard[i][0] = "-" * len(yard[i][0])
    print_yard(yard)
       
def print_yard(yard):
    """
    This function prints out the rail yard as well as information 
    about it such as destination number and locomotive numbers.
    Parameters: yard - a list of list of strings that make up the yard
    Returns: None
    """
    num = 1
    loco = 0
    destination = 0
    destination_list = ["T"]
    for i in range(len(yard)):
        print(str(num) + ": " + yard[i][0])
        num += 1
        for j in range(len(yard[i][0])):
            if "T" in yard[i][0][j]:
                loco += 1
            elif yard[i][0][j] != "-" and yard[i][0][j] not in destination_list:
                destination += 1
                destination_list.append(yard[i][0][j])  
    if loco == 0:
        print("Quitting!")
        quit
    print("Locomotive count: " + str(loco))
    print("Destination count: " + str(destination))
    
def main():
    """
    This main function determins which type the inputted command is.
    And based on that information, runs the appropriate functions.
    It also quits the program if quit is typed.
    Parameters: None
    Returns: None
    """
    yard = rail_yard()
    print("")
    command = input("What is your next command? ")
    print("")
    while "quit" not in command:
        if command == "dump":
            print("")
            debug_dump(yard)
            print("")
            command = input("What is your next command? ")
            print("")
        if "move" in command:
            command = command.strip().split()
            if len(command) != 4:
                print("ERROR: The only valid command formats are (where each X represents an integer): move X X X")
            elif command[1].isalpha():
                print("ERROR: Could not convert the 'count' value to an integer:" + command[1])
            elif command[2].isalpha():
                print("ERROR: Could not convert the 'from-track' value to an integer:" + command[2])
            elif command[3].isalpha():
                print("ERROR: Could not convert the 'to-track' value to an integer:" + command[3])
            elif command[2] == command[3]:
                print("ERROR: The 'to' track is the same as the 'from' track.")
            elif int(command[1]) < 0:
                print("ERROR: Cannot move a negative number of cars.") 
            else:
                move_command(command,yard)
                departing_train(yard)
            print("")
            print_yard(yard)
            print("")
            command = input("What is your next command? ")
            print("")
    if "quit" in command:
        print("Quitting!")
main()