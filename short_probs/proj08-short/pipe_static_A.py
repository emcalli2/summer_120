import graphics
def draw_square_line(win, x,y,north, east, south, west,add_blue):
    win.rectangle(x,y,35,35,"black")
    if east:
        win.line(x+5,y+16,65+x,y+16,"black",15)
        if add_blue:
            win.line(x,y+16,65+x,y+16,"blue",5)
    if west:
        win.line(x-31,y+16,x+5,y+16,"black",15)
        if add_blue:
            win.line(x-31,y+16,x+5,y+16,"blue",5)

    if south:
        win.line(x+17,y,x+17,y+65,"black",15)
        if add_blue:
            win.line(x+17,y+5,x+17,y+65,"blue",5)
    if add_blue:
        win.rectangle(x+5,y+5,25,25,"blue")
def draw_corner(win, x, y,north,east,south,west,add_blue):
    if south:
        win.line(x+15,y+6,x+15,y+63,"black",15)
    if east:
        win.line(x+7.5,y+13,x+63,y+13,"black",15) 
    if west:
        win.line(x-33,y+13,x+17,y+13,"black",15)
    if north:
        win.line(x+15,y+20,x+15,y-33,"black",15)

    if south and add_blue:
        win.line(x+15,y+6,x+15,y+63,"blue",5)
    if east and add_blue:
        win.line(x+7.5,y+13,x+63,y+13,"blue",5)
    if west and add_blue:
        win.line(x-33,y+13,x+17,y+13,"blue",5)
    if north and add_blue:
        win.line(x+15,y+19,x+15,y-33,"blue",5)

def draw_box_multi(win, x, y,north,east,south,west,add_blue):
    win.rectangle(x-2,y-2,35,35,"black")
    if south:
        win.line(x+15,y+6,x+15,y+63,"black",15)
    if east:
        win.line(x+7.5,y+13,x+63,y+13,"black",15) 
    if west:
        win.line(x-33,y+13,x+17,y+13,"black",15)
    if north:
        win.line(x+15,y+20,x+15,y-33,"black",15)

    if south and add_blue:
        win.line(x+15,y,x+15,y+63,"blue",5)
    if east and add_blue:
        win.line(x,y+13,x+63,y+13,"blue",5)
    if west and add_blue:
        win.line(x-33,y+13,x+15,y+13,"blue",5)
    if north and add_blue:
        win.line(x+15,y,x+15,y-33,"blue",5)
    if add_blue:
        win.rectangle(x+3,y+3,25,25,"blue")

def draw_horizontal(win,x,y):
    win.line(x,y,500,y,"white")

def draw_vertical(win,x,y):
    win.line(x,0,x,y,"white")

def draw_grid(win):
    draw_vertical(win,0,500)
    draw_vertical(win,100,500)
    draw_vertical(win,200,500)
    draw_vertical(win,300,500)
    draw_vertical(win,400,500)
    draw_vertical(win,500,500)

    draw_horizontal(win,0,0)
    draw_horizontal(win,0,100)
    draw_horizontal(win,0,200)
    draw_horizontal(win,0,300)
    draw_horizontal(win,0,400)
    draw_horizontal(win,0,500)


def main():
    win = graphics.graphics(500,500,"Pipe Grid")
    win.rectangle(0,0,500,500,"gray")
    draw_grid(win)

    draw_square_line(win,433,33,north=False, east=False, south=True, west=False,add_blue = False)
    draw_square_line(win,233,133,north=False, east=False, south=False, west=True,add_blue = False)
    draw_square_line(win,133,133,north=False, east=False, south=True, west=False,add_blue = True)
    draw_square_line(win,33,433,north=False, east=False, south=True, west=False,add_blue = False)
    draw_square_line(win,233,433,north=False, east=True, south=False, west=False,add_blue = False)
    draw_square_line(win,333,433,north=False, east=False, south=True, west=False,add_blue = False)
    draw_square_line(win,433,433,north=False, east=False, south=True, west=False,add_blue = False)
    draw_square_line(win,233,33,north=False, east=True, south=False, west=False,add_blue = False)
    draw_square_line(win,433,133,north=False, east=True, south=False, west=False,add_blue = False)
    draw_square_line(win,433,233,north=False, east=False, south=False, west=True,add_blue = False)
    

    draw_corner(win,35,35,north=False,east=True,south=True,west=False,add_blue=False)
    draw_corner(win,235,335,north=True,east=True,south=False,west=False,add_blue=True)
    draw_corner(win,135,435,north=True,east=False,south=False,west=True,add_blue=False)
    draw_corner(win,135,335,north=True,east=True,south=False,west=True,add_blue=True)
    draw_corner(win,35,335,north=False,east=True,south=True,west=False,add_blue=True)
    draw_corner(win,135,235,north=True,east=True,south=True,west=False,add_blue=True)
    draw_corner(win,35,235,north=False,east=True,south=True,west=True,add_blue=False)
    draw_corner(win,335,35,north=False,east=False,south=True,west=True,add_blue=False)
    draw_corner(win,435,335,north=True,east=True,south=False,west=True,add_blue=False)
    draw_corner(win,335,335,north=True,east=True,south=True,west=False,add_blue=False)
    draw_corner(win,335,235,north=False,east=True,south=True,west=True,add_blue=False)
    draw_corner(win,335,135,north=True,east=True,south=False,west=True,add_blue=False)
    draw_corner(win,35,135,north=True,east=False,south=True,west=False,add_blue=False)
    draw_corner(win,135,35,north=False,east=True,south=False,west=True,add_blue=False)

    draw_box_multi(win,235,235,north=True,east=False,south=True,west=True,add_blue=True)

    win.mainloop()
main()