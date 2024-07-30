import graphics

def fans_arms_up(win):
    win.ellipse(200,100,50,50,"white")
    win.line(200,100,200,200,"white",5)
    win.line(200,150,150,100,"white",5) #left arm
    win.line(200,150,250,100,"white",5) #right arm

    win.ellipse(400,100,50,50,"white")
    win.line(400,100,400,200,"white",5)
    win.line(400,150,350,100,"white",5) #left arm
    win.line(400,150,450,100,"white",5) #right arm

    win.ellipse(600,100,50,50,"white")
    win.line(600,100,600,200,"white",5)
    win.line(600,150,550,100,"white",5) #left arm
    win.line(600,150,650,100,"white",5) #right arm

def fans_arms_down(win):
    win.ellipse(200,100,50,50,"white")
    win.line(200,100,200,200,"white",5)
    win.line(200,150,150,200,"white",5) #left arm
    win.line(200,150,250,200,"white",5) #right arm

    win.ellipse(400,100,50,50,"white")
    win.line(400,100,400,200,"white",5)
    win.line(400,150,350,200,"white",5) #left arm
    win.line(400,150,450,200,"white",5) #right arm

    win.ellipse(600,100,50,50,"white")
    win.line(600,100,600,200,"white",5)
    win.line(600,150,550,200,"white",5) #left arm
    win.line(600,150,650,200,"white",5) #right arm

def starting_frame(win):
    # fans
    win.ellipse(200,100,50,50,"white")
    win.line(200,100,200,200,"white",5)
    win.line(200,150,150,200,"white",5) #left arm
    win.line(200,150,250,200,"white",5) #right arm

    win.ellipse(400,100,50,50,"white")
    win.line(400,100,400,200,"white",5)
    win.line(400,150,350,200,"white",5) #left arm
    win.line(400,150,450,200,"white",5) #right arm

    win.ellipse(600,100,50,50,"white")
    win.line(600,100,600,200,"white",5)
    win.line(600,150,550,200,"white",5) #left arm
    win.line(600,150,650,200,"white",5) #right arm

    # person
    win.ellipse(100,600,50,50,"white") #head
    win.line(100,600,100,700,"white",5) #body
    win.line(100,700,50,750,"white",5) #left leg
    win.line(100,700,150,750,"white",5) # right leg
    win.line(100,650,50,550,"white",5) # left arm
    win.line(100,650,150,550,"white",5) #right arm

def second_frame(win):
    # fans
    win.ellipse(200,100,50,50,"white")
    win.line(200,100,200,200,"white",5)
    win.line(200,150,150,200,"white",5) #left arm
    win.line(200,150,250,200,"white",5) #right arm

    win.ellipse(400,100,50,50,"white")
    win.line(400,100,400,200,"white",5)
    win.line(400,150,350,200,"white",5) #left arm
    win.line(400,150,450,100,"white",5) #right arm

    win.ellipse(600,100,50,50,"white")
    win.line(600,100,600,200,"white",5)
    win.line(600,150,550,100,"white",5) #left arm
    win.line(600,150,650,100,"white",5) #right arm

    # person
    win.ellipse(100,600,50,50,"white") #head
    win.line(100,600,100,700,"white",5) #body
    win.line(100,700,100,750,"white",5) #left leg
    win.line(100,700,150,750,"white",5) # right leg
    win.line(100,650,50,550,"white",5) # left arm
    win.line(100,650,150,700,"white",5) #right arm
    
def third_frame(win):
    # fans
    win.ellipse(200,100,50,50,"white")
    win.line(200,100,200,200,"white",5)
    win.line(200,150,150,100,"white",5) #left arm
    win.line(200,150,250,200,"white",5) #right arm

    win.ellipse(400,100,50,50,"white")
    win.line(400,100,400,200,"white",5)
    win.line(400,150,350,100,"white",5) #left arm
    win.line(400,150,450,100,"white",5) #right arm

    win.ellipse(600,100,50,50,"white")
    win.line(600,100,600,200,"white",5)
    win.line(600,150,550,100,"white",5) #left arm
    win.line(600,150,650,200,"white",5) #right arm

    # person
    win.ellipse(100,600,50,50,"white") #head
    win.line(100,600,100,700,"white",5) #body
    win.line(100,700,100,750,"white",5) #left leg
    win.line(100,700,150,750,"white",5) # right leg
    win.line(100,650,150,650,"white",5) # left arm
    win.line(100,650,150,700,"white",5) #right arm

