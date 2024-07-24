def concat_build(n):
    retval = ""
    dummy = retval
    for i in range(n):
        retval += " "
        dummy = retval
    return retval
print(concat_build(2))