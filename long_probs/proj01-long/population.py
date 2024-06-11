def population():
    filename = input("file: ")
    filename = filename.strip()
    infile = open(filename, "r")
    num_of_terr = 0
    population = 0
    states = ""
    for line in infile:
        info = []
        states = ""
        if line[0] != "#" and len(line) > 1:
            line = line.strip().split()
            for word in line:
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

def main():
    population()
main()