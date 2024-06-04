line = input()
line = line.strip()
second_line = input()
if len(line) == 0:
    print(line)
elif second_line.isnumeric():
    for i in range(int(second_line)):
        print(line)
else:
    print(line)