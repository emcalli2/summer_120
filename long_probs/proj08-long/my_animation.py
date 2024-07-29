import graphics
import random
def grid(win):
    win.line(100,0,100,800,"white",5)
    win.line(200,0,200,800,"white",5)
    win.line(300,0,300,800,"white",5)
    win.line(400,0,400,800,"white",5)
    win.line(500,0,500,800,"white",5)
    win.line(600,0,600,800,"white",5)
    win.line(700,0,700,800,"white",5)
    win.line(0,100,800,100,"white",5)
    win.line(0,200,800,200,"white",5)
    win.line(0,300,800,300,"white",5)
    win.line(0,400,800,400,"white",5)
    win.line(0,500,800,500,"white",5)
    win.line(0,600,800,600,"white",5)
    win.line(0,700,800,700,"white",5)
def main():
    win = graphics.graphics(800, 800, "window_title")
    i = 1
    while not win.is_destroyed():
        grid(win)
        if i == 1:
            grid(win)
            win.ellipse(200,200, 200,200, "pink")
            win.update_frame(10)
            win.clear()
            i = 2
        if i == 2:
            grid(win)
            win.ellipse(300,300,200,200,"pink")
            win.update_frame(10)
            win.clear()
            i = 3
        if i == 3:
            grid(win)
            win.ellipse(400,400,200,200,"pink")
            win.update_frame(10)
            win.clear()
            i = 1
        grid(win)
        win.update_frame(10)
        win.clear()
    win.mainloop()
main()