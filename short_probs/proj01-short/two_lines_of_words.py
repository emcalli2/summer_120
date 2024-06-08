def main():    
    line = input()
    line2 = input()
    line = line.split()
    line2 = line2.split()
    combine = line + line2
    print("The first line was: " + str(line))
    print("The second line was: " + str(line2))
    print("The combination of both lines had " + str(len(combine)) + " words.")
    print("The combined set of words was: " + str(combine))
    combine.sort()
    print("After sorting, the words were: " + str(combine))
    if len(line) < len(line2):
        print("Pairs:")
        for i in range(len(line)):
            print(str(i) + ": " + str(line[i]) + ", " + str(line2[i]))
    else:
        print("Pairs:")
        for i in range(len(line2)):
            print(str(i) + ": " + str(line[i]) + ", " + str(line2[i]))
main()