def fourth_frame(win):
    # fans
    win.ellipse(200,100,50,50,"white")
    win.line(200,100,200,200,"white",5)
    win.line(200,150,150,200,"white",5) #left arm
    win.line(200,150,250,200,"white",5) #right arm

    win.ellipse(400,100,50,50,"white")
    win.line(400,100,400,200,"white",5)
    win.line(400,150,350,200,"white",5) #left arm
    win.line(400,150,450,200,"white",5) #right arm

    win.ellipse(600,100,50,50,"white")
    win.line(600,100,600,200,"white",5)
    win.line(600,150,550,200,"white",5) #left arm
    win.line(600,150,650,200,"white",5) #right arm

    # person
    win.ellipse(200,600,50,50,"white") #head
    win.line(200,600,100,700,"white",5) #body
    win.line(100,700,100,750,"white",5) #left leg
    win.line(100,700,150,750,"white",5) # right leg
    win.line(150,650,200,650,"white",5) # left arm
    win.line(150,650,200,700,"white",5) #right arm

def fifth_frame(win):
    fans_arms_down(win)
    # person
    win.ellipse(250,600,50,50,"white") #head
    win.line(250,600,100,650,"white",5) #body
    win.line(100,650,50,675,"white",5) #left leg
    win.line(100,650,150,700,"white",5) # right leg
    win.line(200,620,225,700,"white",5) # left arm
    win.line(200,620,200,700,"white",5) #right arm

def six_frame(win):
    fans_arms_up(win)
    # person
    win.ellipse(200,600,50,50,"white") #head
    win.line(200,600,200,500,"white",5) #body
    win.line(200,500,150,450,"white",5) #left leg
    win.line(200,500,250,450,"white",5) # right leg
    win.line(200,550,250,700,"white",5) # left arm
    win.line(200,550,175,700,"white",5) #right arm

def seventh_frame(win):
    fans_arms_down(win)
    # person
    win.ellipse(200,600,50,50,"white") #head
    win.line(200,600,250,500,"white",5) #body
    win.line(250,500,200,450,"white",5) #left leg
    win.line(250,500,300,450,"white",5) # right leg
    win.line(200,600,250,700,"white",5) # left arm
    win.line(200,600,150,650,"white",5) #right arm

def eigth_frame(win):
    fans_arms_down(win)
    # person
    win.ellipse(250,600,50,50,"white") #head
    win.line(250,600,350,550,"white",5) #body
    win.line(350,550,350,500,"white",5) #left leg
    win.line(350,550,400,600,"white",5) # right leg
    win.line(300,575,250,700,"white",5) # left arm
    win.line(300,575,200,650,"white",5) #right arm

def nineth_frame(win):
    fans_arms_down(win)
    # person
    win.ellipse(250,600,50,50,"white") #head
    win.line(250,600,350,600,"white",5) #body
    win.line(350,600,350,650,"white",5) #left leg
    win.line(350,600,400,600,"white",5) # right leg
    win.line(300,600,250,700,"white",5) # left arm
    win.line(300,600,200,600,"white",5) #right arm

def tenth_frame(win):
    # fans
    fans_arms_down(win)
    # person
    win.ellipse(250,600,50,50,"white") #head
    win.line(250,600,350,650,"white",5) #body
    win.line(350,650,350,700,"white",5) #left leg
    win.line(350,650,400,650,"white",5) # right leg
    win.line(300,625,250,700,"white",5) # left arm
    win.line(250,600,200,600,"white",5) #right arm

def eleventh_frame(win):
    # fans
    win.ellipse(200,100,50,50,"white")
    win.line(200,100,200,200,"white",5)
    win.line(200,150,150,200,"white",5) #left arm
    win.line(200,150,250,100,"white",5) #right arm

    win.ellipse(400,100,50,50,"white")
    win.line(400,100,400,200,"white",5)
    win.line(400,150,350,200,"white",5) #left arm
    win.line(400,150,450,100,"white",5) #right arm

    win.ellipse(600,100,50,50,"white")
    win.line(600,100,600,200,"white",5)
    win.line(600,150,550,200,"white",5) #left arm
    win.line(600,150,650,100,"white",5) #right arm

    # person
    win.ellipse(350,550,50,50,"white") #head
    win.line(350,550,350,650,"white",5) #body
    win.line(350,650,350,700,"white",5) #left leg
    win.line(350,650,400,700,"white",5) # right leg
    win.line(350,600,400,550,"white",5) # left arm
    win.line(350,600,300,550,"white",5) #right arm

