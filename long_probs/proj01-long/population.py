""" File: population.py
    Author: Elizabeth McAllister
    Purpose: gains and presents information about
            the population of various states
    Class: Csc 120 Summer 2024
"""
def population():
    """This function prints the state and population 
        of each line in an inputted file, as well as
        gives a total state number and population
        count for the whole file
       Arguments:none
       Return Value: none
       Pre-condition: none

    """
    filename = input("file: ")
    filename = filename.strip()
    infile = open(filename, "r")
    num_of_terr = 0
    population = 0
    states = ""
    for line in infile:
        info = []
        states = ""
        # ignores any lines that are empty or contain #
        if line[0] != "#" and len(line) > 1:
            line = line.strip().split()
            for word in line:
                # checks if the word is a letter
                if word.isalpha():
                    states = states + " " + word
                states = states.strip()
            info.append(states)
            info.append(word)    
            print("State/Territory: " + info[0])
            num_of_terr += 1
            print("Population: " + info[1])
            population += int(info[1])
            print("")
    print("# of States/Territories: " + str(num_of_terr))
    print("Total Population: " + str(population))
    print("CLOSE FILE")
def main():
    population()
main()