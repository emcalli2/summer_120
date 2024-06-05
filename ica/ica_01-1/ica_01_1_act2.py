line = input()
second_line = input()
if second_line.isnumeric():
    for i in range(int(second_line)):
        line = line.strip()
        print(line)
else:
    print(line)