def twelvth_frame(win):
    # fans
    win.ellipse(200,100,50,50,"white")
    win.line(200,100,200,200,"white",5)
    win.line(200,150,150,100,"white",5) #left arm
    win.line(200,150,250,200,"white",5) #right arm

    win.ellipse(400,100,50,50,"white")
    win.line(400,100,400,200,"white",5)
    win.line(400,150,350,100,"white",5) #left arm
    win.line(400,150,450,200,"white",5) #right arm

    win.ellipse(600,100,50,50,"white")
    win.line(600,100,600,200,"white",5)
    win.line(600,150,550,100,"white",5) #left arm
    win.line(600,150,650,200,"white",5) #right arm

    # person
    win.ellipse(350,550,50,50,"white") #head
    win.line(350,550,350,650,"white",5) #body
    win.line(350,650,350,700,"white",5) #left leg
    win.line(350,650,350,700,"white",5) # right leg
    win.line(350,600,350,500,"white",5) # left arm
    win.line(350,600,350,500,"white",5) #right arm

def thirteenth_frame(win):
    # fans
    win.ellipse(200,100,50,50,"white")
    win.line(200,100,200,200,"white",5)
    win.line(200,150,150,150,"white",5) #left arm
    win.line(200,150,250,150,"white",5) #right arm

    win.ellipse(400,100,50,50,"white")
    win.line(400,100,400,200,"white",5)
    win.line(400,150,350,150,"white",5) #left arm
    win.line(400,150,450,150,"white",5) #right arm

    win.ellipse(600,100,50,50,"white")
    win.line(600,100,600,200,"white",5)
    win.line(600,150,550,150,"white",5) #left arm
    win.line(600,150,650,150,"white",5) #right arm

    # person
    win.ellipse(400,550,50,50,"white") #head
    win.line(400,550,400,650,"white",5) #body
    win.line(350,650,350,700,"white",5) #left leg
    win.line(350,650,400,650,"white",5)#knee
    win.line(350,650,350,700,"white",5) # right leg
    win.line(400,600,400,500,"white",5) # left arm
    win.line(400,600,400,500,"white",5) #right arm

def fourteenth_frame(win):
    # fans
    win.ellipse(200,100,50,50,"white")
    win.line(200,100,200,200,"white",5)
    win.line(200,150,150,150,"white",5) #left arm
    win.line(200,150,250,150,"white",5) #right arm

    win.ellipse(400,100,50,50,"white")
    win.line(400,100,400,200,"white",5)
    win.line(400,150,350,150,"white",5) #left arm
    win.line(400,150,450,150,"white",5) #right arm

    win.ellipse(600,100,50,50,"white")
    win.line(600,100,600,200,"white",5)
    win.line(600,150,550,150,"white",5) #left arm
    win.line(600,150,650,150,"white",5) #right arm

    # person
    win.ellipse(450,550,50,50,"white") #head
    win.line(450,550,400,650,"white",5) #body
    win.line(400,650,350,700,"white",5) #left leg
    win.line(425,600,500,500,"white",5) # left arm

def fifteenth_frame(win):
    # fans
    win.ellipse(200,100,50,50,"white")
    win.line(200,100,200,200,"white",5)
    win.line(200,150,150,100,"white",5) #left arm
    win.line(200,150,250,100,"white",5) #right arm

    win.ellipse(400,100,50,50,"white")
    win.line(400,100,400,200,"white",5)
    win.line(400,150,350,100,"white",5) #left arm
    win.line(400,150,450,100,"white",5) #right arm

    win.ellipse(600,100,50,50,"white")
    win.line(600,100,600,200,"white",5)
    win.line(600,150,550,100,"white",5) #left arm
    win.line(600,150,650,100,"white",5) #right arm

    # person
    win.ellipse(500,550,50,50,"white") #head
    win.line(500,550,400,650,"white",5) #body
    win.line(400,650,350,700,"white",5) #left leg
    win.line(450,600,550,550,"white",5) # left arm

def sixteenth_frame(win):
    # fans
    win.ellipse(200,100,50,50,"white")
    win.line(200,100,200,200,"white",5)
    win.line(200,150,150,100,"white",5) #left arm
    win.line(200,150,250,100,"white",5) #right arm

    win.ellipse(400,100,50,50,"white")
    win.line(400,100,400,200,"white",5)
    win.line(400,150,350,100,"white",5) #left arm
    win.line(400,150,450,100,"white",5) #right arm

    win.ellipse(600,100,50,50,"white")
    win.line(600,100,600,200,"white",5)
    win.line(600,150,550,100,"white",5) #left arm
    win.line(600,150,650,100,"white",5) #right arm

    # person
    win.ellipse(550,600,50,50,"white") #head
    win.line(550,600,450,600,"white",5) #body
    win.line(450,600,400,650,"white",5) #body
    win.line(550,600,600,650,"white",5) # left arm

