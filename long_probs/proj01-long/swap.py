def swap():
    line = input("Please give a string to swap:")
    line = line.strip()
    swapped = ""
    half = int(len(line)//2)
    if len(line) % 2 == 0:
        swapped = line[half:] + line[:half]
    else:
        swapped = line[half + 1:] + line[half] + line[:half]
    return swapped

def main():
    print(swap())
main()