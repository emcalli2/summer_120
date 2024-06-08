def second_largest():
    lst = []
    for i in range(4):
        lst.append(int(input()))
    lst.sort()
    return lst[2]
