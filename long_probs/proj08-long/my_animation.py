import graphics
import random
def grid(win):
    win.line(100,0,100,800,"gray",5)
    win.line(200,0,200,800,"gray",5)
    win.line(300,0,300,800,"gray",5)
    win.line(400,0,400,800,"gray",5)
    win.line(500,0,500,800,"gray",5)
    win.line(600,0,600,800,"gray",5)
    win.line(700,0,700,800,"gray",5)
    win.line(0,100,800,100,"gray",5)
    win.line(0,200,800,200,"gray",5)
    win.line(0,300,800,300,"gray",5)
    win.line(0,400,800,400,"gray",5)
    win.line(0,500,800,500,"gray",5)
    win.line(0,600,800,600,"gray",5)
    win.line(0,700,800,700,"gray",5)

def strting_frame(win):
    win.line(400,200,400,600,"purple",5) # big vert
    win.line(200,400,600,400,"purple",5) # big horizontal

    win.line(300,300,500,100,"green",5) 
    win.line(500,300,300,100,"green",5) 
    win.line(500,500,700,300,"blue",5) 
    win.line(700,500,500,300,"blue",5)
    win.line(300,700,500,500,"yellow",5)
    win.line(500,700,300,500,"yellow",5)
    win.line(100,500,300,300,"pink",5)
    win.line(300,500,100,300,"pink",5)

    win.line(450,100,550,100,"red",5)
    win.line(500,50,500,150,"red",5)

    win.line(250,100,350,100,"red",5)
    win.line(300,50,300,150,"red",5)

    win.line(250,300,350,300,"orange",5)
    win.line(300,250,300,350,"orange",5)

    win.line(450,300,550,300,"red",5)
    win.line(500,250,500,350,"red",5)

    win.line(250,500,350,500,"orange",5)
    win.line(300,450,300,550,"orange",5)

    win.line(50,500,150,500,"orange",5)
    win.line(100,450,100,550,"orange",5)

    win.line(50,300,150,300,"orange",5)
    win.line(100,250,100,350,"orange",5)

    win.line(450,500,550,500,"blue",5)
    win.line(500,450,500,550,"blue",5)

    win.line(450,700,550,700,"blue",5)
    win.line(500,650,500,750,"blue",5)

    win.line(250,500,350,500,"blue",5)
    win.line(300,450,300,550,"blue",5)

    win.line(250,700,350,700,"blue",5)
    win.line(300,650,300,750,"blue",5)

    win.line(650,500,750,500,"pink",5)
    win.line(700,450,700,550,"pink",5)

    win.line(650,300,750,300,"pink",5)
    win.line(700,250,700,350,"pink",5)

    win.line(75,275,125,225,"white",5)
    win.line(125,275,75,225,"white",5)

def main():
    win = graphics.graphics(800, 800, "window_title")
    grid(win)
    strting_frame(win)
    win.mainloop()
main()