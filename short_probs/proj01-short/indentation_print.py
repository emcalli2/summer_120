def main():  
    while True:
        line = input()
        count = 0
        if "quit" in line:
            break
        else:
            for i in range(len(line)):
                if " " in line[i]:
                    count += 1
                else:
                    break
            print(count)
main()