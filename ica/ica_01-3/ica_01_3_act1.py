filename = input()
in_file = open(filename, "r")
for line in in_file:
    if len(line) != 0:
        print("Line length: " + str(len(line)))
    print(line)