def shape_alpha():
    x = [10,20]
    y = [50,60]
    return [x,30,40,y]

def shape_bravo():
    # fix
    x = [123,456]
    y = [789,1024]
    w = [x,y]
    z = [y,x]
    p = [w,z]
    return p

def shape_charlie(arg1):
    x = [arg1,arg1]
    y = [arg1,arg1]
    z = [arg1,arg1]
    w = [x,y]
    return [w,z]

def shape_delta(arg1, arg2):
    x = [arg2]
    y = [arg1,x]
    w = [arg1]
    z = [y,w]
    p = [17]
    return [arg1,arg2,z,p]

def shape_echo(arg1, arg2, arg3):
    x = [arg1,None]
    y = [arg2,None]
    z = [arg3,x]
    x[1] = y
    y[1] = z
    z[1] = x
    return x

