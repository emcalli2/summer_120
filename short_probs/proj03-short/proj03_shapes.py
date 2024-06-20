def grid_of_arrays():
    x = [None,(0,0),None]
    y = [None,(1,0),None]
    z = [None,(2,0),None]
    x[0] = y
    y[0] = z
    a = [None,(0,1),None]
    b = [None,(1,1),None]
    c = [None,(2,1),None]
    x[2] = a
    y[2] = b
    z[2] = c
    a[0] = b
    b[0] = c
    d = [None,(0,2),None]
    e = [None,(1,2),None]
    f = [None,(2,2),None]
    a[2] = d
    b[2] = e
    c[2] = f 
    d[0] = e 
    e[0] = f 
    return x

def main():
    grid_of_arrays()
main()