def seventeenth_frame(win):
    # fans
    fans_arms_down(win)

    # person
    win.ellipse(600,650,50,50,"white") #head
    win.line(600,650,550,550,"white",5) #body
    win.line(550,550,500,525,"white",5) #leg
    win.line(600,650,600,700,"white",5) # left arm

def eighteenth_frame(win):
    # fans
    fans_arms_down(win)

    # person
    win.ellipse(600,650,50,50,"white") #head
    win.line(600,650,650,550,"white",5) #body
    win.line(650,550,700,525,"white",5) #leg
    win.line(600,650,600,700,"white",5) # left arm

def nineteenth_frame(win):
    fans_arms_down(win)

    # person
    win.ellipse(700,550,50,50,"white") #head
    win.line(700,550,700,650,"white",5) #body
    win.line(700,650,700,700,"white",5) #leg
    win.line(700,550,700,500,"white",5) # left arm

def twenty_frame(win):
    fans_arms_up(win)
    win.line(100,100,100,150,"yellow",5)
    win.ellipse(130,125,40,40,"yellow")
    win.ellipse(130,125,20,20,"black")

    win.line(300,100,300,150,"yellow",5)
    win.ellipse(330,125,40,40,"yellow")
    win.ellipse(330,125,20,20,"black")

    win.line(500,100,500,150,"yellow",5)
    win.ellipse(530,125,40,40,"yellow")
    win.ellipse(530,125,20,20,"black")
    # person
    win.ellipse(750,600,50,50,"white") #head
    win.line(750,600,750,700,"white",5) #body
    win.line(750,700,750,750,"white",5) #leg
    win.line(750,650,700,600,"white",5) # left arm

def twentyone_frame(win):
    win.line(100,100,100,150,"yellow",5)
    win.ellipse(130,125,40,40,"yellow")
    win.ellipse(130,125,20,20,"black")

    win.line(300,100,300,150,"yellow",5)
    win.ellipse(330,125,40,40,"yellow")
    win.ellipse(330,125,20,20,"black")

    win.line(500,100,500,150,"yellow",5)
    win.ellipse(530,125,40,40,"yellow")
    win.ellipse(530,125,20,20,"black")
    # fans
    win.ellipse(200,100,50,50,"white")
    win.line(200,100,200,200,"white",5)
    win.line(200,150,150,100,"white",5) #left arm
    win.line(200,150,250,100,"white",5) #right arm

    win.ellipse(400,100,50,50,"white")
    win.line(400,100,400,200,"white",5)
    win.line(400,150,350,100,"white",5) #left arm
    win.line(400,150,450,100,"white",5) #right arm

    win.ellipse(600,100,50,50,"white")
    win.line(600,100,600,200,"white",5)
    win.line(600,150,550,100,"white",5) #left arm
    win.line(600,150,650,100,"white",5) #right arm

    # person
    win.ellipse(750,650,50,50,"white") #head
    win.line(750,650,750,750,"white",5) #body
    win.line(750,750,750,800,"white",5) #leg
    win.line(750,700,700,650,"white",5) # left arm
    win.line(750,700,800,650,"white",5) # right arm
def main():
    win = graphics.graphics(800, 800, "window_title")
    i = 0
    while not win.is_destroyed():
        win.rectangle(0,0,800,800,"black")
        # stands
        win.rectangle(100,200,600,50,"red")
        #floor
        win.rectangle(0,750,200,50,"blue")
        # beam
        win.rectangle(175,700,500,50,"purple")
        win.line(300,700,300,800,"purple",5)
        win.line(600,700,600,800,"purple",5)
        if i == 0:
            starting_frame(win)
        if i == 1:
            second_frame(win)
        if i == 2:
            third_frame(win)
        if i == 3:
            fourth_frame(win)
        if i == 4:
            fifth_frame(win)
        if i == 5:
            six_frame(win)
        if i == 6:
            seventh_frame(win)
        if i == 7:
            eigth_frame(win)
        if i == 8:
            nineth_frame(win)
        if i == 9:
            tenth_frame(win)
        if i == 10:
            eleventh_frame(win)
        if i == 11:
            twelvth_frame(win)
        if i == 12:
            thirteenth_frame(win)
        if i == 13:
            fourteenth_frame(win)
        if i == 14:
            fifteenth_frame(win)
        if i == 15:
            sixteenth_frame(win)
        if i == 16:
            seventeenth_frame(win)
        if i == 17:
            eighteenth_frame(win)
        if i == 18:
            nineteenth_frame(win)
        if i == 19:
            twenty_frame(win)
        if i == 20:
            twentyone_frame(win)
        if i == 21:
            i = -1
        win.update_frame(5)
        win.clear()
        i += 1
    win.mainloop()
main()