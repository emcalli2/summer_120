import graphics

def draw_horizontal(win,x,y):
    win.line(x,y,500,y,"white")

def draw_vertical(win,x,y):
    win.line(x,0,x,y,"white")

def draw_rectangle_with_line(win,x,y):
    win.rectangle(x,y,30,30,"black")
    win.line(x,y+15,65+x,y+15,"black",7)
def main():
    win = graphics.graphics(500,500,"Example")
    win.rectangle(0,0,500,500,"gray")
    draw_horizontal(win,0,0)
    draw_vertical(win,0,500)
    draw_vertical(win,100,500)
    draw_vertical(win,200,500)
    draw_vertical(win,300,500)
    draw_vertical(win,400,500)
    draw_vertical(win,500,500)
    draw_horizontal(win,0,100)
    draw_horizontal(win,0,200)
    draw_horizontal(win,0,300)
    draw_horizontal(win,0,400)
    draw_horizontal(win,0,500)
    draw_rectangle_with_line(win,235,35)
    win.mainloop()
main()
