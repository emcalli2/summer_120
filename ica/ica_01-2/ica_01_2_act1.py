line = input()
second_line = input()
if line == second_line:
    print(line)
elif int(line) < int(second_line):
    for i in range(int(line), int(second_line) + 1):
        print(i)
else:
    for i in range(int(line), int(second_line) -1,-1):
        print(i)