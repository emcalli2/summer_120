import graphics
import random
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
    randx = 0
    while randx < 500:
        randy = 0
        while randy < 500:
            num = random.randint(0,3)
            north = random.choice([True, False])
            south = random.choice([True, False])
            east = random.choice([True, False])
            west = random.choice([True, False])
            add_blue = random.choice([True, False])
            if num == 0:
                draw_square_line(win,randx + 33,randy + 33,north, east, south, west,add_blue)
            elif num == 1:
                draw_corner(win,randx+35,randy+35,north, east, south, west,add_blue)
            else:
                draw_box_multi(win,randx+35,randy+35,north, east, south, west,add_blue)
            randy += 100
        randx += 100

    win.mainloop()
main()